from typing import Tuple, List
from numpy.typing import NDArray

import warnings
import numpy as np

import mosek
from scipy.sparse import lil_matrix

from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver


def get_sparse_vecs(
    matrix: lil_matrix,
) -> Tuple[List[float], List[int], List[int]]:
    """
    Return the sparse form of a symmetric matrix stored as a lil_matrix,
    considering only the lower triangle (including diagonal).

    Args:
        matrix: lil_matrix, square sparse matrix.

    Returns:
        Tuple of lists: (values, rows, cols)
    """
    n = matrix.shape[0]
    values = []
    rows = []
    cols = []

    # itérer sur chaque ligne
    for i in range(n):
        # colonnes non-nulles sur la ligne i
        row_cols = matrix.rows[i]
        # valeurs correspondantes
        row_data = matrix.data[i]
        for idx, j in enumerate(row_cols):
            if j <= i:  # on ne garde que la partie inférieure (y compris la diagonale)
                values.append(row_data[idx])
                rows.append(i)
                cols.append(j)

    return values, rows, cols


def de_linearize(vec: NDArray[np.float64]) -> NDArray[np.float64]:
    """Converts a linearized, lower triangular symmetric matrix array used by mosek
    to a conventional numpy matrix"""
    matrix_size = int(np.sqrt(1 + 8 * len(vec)) - 1) // 2
    if matrix_size * (matrix_size + 1) / 2 != len(vec):
        raise ValueError("vec should be of dimension n(n+1)/2")

    result = np.zeros((matrix_size, matrix_size), dtype=np.float64)
    index = 0
    for i in range(matrix_size):
        for j in range(i, matrix_size):
            value = vec[index]
            result[i][j] = value
            result[j][i] = value
            index += 1
    return result


def parse_mosek_solution(
    problem: ProblemSDP, task: mosek.Task, n_eq_constrants: int
) -> Solution_SDP[np.float64]:
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
    primal_PSD_variables_lin = [
        np.zeros(n * (n + 1) // 2, dtype=np.float64) for n in problem.variable_sizes
    ]
    dual_PSD_variables_lin = [
        np.zeros(n * (n + 1) // 2, dtype=np.float64) for n in problem.variable_sizes
    ]

    for i in range(len(problem.variable_sizes)):
        task.getbarxj(solution_type, i, primal_PSD_variables_lin[i])
        task.getbarsj(solution_type, i, dual_PSD_variables_lin[i])

    primal_PSD_variables = [de_linearize(var) for var in primal_PSD_variables_lin]
    # despite what the MOSEK docs might suggest, barsj are negative semidefinite variables
    dual_PSD_variables = [-de_linearize(var) for var in dual_PSD_variables_lin]

    # The first y is the dual_objective, then come the equality constraints.
    dual_eqC_variables = np.zeros(n_eq_constrants, dtype=np.float64)
    task.getyslice(solution_type, 1, 1 + n_eq_constrants, dual_eqC_variables)
    dual_eqC_variables *= -1.0

    n_scalar_ineq_constrains = len(problem.inequality_scalar_constraints)
    dual_ineqC_variables = np.zeros(n_eq_constrants, dtype=np.float64)
    task.getyslice(
        solution_type,
        1 + n_eq_constrants,
        1 + n_eq_constrants + n_scalar_ineq_constrains,
        dual_ineqC_variables,
    )
    dual_ineqC_variables *= -1.0

    return Solution_SDP(
        primal_objective_value=primal_objective_value,
        primal_PSD_variables=primal_PSD_variables,
        dual_objective_value=dual_objective_value,
        dual_PSD_variables=dual_PSD_variables,
        dual_eqC_variables=dual_eqC_variables,
        dual_ineqC_variables=dual_ineqC_variables,
    )


class MosekSolver(Solver):
    @classmethod
    def solve(self, problem: ProblemSDP) -> Solution_SDP[np.float64]:
        """Solve the SDP problem with mosek"""

        # Gets the number of equ constraints to decode the solution
        n_eq_constrants = len(problem.constraints)

        # Convert constraints inside the moment matrix to primal form constraints
        problem.compile_moment_matrix_to_constraints()

        # Define a stream printer to grab output from MOSEK
        def stream_printer(text: str) -> None:
            # sys.stdout.write(text)
            # sys.stdout.flush()
            # print(text, end="")
            pass

        def mosek_task() -> Solution_SDP[np.float64] | None:
            # Create a task object and attach log stream printer
            with mosek.Task() as task:
                task.set_Stream(mosek.streamtype.log, stream_printer)

                # Append #problem.variable_sizes symmetric variables of dimension problem.variable_sizes
                task.appendbarvars(problem.variable_sizes)

                # objective function
                val_obj, rows_obj, cols_obj = get_sparse_vecs(problem.objective)
                task.putbarcblocktriplet(
                    [problem.MOMENT_MATRIX_VAR_NUM] * len(val_obj),
                    rows_obj,
                    cols_obj,
                    val_obj,
                )
                # Append the contraints
                number_of_constraints = len(problem.constraints)
                number_of_scalar_constraints = len(
                    problem.inequality_scalar_constraints
                )
                task.appendcons(
                    number_of_constraints + number_of_scalar_constraints + 1
                )

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
                        val_m, rows_m, cols_m = get_sparse_vecs(matrix)
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

                for i in range(number_of_scalar_constraints):
                    which_constraint = []
                    which_SDP = []
                    constraint_k = []
                    constraint_l = []
                    constraint_v = []
                    var_num, matrix = problem.inequality_scalar_constraints[
                        i
                    ].constraints
                    val_m, rows_m, cols_m = get_sparse_vecs(matrix)
                    which_constraint += [1 + i + number_of_constraints] * len(val_m)
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
                    list(
                        range(number_of_constraints + number_of_scalar_constraints + 1)
                    ),
                    [mosek.boundkey.fx for _ in range(number_of_constraints + 1)]
                    + [mosek.boundkey.lo for _ in range(number_of_scalar_constraints)],
                    [1.0]
                    + [
                        0.0
                        for _ in range(
                            number_of_constraints + number_of_scalar_constraints
                        )
                    ],
                    [1]
                    + [0 for _ in range(number_of_constraints)]
                    + [float("inf") for _ in range(number_of_scalar_constraints)],  # type: ignore
                )

                # Optimize
                task.putobjsense(mosek.objsense.maximize)
                task.optimize()

                # Get solution status
                solution_status = task.getsolsta(mosek.soltype.itr)

                # Handle solution cases
                if solution_status == mosek.solsta.optimal:
                    return parse_mosek_solution(problem, task, n_eq_constrants)

                elif solution_status in [
                    mosek.solsta.dual_infeas_cer,
                    mosek.solsta.prim_infeas_cer,
                ]:
                    warnings.warn("Infeasible")
                    return None  # Primal or dual infeasibility certificate found
                elif solution_status == mosek.solsta.unknown:
                    warnings.warn("Unknown solution status")

                    # Unknown solution status
                    # In the mosek docs: `Solution status UNKNOWN does not necessarily mean that the solution is completely useless`
                    return parse_mosek_solution(problem, task, n_eq_constrants)
                else:
                    # task.analyzeproblem(mosek.streamtype.msg)
                    # task.solutionsummary(mosek.streamtype.msg)
                    warnings.warn(f"Other solution status: {solution_status}")
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
