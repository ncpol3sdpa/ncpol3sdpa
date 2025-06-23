from typing import List

from scipy.sparse import lil_matrix

import cvxpy

from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver


def cvxpy_dot_prod(c: lil_matrix, x: "cvxpy.Expression") -> "cvxpy.Expression":
    expr = cvxpy.Constant(0)
    for i, row in enumerate(c.rows):
        for idx, j in enumerate(row):
            val = c.data[i][idx]
            expr += val * x[i, j]
    return expr


class CvxpySolver(Solver):
    @classmethod
    def solve(self, problem: ProblemSDP) -> float:
        """Solve the SDP problem with cvxpy"""
        # Variables
        sdp_vars = [
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
                expression += cvxpy_dot_prod(matrix, sdp_vars[var_num])
            constraints.append(cvxpy.Constant(0) == expression)

        for constraint in problem.inequality_scalar_constraints:  # type: ignore
            var_num, mat = constraint.constraints  # type: ignore
            expression: cvxpy.Expression = cvxpy_dot_prod(  # type: ignore
                mat,  # type: ignore
                sdp_vars[var_num],
            )
            constraints.append(expression >= cvxpy.Constant(0))

        # tr(A.T x G)
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))

        prob = cvxpy.Problem(objective, constraints)
        # Returns the optimal value.
        prob.solve()
        assert isinstance(prob.value, float)
        return prob.value
