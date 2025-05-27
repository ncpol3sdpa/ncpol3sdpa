from typing import Tuple, List, Optional
from numpy.typing import NDArray

import warnings
import numpy as np
import mosek

from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver


def to_sparse_symmetric(
    matrix: NDArray[np.float64] | NDArray[np.complex64],
) -> Tuple[List[float], List[int], List[int]]:
    """
    Return the sparse form of a symmetric matrix (only lower triangle is given)
    Exemple:
    >>> to_sparse([
    ... [a, 0, b],
    ... [0, 0, c],
    ... [b, c, 0]
    ... ])
    [
    [a, b, c],
    [0, 2, 2],
    [0, 0, 1]
    ]
    """
    n = len(matrix)
    val = []
    rows = []
    cols = []
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] != 0:
                val.append(matrix[i][j])
                rows.append(i)
                cols.append(j)
    return val, rows, cols


def de_linearize(vec: NDArray[np.float64]) -> NDArray[np.float64]:
    """Converts a linearized, lower triangular symmetric matrix array used by mosek
    to a conventional numpy matrix"""
    matrix_size = int(np.sqrt(1 + 8 * len(vec)) - 1) // 2
    if matrix_size * (matrix_size + 1) / 2 != len(vec):
        raise ValueError("vec should be of dimension n(n+1)/2")

    result = np.zeros((matrix_size, matrix_size), dtype=np.float64)
    for i in range(matrix_size):
        for j in range(i + 1):
            index = j + ((i + 1) * i // 2)
            value = vec[index]
            result[i][j] = value
            result[j][i] = value
    return result


def parse_mosek_solution(problem: ProblemSDP, task: mosek.Task) -> Solution_SDP:
    solution_type = mosek.soltype.itr
    primal_objective_value = task.getprimalobj(solution_type)
    dual_objective_value = task.getdualobj(solution_type)

    # Sanity check: in our case, the  dual objective is <e0 | slc - suc> = <e0 | y> = y_0
    # https://docs.mosek.com/latest/pythonapi/prob-def-semidef.html#index-11
    dual_alt = (
        task.getslcslice(solution_type, 0, 1)[0]
        - task.getsucslice(solution_type, 0, 1)[0]
    )
    assert abs(dual_objective_value - dual_alt) <= 0.01

    # pre-allocate the arrays to be filled in. They are stored as a list by mosek
    primal_variables_lin = [
        np.zeros(n * (n + 1) // 2, dtype=np.float64) for n in problem.variable_sizes
    ]
    dual_variables_lin = [
        np.zeros(n * (n + 1) // 2, dtype=np.float64) for n in problem.variable_sizes
    ]

    for i in range(len(problem.variable_sizes)):
        task.getbarxj(solution_type, i, primal_variables_lin[i])
        task.getbarsj(solution_type, i, dual_variables_lin[i])

    primal_variables = [de_linearize(var) for var in primal_variables_lin]
    dual_variables = [-de_linearize(var) for var in dual_variables_lin]

    return Solution_SDP(
        primal_objective_value=primal_objective_value,
        primal_variables=primal_variables,
        dual_objective_value=dual_objective_value,
        dual_variables=dual_variables,
    )


class MosekSolver(Solver):
    @classmethod
    def solve(self, problem: ProblemSDP) -> Solution_SDP:
        """Solve the SDP problem with mosek"""

        # Convert constraints inside the moment matrix to primal form constraints
        problem.compile_moment_matrix_to_constraints()

        # Define a stream printer to grab output from MOSEK
        def stream_printer(text: str) -> None:
            # sys.stdout.write(text)
            # sys.stdout.flush()
            pass

        def mosek_task() -> Optional[Solution_SDP]:
            # Create a task object and attach log stream printer
            with mosek.Task() as task:
                task.set_Stream(mosek.streamtype.log, stream_printer)

                # Append #problem.variable_sizes symmetric variables of dimension problem.variable_sizes
                task.appendbarvars(problem.variable_sizes)

                # objective function
                val_obj, rows_obj, cols_obj = to_sparse_symmetric(problem.objective)
                task.putbarcblocktriplet(
                    [problem.MOMENT_MATRIX_VAR_NUM] * len(val_obj),
                    rows_obj,
                    cols_obj,
                    val_obj,
                )
                # Append the contraints
                number_of_constraints = len(problem.constraints)
                task.appendcons(number_of_constraints + 1)

                # Adds the normalisation constraint
                task.putbarablocktriplet(
                    [0], [problem.MOMENT_MATRIX_VAR_NUM], [0], [0], [1]
                )

                # Adds constraints
                for i in range(number_of_constraints):
                    which_constraint = []
                    which_SDP = []
                    constraint_k = []
                    constraint_l = []
                    constraint_v = []
                    for var_num, matrix in problem.constraints[i].constraints:
                        val_m, rows_m, cols_m = to_sparse_symmetric(matrix)  # type
                        which_constraint += [1 + i] * len(val_m)
                        which_SDP += [var_num] * len(val_m)
                        constraint_k += rows_m
                        constraint_l += cols_m
                        constraint_v += val_m
                    task.putbarablocktriplet(
                        which_constraint,
                        which_SDP,
                        constraint_k,
                        constraint_l,
                        constraint_v,
                    )

                # Set bounds for constraints
                task.putconboundlist(
                    list(range(number_of_constraints + 1)),
                    [mosek.boundkey.fx for _ in range(number_of_constraints + 1)],
                    [1.0] + [0.0 for _ in range(number_of_constraints)],
                    [1] + [0 for _ in range(number_of_constraints)],
                )

                # Optimize
                task.putobjsense(mosek.objsense.maximize)
                task.optimize()

                # Get solution status
                solution_status = task.getsolsta(mosek.soltype.itr)

                # Handle solution cases
                if solution_status == mosek.solsta.optimal:
                    return parse_mosek_solution(problem=problem, task=task)

                elif solution_status in [
                    mosek.solsta.dual_infeas_cer,
                    mosek.solsta.prim_infeas_cer,
                ]:
                    warnings.warn("Infeasible")
                    return None  # Primal or dual infeasibility certificate found
                elif solution_status == mosek.solsta.unknown:
                    warnings.warn("Unknown solution status")
                    return None  # Unknown solution status
                else:
                    warnings.warn("Other solution status: ", solution_status)
                    return None  # Other solution status

        # TODO implement getting the dual solution out of mosek
        try:
            return mosek_task()  # type: ignore
        except mosek.MosekException as e:
            warnings.warn(f"Mosek exception : {e}")
            return None  # type: ignore
        # except Exception as e:
        #     warnings.warn(f"Other exception : {e}")
        #     return None  # type: ignore
