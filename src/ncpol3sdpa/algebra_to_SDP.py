from typing import List, Tuple

import sympy
import numpy as np
from numpy.typing import NDArray

from ncpol3sdpa.resolution import AlgebraSDP
from ncpol3sdpa.sdp_repr import ProblemSDP, EqConstraint, MomentMatrixSDP


def polynomial_to_matrix(
    algebra: AlgebraSDP, poly: sympy.Expr
) -> NDArray[np.float64] | NDArray[np.complex64]:
    """Returns a symmetric A matrix such that poly = Tr(A.T @ G) where G is the moment matrix. In other
    words express poly as a linear combination of the coefficients of G.
    Requires that all monomials of poly exist within the moment matrix:
        poly.free_vars included in algebra.moment_matrix free_vars
        and deg(poly) <= 2*algebra.relaxation_order"""
    moment_matrix_size = len(algebra.moment_matrix)

    a_0: NDArray[np.float64] | NDArray[np.complex64] = np.zeros(
        shape=(moment_matrix_size, moment_matrix_size), dtype=algebra.DTYPE
    )

    print("a", algebra.monomial_to_positions.keys())
    print("b", sympy.expand(poly).as_coefficients_dict().items())

    for monomial, coef in sympy.expand(poly).as_coefficients_dict().items():
        if sympy.I in coef.atoms():  # type: ignore
            coef /= sympy.I
            coef = float(coef)
            coef *= 1j  # type: ignore
        if sympy.I in monomial.atoms():  # type: ignore
            monomial /= sympy.I
            coef = float(coef)
            coef *= 1j  # type: ignore
        assert monomial in algebra.monomial_to_positions.keys()
        assert 0 < len(algebra.monomial_to_positions[monomial])

        # The 0 is arbitrary (?) could be any other element of the list.
        # TODO/Idea What happens if we chose other than 0? at random?
        monomial_x, monomial_y = algebra.monomial_to_positions[monomial][0]

        if algebra.is_real:
            # The matrices must be symmetric
            a_0[monomial_x][monomial_y] += 0.5 * coef
            a_0[monomial_y][monomial_x] += 0.5 * coef
        else:
            a_0[monomial_x][monomial_y] += coef

    return a_0


def algebra_to_SDP_add_equality_constraint(
    problem: ProblemSDP, algebra: AlgebraSDP, eq_constraint: sympy.Expr
) -> None:
    implied_constraints = algebra.expand_eq_constraint(eq_constraint)
    for implied_constraint in implied_constraints:
        implied_constraint = algebra.substitution_rules.apply_to_polynomial(
            implied_constraint
        )

        # constraint matrix
        a_0 = polynomial_to_matrix(algebra, implied_constraint)

        constraint = EqConstraint([(problem.MOMENT_MATRIX_VAR_NUM, a_0)])
        problem.constraints.append(constraint)


def algebra_to_SDP_add_inequality_constraint(
    problem: ProblemSDP,
    algebra: AlgebraSDP,
    constraint_moment_matrix: List[List[sympy.Expr]],
) -> None:
    """Adds the translation of an inequality constraint"""
    constraint_matrix_size = len(constraint_moment_matrix)

    new_var = len(problem.variable_sizes)
    problem.variable_sizes.append(constraint_matrix_size)

    for i, row in enumerate(constraint_moment_matrix):
        for j, poly in enumerate(row):
            a_k = np.zeros(shape=(constraint_matrix_size, constraint_matrix_size))
            a_k[i][j] -= 0.5
            a_k[j][i] -= 0.5

            a_0 = polynomial_to_matrix(algebra, poly)
            constraint = EqConstraint(
                [(problem.MOMENT_MATRIX_VAR_NUM, a_0), (new_var, a_k)]
            )
            problem.constraints.append(constraint)


def algebra_to_SDP(algebra: AlgebraSDP) -> ProblemSDP:
    """Convert the algebraic representation to the numeric SDP representation"""

    moment_matrix_size = len(algebra.moment_matrix)

    # Convert objective
    objective = polynomial_to_matrix(algebra, algebra.objective)

    # Moment matrix
    equiv_classes: List[List[Tuple[int, int]]] = list(
        algebra.monomial_to_positions.values()
    )

    moment_matrix_repr = MomentMatrixSDP(moment_matrix_size, equiv_classes)

    result_SDP = ProblemSDP(moment_matrix_repr, objective)

    # Translate Equality constraints

    for eq_constraint in algebra.equality_constraints:
        algebra_to_SDP_add_equality_constraint(result_SDP, algebra, eq_constraint)

    # Translate Inequality constrains

    for constraint_matrix in algebra.constraint_moment_matrices:
        algebra_to_SDP_add_inequality_constraint(result_SDP, algebra, constraint_matrix)

    return result_SDP
