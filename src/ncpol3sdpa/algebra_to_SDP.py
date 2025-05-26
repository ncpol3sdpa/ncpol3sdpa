from typing import List, Tuple

import sympy
import numpy as np

from ncpol3sdpa.resolution import AlgebraSDP
from ncpol3sdpa.sdp_repr import ProblemSDP, EqConstraint, MomentMatrixSDP


def algebra_to_SDP_add_equality_constraint(
    problem: ProblemSDP, algebra: AlgebraSDP, eq_constraint: sympy.Expr
) -> None:
    implied_constraints = algebra.expand_eq_constraint(eq_constraint)
    for implied_constraint in implied_constraints:
        implied_constraint = algebra.substitution_rules.apply_to_polynomial(
            implied_constraint
        )

        # constraint matrix
        a_0 = algebra.polynomial_to_matrix(implied_constraint)

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

            a_0 = algebra.polynomial_to_matrix(poly)
            constraint = EqConstraint(
                [(problem.MOMENT_MATRIX_VAR_NUM, a_0), (new_var, a_k)]
            )
            problem.constraints.append(constraint)


def algebra_to_SDP(algebra: AlgebraSDP) -> ProblemSDP:
    """Convert the algebraic representation to the numeric SDP representation"""

    moment_matrix_size = len(algebra.moment_matrix)

    # Convert objective
    objective = algebra.polynomial_to_matrix(algebra.objective)

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
