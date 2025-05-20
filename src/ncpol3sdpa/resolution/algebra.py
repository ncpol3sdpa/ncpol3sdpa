from __future__ import annotations
from typing import List, Tuple, Dict, Callable

import sympy as sp

from .rules import Rule
from .monomial import generate_monomials
from .constraints import Constraint
from .utils import (
    Matrix,
    degree_of_polynomial,
)


def create_moment_matrix(
    monomials: List[sp.Expr],
    substitution_rules: Rule,
    is_commutative: bool = True,
    get_adjoint: Callable[[sp.Expr], sp.Expr] = lambda x: x,
) -> Matrix:
    """Creates a moment matrix with monomials, substitution rules. Defaults to the real commutative case"""
    matrix_size = len(monomials)
    return [
        [
            substitution_rules.apply_to_monomial(
                get_adjoint(monomials[j]) * monomials[i],
                is_commutative,
            )
            for j in range(i + 1)
        ]
        for i in range(matrix_size)
    ]


class AlgebraSDP:
    """Base class for all SDP algebras"""

    # Special methods

    def __init__(
        self,
        needed_variables: List[sp.Symbol],
        objective: sp.Expr,
        relaxation_order: int,
        substitution_rules: Rule,
    ) -> None:
        """
        Construct the symbolic Moment Matrices and soundings data structures.

        Works for the commutative case only.
        """

        self.relaxation_order: int = relaxation_order
        self.substitution_rules: Rule = substitution_rules
        self.monomials: List[sp.Expr] = substitution_rules.filter_monomials(
            generate_monomials(needed_variables, relaxation_order, self.is_commutative)
        )
        self.objective: sp.Expr = substitution_rules.apply_to_polynomial(
            sp.expand(objective)
        )

        # In the commutative case, the moment matrix is symmetric
        self.moment_matrix = create_moment_matrix(
            substitution_rules=self.substitution_rules,
            monomials=self.monomials,
            is_commutative=self.is_commutative,
            get_adjoint=self.get_adjoint,
        )
        matrix_size: int = len(self.moment_matrix)

        # equivalence classes of equal coefficients
        self.monomial_to_positions: Dict[sp.Expr, List[Tuple[int, int]]] = {}
        for i in range(matrix_size):
            for j in range(i + 1):
                monomial = self.moment_matrix[i][j]
                self.add_monomial_to_positions(monomial, i, j)

        # This is the positive semi-definite matrices in the sdp
        self.constraint_moment_matrices: List[Matrix] = []
        # List of polynomials that equal 0
        self.equality_constraints: List[sp.Expr] = []

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

    # Properties

    @property
    def DTYPE(self) -> type:
        """Return the type of the objects in the algebra"""
        raise NotImplementedError

    @property
    def is_real(self) -> bool:
        return False

    @property
    def is_commutative(self) -> bool:
        "Return the commutativity of self"
        raise NotImplementedError

    # Public methods

    def add_constraint(self, constraint: Constraint) -> None:
        """Add a constraint to the algebra

        Save the constraint if it is an equality constraint,
        otherwise update the moment matrix for the inequality constraint"""
        if constraint.is_equality_constraint:
            self.equality_constraints.append(constraint.polynomial)
        else:
            # inequality constraint
            # p.10 of Semidefinite programming relaxations for quantum correlations

            k_i = self.get_length_constraint_matrix(
                degree_of_polynomial(constraint.polynomial)
            )
            assert k_i >= 0, (
                "Insufficient relaxation order to capture the constraint {constraint.polynomial}"
            )

            # TODO This is redundant work, does this matter?
            constraint_monomials = self.substitution_rules.filter_monomials(
                generate_monomials(
                    self.objective.free_symbols,  # type: ignore
                    k_i,
                    self.is_commutative,
                )
            )

            self.constraint_moment_matrices.append(
                self.create_constraint_matrix(
                    constraint_monomials,
                    constraint.polynomial,
                )
            )

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for constraint in constraints:
            self.add_constraint(constraint)

    def add_monomial_to_positions(self, monomial: sp.Expr, i: int, j: int) -> None:
        """Add a monomial to the list of monomials and its position in the moment matrix"""

        if monomial in self.monomial_to_positions.keys():
            self.monomial_to_positions[monomial].append((i, j))
        else:
            self.monomial_to_positions[monomial] = [(i, j)]

    def expand_eq_constraint(self, constraint: sp.Expr) -> List[sp.Expr]:
        """
        Generate a list of polynomials {p = m * constraint | m : monomial & degre(p) <= 2*k }
        where k is the relaxation order. 2k are monomials that "fit inside" the moment matrix.

        Used for equality constraints.
        """

        # Map and filter are lazy
        # so intermediate lists are not created
        ruled_monomials: map[sp.Expr] = map(
            lambda monomial: self.substitution_rules.apply_to_monomial(
                monomial * constraint
            ),
            self.monomials,
        )
        ruled_filtered_monomials: filter[sp.Expr] = filter(
            lambda monomial: self.is_expressible_as_moment_coeff(monomial),
            ruled_monomials,
        )
        return list(ruled_filtered_monomials)

    def create_constraint_matrix(
        self, monomials: List[sp.Expr], constraint_polynomial: sp.Expr
    ) -> Matrix:
        """Create the matrix of constraints
        The constraints are of the form `constraint_polynomial >= 0`
        """

        n = len(monomials)
        return [
            [
                self.substitution_rules.apply_to_polynomial(
                    sp.expand(
                        self.get_adjoint(self.monomials[j])
                        * constraint_polynomial
                        * monomials[i]
                    ),
                    self.is_commutative,
                )
                for j in range(i + 1)
            ]
            for i in range(n)
        ]

    # Abstract methods

    def get_adjoint(self, monomial: sp.Expr) -> sp.Expr:
        """Get the adjoint of a monomial"""

        raise NotImplementedError

    def get_length_constraint_matrix(self, deg_pol: int) -> int:
        """Get the length of the constraint matrix"""
        raise NotImplementedError

    def is_expressible_as_moment_coeff(self, monomial: sp.Expr) -> bool:
        """Check if the monomial is expressible as a moment coefficient"""

        raise NotImplementedError
