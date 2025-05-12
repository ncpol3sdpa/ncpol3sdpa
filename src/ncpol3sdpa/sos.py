from typing import List, Any

from numpy.typing import NDArray
import numpy as np
import cvxpy
from cvxpy.expressions.expression import Expression as CVXPY_Expr

from ncpol3sdpa.sdp_repr import ProblemSDP


def cvxpy_dot_prod(c: NDArray[np.float64], x: CVXPY_Expr) -> CVXPY_Expr:
    rt = cvxpy.sum(cvxpy.multiply(c, x))
    assert isinstance(rt, CVXPY_Expr)
    return rt


class Sos:
    """Class to represent the SOS problem"""

    @classmethod
    def dual_constraints_cvxpy(self, problem: ProblemSDP) -> List[Any]:
        """Solve the SDP problem with cvxpy"""

        sdp_vars: List[cvxpy.Variable] = [
            cvxpy.Variable((size, size), PSD=True) for size in problem.variable_sizes
        ]

        # Moment matrix structure
        G = sdp_vars[problem.MOMENT_MATRIX_VAR_NUM]
        constraints: List[cvxpy.Constraint] = [G[0, 0] == 1]

        for eq_class in problem.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            (i, j) = eq_class.pop()
            for x, y in eq_class:
                constraints.append(G[i, j] == G[x, y])

        # Constraints
        for constraint in problem.constraints:
            expression: cvxpy.Expression = cvxpy.Constant(0)
            for var_num, matrix in constraint.constraints:
                expression += cvxpy_dot_prod(matrix, sdp_vars[var_num])  # type: ignore
            constraints.append(expression == 0)

        # Objective function
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))  # type: ignore

        cvxpy.Problem(objective, constraints)

        # Returns the values of the dual problem for each constraint.

        dual_problem = []
        for constraint in constraints:  # type: ignore
            dual_problem.append(constraint.dual_value)  # type: ignore

        return dual_problem


# def from_dual_constraints_to_sos(self, problem: ProblemSDP):

"""

Il faudrait typer les fonctions:

List[cvxpy.Expression]

src/ncpol3sdpa/sos.py:40: error: Incompatible types in assignment (expression has type "Expression", variable has type "int")  [assignment]
src/ncpol3sdpa/sos.py:41: error: Argument 1 to "append" of "list" has incompatible type "bool"; expected "Equality"  [arg-type]
src/ncpol3sdpa/sos.py:46: error: Argument 2 to "Problem" has incompatible type "list[Equality]"; expected "list[Constraint] | None"  [arg-type]
src/ncpol3sdpa/sos.py:46: note: "List" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
src/ncpol3sdpa/sos.py:46: note: Consider using "Sequence" instead, which is covariant
src/ncpol3sdpa/sos.py:51: error: Incompatible types in assignment (expression has type "Equality", variable has type "EqConstraint")  [assignment]
src/ncpol3sdpa/sos.py:52: error: "EqConstraint" has no attribute "dual_value"  [attr-defined]
"""
