from typing import Tuple, List
from numpy.typing import NDArray
import numpy as np
import cvxpy
from cvxpy.expressions.expression import Expression as CVXPY_Expr
import mosek
import ncpol3sdpa.sdp_repr as sdp_repr
import warnings


#def solve_dual(P :ProblemSDP):


def cvxpy_dot_prod(c: Any, x: Any) -> Any:
    # TODO: Fix the typing of this.
    # Should be c: NDArray, x : cvxpy PSD variable, result : cvxpy expression(?)
    return cvxpy.sum(cvxpy.multiply(c, x))


class Sos:   

    def dual_constraints_cvxpy(self, problem: sdp_repr.ProblemSDP) -> list:
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

        # tr(A.T x G)
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))

        prob = cvxpy.Problem(objective, constraints)
        
        # Returns the values of the dual problem for each constraint.
        
        dual_problem = []
        for constraint in constraints:
              dual_problem.append(constraint.dual_value)
        
        return dual_problem
    

    def from_dual_constraints_to_sos(self, problem: sdp_repr.ProblemSDP)


