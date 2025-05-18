from typing import List

from numpy.typing import NDArray
import numpy as np

import cvxpy
from cvxpy.expressions.expression import Expression as CVXPY_Expr

from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver


def cvxpy_dot_prod(c: NDArray[np.float64], x: CVXPY_Expr) -> CVXPY_Expr:
    rt = cvxpy.sum(cvxpy.multiply(c, x))
    assert isinstance(rt, CVXPY_Expr)
    return rt


class CvxpySolver(Solver):
    @classmethod
    def solve(self, problem: ProblemSDP) -> Solution_SDP:
        """Solve the SDP problem with cvxpy"""
        # Variables
        sdp_vars = [
            cvxpy.Variable((size, size), symmetric=True)
            for size in problem.variable_sizes
        ]
        psd_constraints: List[cvxpy.Constraint] = [x >> 0 for x in sdp_vars]
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
            constraints.append(cvxpy.Constant(0) == expression)

        # tr(A.T x G)
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))  # type: ignore

        prob = cvxpy.Problem(objective, constraints + psd_constraints)
        # Returns the optimal value.
        prob.solve()
        assert isinstance(prob.value, float)

        return Solution_SDP(
            prob.value,
            [x.value for x in sdp_vars],  # type: ignore
            constraints[0].dual_value,
            [c.dual_value for c in psd_constraints],
        )
