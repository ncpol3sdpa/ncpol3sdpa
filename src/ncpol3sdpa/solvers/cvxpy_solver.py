from typing import List
import warnings

from scipy.sparse import lil_matrix
import numpy as np

import cvxpy

from ncpol3sdpa.sdp_solution import Solution_SDP
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
    def solve(self, problem: ProblemSDP) -> Solution_SDP[np.float64] | None:
        """Solve the SDP problem with cvxpy"""
        # Variables
        sdp_vars = [
            cvxpy.Variable((size, size), symmetric=True)
            for size in problem.variable_sizes
        ]
        psd_constraints: List[cvxpy.Constraint] = [x >> 0 for x in sdp_vars]
        # Moment matrix structure
        G = sdp_vars[problem.MOMENT_MATRIX_VAR_NUM]
        moment_structure_constraints: List[cvxpy.Constraint] = [G[0, 0] == 1]
        for eq_class in problem.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            (i, j) = eq_class.pop()
            for x, y in eq_class:
                moment_structure_constraints.append(G[i, j] == G[x, y])

        # Constraints
        eq_constraints: List[cvxpy.Constraint] = []
        for constraint in problem.constraints:
            expression: cvxpy.Expression = cvxpy.Constant(0)
            for var_num, matrix in constraint.constraints:
                expression += cvxpy_dot_prod(matrix, sdp_vars[var_num])
            eq_constraints.append(cvxpy.Constant(0) == expression)

        ineq_constraints: List[cvxpy.Constraint] = []
        for constraint2 in problem.inequality_scalar_constraints:
            var_num, mat = constraint2.constraints
            expression2: cvxpy.Expression = cvxpy_dot_prod(
                mat,
                sdp_vars[var_num],
            )
            ineq_constraints.append(expression2 >= cvxpy.Constant(0))

        # tr(A.T x G)
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))

        prob = cvxpy.Problem(
            objective, moment_structure_constraints + psd_constraints + eq_constraints
        )
        # Returns the optimal value.
        prob.solve()
        assert isinstance(prob.value, float)

        if prob.status == "optimal" or prob.status == "optimal_inaccurate":
            if prob.status == "optimal_inaccurate":
                warnings.warn(
                    f'CVXPY does not guarantee the accuracy of the solution: "{prob.status}"'
                )

            return Solution_SDP(
                primal_objective_value=prob.value,
                primal_PSD_variables=[x.value for x in sdp_vars],  # type: ignore
                dual_objective_value=moment_structure_constraints[0].dual_value,
                dual_PSD_variables=[c.dual_value for c in psd_constraints],
                dual_eqC_variables=np.array([c.dual_value for c in eq_constraints]),
                dual_ineqC_variables=np.array([c.dual_value for c in ineq_constraints]),
            )
        else:
            warnings.warn(
                f'CVXPY could not solve the problem, solution status is "{prob.status}"'
            )
            return None
