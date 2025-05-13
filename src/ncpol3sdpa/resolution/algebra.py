from __future__ import annotations
from typing import List, Tuple, Dict

import sympy as sp
import math

from .rules import Rule
from .monomial import generate_monomials
from .constraints import Constraint
from .utils import (
    Matrix,
    needed_monomials,
    degree_of_polynomial,
    create_constraint_matrix,
    create_moment_matrix,
)


class AlgebraSDP:
    def __init__(
        self,
        needed_variables: List[sp.Symbol],
        objective: sp.Expr,
        relaxation_order: int,
        substitution_rules: Dict[sp.Expr, sp.Expr],
        is_commutative: bool = True,
        is_real: bool = True,
    ) -> None:
        """Construct the symbolic Moment Matrices and soundings data structures. Works for the commutative case"""
        self.relaxation_order: int = relaxation_order
        self.substitution_rules: Dict[sp.Expr, sp.Expr] = substitution_rules
        self.is_commutative = is_commutative
        self.is_real = is_real
        self.monomials: List[sp.Expr] = needed_monomials(
            generate_monomials(
                needed_variables, relaxation_order, is_commutative, is_real
            ),
            substitution_rules,
        )
        self.objective: sp.Expr = Rule.apply_to_polynomial(
            sp.expand(objective),
            substitution_rules,
        )

        # In the commutative case, the moment matrix is symmetric
        self.moment_matrix = create_moment_matrix(
            self.monomials, self.substitution_rules, self.is_commutative, self.is_real
        )
        matrix_size: int = len(self.moment_matrix)

        # equivalence classes of equal coefficients
        self.monomial_to_positions: Dict[sp.Expr, List[Tuple[int, int]]] = {}
        for i in range(matrix_size):
            for j in range(i + 1):
                monomial = self.moment_matrix[i][j]
                if monomial in self.monomial_to_positions.keys():
                    self.monomial_to_positions[monomial].append((i, j))
                else:
                    self.monomial_to_positions[monomial] = [(i, j)]
                if not is_real and i != j:
                    monomial = self.moment_matrix[i][j].conjugate()  # type: ignore
                    if monomial in self.monomial_to_positions.keys():
                        self.monomial_to_positions[monomial].append((j, i))
                    else:
                        self.monomial_to_positions[monomial] = [(j, i)]

        # This is the positive semi-definite matrices in the sdp
        self.constraint_moment_matrices: List[Matrix] = []
        # List of polynomials that equal 0
        self.equality_constraints: List[sp.Expr] = []

    def add_constraint(self, constraint: Constraint) -> None:
        """Add a constraint to the algebra

        Save the constraint if it is an equality constraint,
        otherwise update the moment matrix for the inequality constraint"""
        if constraint.is_equality_constraint:
            self.equality_constraints.append(constraint.polynomial)
        else:
            # inequality constraint
            # p.10 of Semidefinite programming relaxations for quantum correlations

            if self.is_real:
                k_i = math.floor(
                    self.relaxation_order
                    - degree_of_polynomial(constraint.polynomial) / 2
                )
            else:
                k_i = self.relaxation_order - degree_of_polynomial(
                    constraint.polynomial
                )
            assert k_i >= 0, (
                "Insufficient relaxation order to capture the constraint {constraint.polynomial}"
            )

            # TODO This is redundant work, does this matter?
            constraint_monomials = needed_monomials(
                generate_monomials(
                    self.objective.free_symbols,  # type: ignore
                    k_i,
                    self.is_commutative,
                    self.is_real,
                ),
                self.substitution_rules,
            )

            self.constraint_moment_matrices.append(
                create_constraint_matrix(
                    constraint_monomials,
                    constraint.polynomial,
                    self.substitution_rules,
                    self.is_commutative,
                    self.is_real,
                )
            )

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for constraint in constraints:
            self.add_constraint(constraint)

    def expand_eq_constraint(self, constraint: sp.Expr) -> List[sp.Expr]:
        """
        Generate a list of polynomials {p = m * constraint | m : monomial & degre(p) <= 2*k }
        where k is the relaxation order. 2k are monomials that "fit inside" the moment matrix.

        Used for equality constraints.
        """

        # Map and filter are lazy
        # so intermediate lists are not created
        ruled_monomials: map[sp.Expr] = map(
            lambda monomial: Rule.apply_to_monomial(
                monomial * constraint, self.substitution_rules
            ),
            self.monomials,
        )
        ruled_filtered_monomials: filter[sp.Expr] = filter(
            lambda monomial: degree_of_polynomial(monomial)
            <= (2 * self.relaxation_order if self.is_real else self.relaxation_order),
            ruled_monomials,
        )
        return list(ruled_filtered_monomials)

    def __str__(self) -> str:
        """Return a string representation of the algebra for debugging."""

        return f"""Algebra:
    relaxation_order: {self.relaxation_order}
    monomials:
        {self.monomials}
    moment_matrix:
        {self.moment_matrix}
    substitution_rules:
        {self.substitution_rules}
    monomial_to_positions:
        {self.monomial_to_positions}
    equality_constraints:
        {self.equality_constraints}
    constraint_moment_matrices:
        {self.constraint_moment_matrices}"""

    def __repr__(self) -> str:
        """Return a string representation of the algebra for debugging."""
        return self.__str__()
