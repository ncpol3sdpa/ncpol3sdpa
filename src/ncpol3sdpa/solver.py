from typing import Any #,List, Dict
import cvxpy

import ncpol3sdpa.sdp_repr as sdp_repr


def cvxpy_dot_prod(c: Any, x: Any) -> Any:
    # TODO: Fix the typing of this. 
    # Should be c: NDArray, x : cvxpy PSD variable, result : cvxpy expression(?)
    return cvxpy.sum(cvxpy.multiply(c, x))


class Solver:
    @classmethod
    def solve_cvxpy(self, problem: sdp_repr.ProblemSDP) -> float:
        """Solve the SDP problem with cvxpy"""
        # Variables
        sdp_vars = [
            cvxpy.Variable((size, size), PSD=True) for size in problem.variable_sizes
        ]

        # Moment matrix structure
        G = sdp_vars[problem.MOMENT_MATRIX_VAR_NUM]
        constraints = [G[0, 0] == 1]
        for eq_class in problem.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            (i, j) = eq_class.pop()
            for x, y in eq_class:
                constraints.append(G[i, j] == G[x, y])

        # Constraints
        for constraint in problem.constraints:
            expression = 0
            for var_num, matrix in constraint.constraints:
                expression += cvxpy_dot_prod(matrix, sdp_vars[var_num])
            constraints.append(0 == expression)

        print("SOLVER constraints:")
        print(constraints)

        # tr(A.T x G)
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))

        prob = cvxpy.Problem(objective, constraints)
        # Returns the optimal value.
        prob.solve()
        print("status:", prob.status)
        print("optimal value", prob.value)
        print("optimal var", G.value)
        return prob.value # type: ignore
