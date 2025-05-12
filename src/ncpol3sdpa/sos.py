from typing import List, Tuple

# from numpy.typing import NDArray
# import numpy as np
import sympy
import numpy
from numpy.linalg import cholesky
from numpy.typing import NDArray
from ncpol3sdpa.sdp_solution import Solution_SDP
import ncpol3sdpa.algebra as algebra
# from ncpol3sdpa.problem import AvailableSolvers
# from ncpol3sdpa.problem import Problem


class Sos:
    """Class to represent the SOS problem"""

    def compute_sos_decomposition(
        self, problem_algebra: algebra.AlgebraSDP, solution: Solution_SDP
    ) -> Tuple[float, List[sympy.Expr], List[List[sympy.Expr]]]:
        """Computes an SOS decomposition of (objective polynomial - lambda) using of the solution to the
        dual SDP.

        returns: (lambda, SOS, [SOS_i | i in range(len(algebra.constraints))])
        requires: solution is a solution of the SDP relaxation
        ensures: lambda - problem_algebra.objective_polynomial = SOS + Sum of(SOS_i*g_i)
        """

        A = solution.dual_variables[0]
        B = solution.dual_variables[1:]

        def obtentionSOS(
            w: List[sympy.Expr], A: NDArray[numpy.float64]
        ) -> List[sympy.Expr]:
            P = cholesky(A)
            Pw: List[sympy.Expr] = [sympy.S.Zero for _ in range(len(P))]
            for i in range(len(P)):
                for j in range(len(P)):
                    Pw[i] += P[i][j] * w[j]

            return Pw

        w = problem_algebra.monomials  # list of monomials used in the polynom

        SOS = obtentionSOS(w, A)

        SOSi = []
        for i in range(1, len(solution.dual_variables)):
            SOSi.append(obtentionSOS(w, B[i]))

        return (solution.dual_objective_value, SOS, SOSi)
