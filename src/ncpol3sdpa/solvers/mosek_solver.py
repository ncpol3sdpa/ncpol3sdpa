from typing import Tuple, List, Union
import warnings

from numpy.typing import NDArray
import numpy as np
import mosek

from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver


def to_sparse_symmetric(
    matrix: Union[NDArray[np.float64], NDArray[np.complex64]],
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


class MosekSolver(Solver):
    @classmethod
    def solve(self, problem: ProblemSDP) -> float:
        """Solve the SDP problem with mosek"""

        # Convert constraints inside the moment matrix to primal form constraints
        problem.compile_moment_matrix_to_constraints()

        # Define a stream printer to grab output from MOSEK
        def stream_printer(text: str) -> None:
            # sys.stdout.write(text)
            # sys.stdout.flush()
            pass

        def mosek_task() -> float:
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
                    optimal = task.getprimalobj(
                        mosek.soltype.itr
                    )  # Return optimal value
                    assert isinstance(optimal, float)
                    return optimal

                elif solution_status in [
                    mosek.solsta.dual_infeas_cer,
                    mosek.solsta.prim_infeas_cer,
                ]:
                    warnings.warn("Infeasible")
                    return float(
                        "inf"
                    )  # Primal or dual infeasibility certificate found
                elif solution_status == mosek.solsta.unknown:
                    warnings.warn("Unknown solution status")
                    return float("nan")  # Unknown solution status

                else:
                    warnings.warn("Other solution status: ", solution_status)
                    return float("nan")  # Other solution status

        try:
            return mosek_task()
        except mosek.MosekException as e:
            warnings.warn(f"Mosek exception : {e}")
            return float("nan")
        except Exception as e:
            warnings.warn(f"Other exception : {e}")
            return float("nan")
