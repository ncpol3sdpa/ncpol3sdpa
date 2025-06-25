from typing import List, Dict, Any

from scipy.sparse import lil_matrix

from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver




class CvxpySolver(Solver):
    """Solver for SDP problems using CVXPY."""

    def is_available(self) -> bool:
        """Check if cvxpy is available"""
        try:
            import cvxpy  # noqa: F401
            return True
        except ImportError:
            return False

    def solve(self, problem: ProblemSDP, **config: Dict[str, Any]) -> float:
        """Solve the SDP problem with cvxpy"""

        import cvxpy

        sdp_vars = [
            cvxpy.Variable((size, size), PSD=True) 
            for size in problem.variable_sizes
        ]

        # Moment matrix structure
        G = sdp_vars[problem.MOMENT_MATRIX_VAR_NUM]
        constraints: List[cvxpy.Constraint] = [G[0, 0] == 1]
        for eq_class in problem.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            (i, j) = eq_class.pop()
            for x, y in eq_class:
                constraints.append(G[i, j] == G[x, y])

        # Equality Constraints
        for constraint in problem.constraints:
            expression: cvxpy.Expression = cvxpy.Constant(0)
            for var_num, matrix in constraint.constraints:
                expression += CvxpySolver._cvxpy_dot_prod(matrix, sdp_vars[var_num])
            constraints.append(cvxpy.Constant(0) == expression)

        # Inequality Constraints
        for ineq_constraint in problem.inequality_scalar_constraints:
            var_num, matrix = ineq_constraint.constraints
            expression = CvxpySolver._cvxpy_dot_prod(
                matrix,
                sdp_vars[var_num],
            )
            constraints.append(expression >= cvxpy.Constant(0))

        objective = cvxpy.Maximize(CvxpySolver._cvxpy_dot_prod(problem.objective, G))

        prob = cvxpy.Problem(objective, constraints)

        prob.solve(verbose=config.get("verbose", False))
        assert isinstance(prob.value, float)
        return prob.value


    @classmethod
    def _cvxpy_dot_prod(cls, c: lil_matrix, x: Any) -> Any:
        """Compute the dot product of a sparse matrix and a cvxpy expression."""

        import cvxpy

        expr = cvxpy.Constant(0)
        for i, row in enumerate(c.rows):
            for idx, j in enumerate(row):
                val = c.data[i][idx]
                expr += val * x[i, j]
        return expr