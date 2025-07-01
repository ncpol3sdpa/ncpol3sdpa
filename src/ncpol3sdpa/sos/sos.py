from typing import List, NamedTuple, Any, TypeVar
from collections.abc import Callable

import sympy
import numpy
from numpy.typing import NDArray
from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.resolution import AlgebraSDP
from ncpol3sdpa.resolution.utils import sympy_sum
from .solution_real_to_complex import solution_real_to_complex


class SOS_TraceConstraintTerm(NamedTuple):
    """Represents a trace inequality equality constraint SOS term"""

    coef_eta: float
    """The positive scalar coefficient that multiplies the term"""

    poly_h: sympy.Expr
    """Polynomial form the trace constraint :math:`\\mathrm{tr}(\\rho h_i) \\geqslant 0`"""

    def to_expression(self) -> sympy.Expr:
        """Convert this to a sympy expression"""
        return self.coef_eta * self.poly_h  # type: ignore


class SOS_EqConstraintFactor(NamedTuple):
    """Represents a part of an equality constraint SOS term"""

    coef_nu: complex
    """The scalar coefficient that multiplies the term. possibly imaginary"""

    l_monomial: sympy.Expr
    """Left multiplier monomial"""

    r_monomial: sympy.Expr
    """Right multiplier monomial"""


class SOS_EqConstraintTerms(NamedTuple):
    """Represents equality constraint SOS terms"""

    poly_f: sympy.Expr
    """The zero polynomial"""

    multiplier_monomials: List[SOS_EqConstraintFactor]
    """Factors that multiply the polynomial"""

    adjoint_func: Callable[[sympy.Expr], sympy.Expr]
    """Function that maps a monomial to it's adjoint (in particular in the complex case)"""

    def to_expression(self) -> sympy.Expr:
        """Convert this to a sympy expression"""
        # fmt: off
        terms: map[sympy.Expr] = map(
            lambda multiplier:
            0.5 * multiplier.coef_nu
                * self.adjoint_func(multiplier.l_monomial)
                * self.poly_f
                * multiplier.r_monomial
            +
            0.5 * numpy.conjugate(multiplier.coef_nu)
                * self.adjoint_func(multiplier.r_monomial)
                * self.adjoint_func(self.poly_f)
                * multiplier.l_monomial,
            self.multiplier_monomials,
        )
        # fmt: on
        return sympy_sum(terms)


class SumOfSquaresTerm(NamedTuple):
    """Data structure representing a sum of squares polynomials.
    The represented expression is :math:`\\sum_i \\texttt{squares[i]}^\\dagger \\times \\texttt{middle_term[i]} \\times \\texttt{squares[i]}`"""

    squares: List[sympy.Expr]
    middle_term: sympy.Expr

    adjoint_func: Callable[[sympy.Expr], sympy.Expr]
    """Function that maps a monomial to it's adjoint (in particular in the complex case)"""

    def to_expression(self) -> sympy.Expr:
        """Convert this to a sympy expression"""
        return sympy_sum(
            [self.adjoint_func(term) * self.middle_term * term for term in self.squares]
        )


class SosDecomposition(NamedTuple):
    """Class to represent a SOS decomposition. See :docs:`sos` for more detail"""

    original_objective: sympy.Expr
    """The objective polynomial :math:`c` from the optimisation problem"""

    dual_objective: float
    """This is an upper bound :math:`\\lambda` on the objective polynomial, obtained as the optimal value of the dual SDP relaxation"""

    SOS: SumOfSquaresTerm
    """Sum of squares terms"""

    SOS_i: List[SumOfSquaresTerm]
    """Quasi SOS terms form PSD inequality constraints"""

    eq_terms: List[SOS_EqConstraintTerms]  # $\\nu_i * f_i
    """Terms from the equality constraints"""

    trace_terms: List[SOS_TraceConstraintTerm]  # \\eta_i * h_i
    """Terms from the inequality constrains :math:`\\eta_i * h_i`"""

    def reconstructed_objective(self) -> sympy.Expr:
        """
        Calculates the objective polynomial from the SOS formula

        See equation :math:`(2)` in :doc:`sos`
        """

        s_lambda: sympy.Expr = sympy.sympify(self.dual_objective)
        return sympy_sum(
            [s_lambda, -self.SOS.to_expression()]
            + [-sos.to_expression() for sos in self.SOS_i]
            + [-eq_c.to_expression() for eq_c in self.eq_terms]
            + [-trace_c.to_expression() for trace_c in self.trace_terms]
        )

    def objective_error(self) -> float:
        """Returns the maximum difference in coefficients of :math:`c - c_r`,
        where :math:`c` is the objective polynomial, and :math:`c_r` is
        the reconstructed objective, see the :func:`SosDecomposition.reconstructed_objective` function.

        Ideally, this should be zero. In practice it is non zero due to numerical precision.

        .. warning::

            This function takes a lot of time to compute for large problems!
        """
        difference: sympy.Expr = sympy.expand(
            self.original_objective - self.reconstructed_objective()
        )
        epsilon = 0.0
        for v in difference.as_coefficients_dict().values():
            epsilon = max(epsilon, abs(v))

        return epsilon


