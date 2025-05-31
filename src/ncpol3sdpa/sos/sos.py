from typing import List

import sympy
import numpy
from numpy.typing import NDArray
from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.resolution import AlgebraSDP


def sympy_sum(terms: List[sympy.Expr]) -> sympy.Expr:
    res: sympy.Expr = sympy.sympify(0)
    for term in terms:
        res += term
    return res


def semidefinite_PTP_decomp(A: NDArray[numpy.float64]) -> NDArray[numpy.float64]:
    """Returns $P$ such that $A = P^T P$ .

    We could not use the standard Cholesky decomposition of numpy, because it does not like positive
    semidefinite matrices(it only works with positive definite ones).
    """
    eigenvalues, eigenvectors = numpy.linalg.eigh(A)
    # Clip small negative values (numerical errors)
    eigvals_clipped = numpy.clip(eigenvalues, 0, None)
    sqrt_eigvals = numpy.sqrt(eigvals_clipped)

    P = eigenvectors @ numpy.diag(sqrt_eigvals)
    return P.T  # type: ignore


class SumOfSquares:
    """Data structure representing a sum of squares polynomials"""

    def __init__(self, squares: List[sympy.Expr], middle_term: sympy.Expr) -> None:
        """The polynomial represented is the sum of the squares of the elements of `squares`"""
        self.squares = squares
        self.middle_term = middle_term

    def to_expression(self) -> sympy.Expr:
        return sympy_sum([self.middle_term * term**2 for term in self.squares])


class SosDecomposition:
    """Class to represent the SOS problem"""

    def __init__(
        self, dual_objective: float, SOS: SumOfSquares, SOS_i: List[SumOfSquares]
    ) -> None:
        self.dual_objective = dual_objective
        self.SOS = SOS
        self.SOS_i = SOS_i

    def reconstructed_objective(self) -> sympy.Expr:
        """Calculates the objective polynomial from the SOS formula
        See equation (34) form "Semidefinite programming relaxations for quantum correlations" """
        s_lambda: sympy.Expr = sympy.sympify(self.dual_objective)
        return sympy_sum(
            [s_lambda, -self.SOS.to_expression()]
            + [-sos.to_expression() for sos in self.SOS_i]
        )

    def objective_error(self, problem_algebra: AlgebraSDP) -> float:
        """Returns the maximum difference in coefficients of f - f_reconstructed,
        where f is the objective polynomial, and f_reconstructed is the reconstructed
        objective, see the above function.

        Ideally, this should be zero. In practice it is non zero due to numerical precision."""
        difference: sympy.Expr = sympy.expand(
            problem_algebra.objective - self.reconstructed_objective()
        )
        epsilon = 0.0
        for v in difference.as_coefficients_dict().values():
            epsilon = max(epsilon, abs(v))

        return epsilon


def compute_sos_decomposition(
    problem_algebra: AlgebraSDP, solution: Solution_SDP
) -> SosDecomposition:
    """Computes an SOS decomposition of (objective polynomial - lambda) using of the solution to the
    dual SDP.

    returns: (lambda, SOS, [SOS_i | i in range(len(algebra.constraints))])
    requires: solution is a solution of the SDP relaxation
    ensures: lambda - problem_algebra.objective_polynomial = SOS + Sum of(SOS_i*g_i)
    """

    A = solution.dual_PSD_variables[0]
    B = solution.dual_PSD_variables[1:]

    def calculate_SOS(
        w: List[sympy.Expr], A: NDArray[numpy.float64], middle: sympy.Expr
    ) -> SumOfSquares:
        """
        w.T A w is a polynomial, and if A is positive-semidefinite, then
        this function will calculate the SOS of this polynomial using the
        Cholesky decomposition
        Arguments:
        w is the vector of monomials from AlgebraSDP
        A is the numerical result of the dual variable from the SDP
        """
        P = semidefinite_PTP_decomp(A)
        Pw: List[sympy.Expr] = [sympy.S.Zero for _ in range(len(P))]
        for i in range(len(P)):
            for j in range(len(P)):
                Pw[i] += P[i][j] * w[j]
        return SumOfSquares(Pw, middle)

    w = problem_algebra.monomials  # list of monomials used in the polynomial

    SOS = calculate_SOS(w, A, sympy.S.One)

    SOSi = [
        calculate_SOS(w, B[i], problem_algebra.psd_polynomials_gi[i])
        for i in range(len(B))
    ]

    return SosDecomposition(solution.dual_objective_value, SOS, SOSi)
