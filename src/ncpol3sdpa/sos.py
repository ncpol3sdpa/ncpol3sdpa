from typing import List, Tuple

# from numpy.typing import NDArray
# import numpy as np
import sympy
from ncpol3sdpa.sdp_solution import Solution_SDP
import ncpol3sdpa.algebra as algebra


class Sos:
    """Class to represent the SOS problem"""

    def compute_sos_decomposition(
        self, problem_algebra: algebra.AlgebraSDP, solution: Solution_SDP
    ) -> Tuple[float, sympy.Expr, List[sympy.Expr]]:
        """Computes an SOS decomposition of (objective polynomial - lambda) using of the solution to the
        dual SDP.

        returns: (lambda, SOS, [SOS_i | i in range(len(algebra.constraints))])
        requires: solution is a solution of the SPD relaxation
        ensures: lambda - problem_algebra.objective_polynomial = SOS + Sum of(SOS_i*g_i)
        """
        # TODO
        return NotImplementedError  # type: ignore