def compute_equality_constraints(
    problem_algebra: AlgebraSDP, solution: Solution_SDP[Any]
) -> List[SOS_EqConstraintTerms]:
    """Obtain equality constraint data from the solution"""

    # `solution.dual_eqC_variables` contains the constraints in order
    # for each equality contraint is f_i = 0 has a group of sub-constraints :
    #   {m* f_i *n = 0 | m,n monomials}
    # `solution.dual_eqC_variables` has  the dual variables of sub constraints in the following order:
    #  * first, the sub-constraints of f_0, with the order indicated by constraint.monomial_multiples
    #  * then, the sub-constraints of f_1,
    #  * etc...

    y_idx = 0
    res = []
    for constraint in problem_algebra.equality_constraints:
        multiplier_monomials: List[SOS_EqConstraintFactor] = []
        for monomials in constraint.monomial_multiples:
            a, b = monomials
            nu_i_RE = solution.dual_eqC_variables[y_idx]
            y_idx += 1
            multiplier_monomials.append(
                SOS_EqConstraintFactor(coef_nu=nu_i_RE, l_monomial=a, r_monomial=b)
            )
            if not problem_algebra.is_real:
                nu_i_IM = solution.dual_eqC_variables[y_idx]
                y_idx += 1
                multiplier_monomials.append(
                    SOS_EqConstraintFactor(
                        coef_nu=-1j * nu_i_IM, l_monomial=a, r_monomial=b
                    )
                )

        res.append(
            SOS_EqConstraintTerms(
                poly_f=constraint.zero_polynomials[0],
                multiplier_monomials=multiplier_monomials,
                adjoint_func=problem_algebra.get_adjoint,
            )
        )

    return res


def compute_trace_constraints(
    problem_algebra: AlgebraSDP, solution: Solution_SDP[Any]
) -> List[SOS_TraceConstraintTerm]:
    """Obtain trace constraint data from the solution"""

    res: List[SOS_TraceConstraintTerm] = []
    for i in range(len(problem_algebra.local_inequality_constraints)):
        poly = problem_algebra.local_inequality_constraints[i]
        eta_i = solution.dual_ineqC_variables[i]
        res.append(SOS_TraceConstraintTerm(poly_h=poly, coef_eta=eta_i))

    return res


T0 = TypeVar("T0", numpy.float64, numpy.complex64)


def compute_sos_decomposition(
    problem_algebra: AlgebraSDP, solution: Solution_SDP[numpy.float64]
) -> SosDecomposition:
    """Computes an SOS decomposition of (objective polynomial - lambda) using of the solution to the
    dual SDP.

    returns: (lambda, SOS, [SOS_i | i in range(len(algebra.constraints))])
    requires: solution is a solution of the SDP relaxation
    ensures: lambda - problem_algebra.objective_polynomial = SOS + Sum of(SOS_i*g_i)

    :meta private:
    """

    true_solution = (
        solution if problem_algebra.is_real else solution_real_to_complex(solution)
    )
    A = true_solution.dual_PSD_variables[0]
    B = true_solution.dual_PSD_variables[1:]

    def calculate_SOS(
        w: List[sympy.Expr], A: NDArray[T0], middle: sympy.Expr
    ) -> SumOfSquaresTerm:
        """
        w† A w is a polynomial, and if A is positive-semidefinite, then
        this function will calculate the SOS of this polynomial using the
        eigenvalue decomposition
        Arguments:
        w is the vector of monomials from AlgebraSDP
        A is the numerical result of the dual variable from the SDP
        """
        P = semidefinite_PTP_decomp(A)
        Pw: List[sympy.Expr] = [sympy.S.Zero for _ in range(len(P))]
        for i in range(len(P)):
            for j in range(len(P)):
                Pw[i] += P[i][j] * w[j]
        return SumOfSquaresTerm(Pw, middle, adjoint_func=problem_algebra.get_adjoint)

    w = problem_algebra.monomials  # list of monomials used in the polynomial
    SOS = calculate_SOS(w, A, sympy.S.One)  # type:ignore

    SOSi = [
        calculate_SOS(w, B[i], problem_algebra.psd_polynomials_gi[i])  # type:ignore
        for i in range(len(B))
    ]

    eq_terms = compute_equality_constraints(problem_algebra, true_solution)
    trace_terms = compute_trace_constraints(problem_algebra, true_solution)

    return SosDecomposition(
        original_objective=problem_algebra.objective,
        dual_objective=true_solution.dual_objective_value,
        SOS=SOS,
        SOS_i=SOSi,
        eq_terms=eq_terms,
        trace_terms=trace_terms,
    )


T = TypeVar("T", numpy.float64, numpy.complex64)


def semidefinite_PTP_decomp(A: NDArray[T]) -> NDArray[T]:
    """If A is a hermitian matrix, returns :math:`P` such that :math:`A = P^† P` ."""

    # We could not use the standard Cholesky decomposition of numpy, because it does not like singular
    # positive semidefinite matrices(it only works with positive definite ones).

    eigenvalues, eigenvectors = numpy.linalg.eigh(A)
    # Clip small negative values (numerical errors)
    eigvals_clipped = numpy.clip(eigenvalues, 0, None)
    sqrt_eigvals = numpy.sqrt(eigvals_clipped)

    P = eigenvectors @ numpy.diag(sqrt_eigvals)
    return numpy.conj(P).T  # type: ignore
