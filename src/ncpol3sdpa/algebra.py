from __future__ import annotations
from typing import List, Tuple, Dict, Any
from sympy import Expr
import sympy as sp
from ncpol3sdpa.rules import apply_rule, apply_rule_to_polynomial
from ncpol3sdpa.monomial import generate_monomials
from ncpol3sdpa.constraints import Constraint
import math


def degree_of_polynomial(polynomial: Expr) -> int:
    polynomial = polynomial.expand()
    terms = polynomial.as_ordered_terms()
    res = 0
    for term in terms:
        factors = term.as_ordered_factors()
        deg = 0
        for factor in factors:
            if not factor.is_number:
                _, exp = factor.as_base_exp()
                deg += exp
        res = max(deg, res)
    return res


def needed_monomials(monomials: List[Expr], rules: Dict[Expr, Expr]) -> List[Expr]:
    """Filter the monomials according to the rules"""
    # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
    return [monomial for monomial in monomials if monomial not in rules.keys()]


def create_moment_matrix(
    monomials: List[sp.Expr],
    substitution_rules: Dict[sp.Expr, Any],
    commutative: bool = True,
) -> List[List[sp.Expr]]:
    """Create the moment matrix of the monomials"""

    matrix_size = len(monomials)
    return [
        [
            apply_rule(
                (monomials[j] if commutative else monomials[j].adjoint())
                * monomials[i],
                substitution_rules,
                commutative,
            )  # type: ignore
            for j in range(i + 1)
        ]
        for i in range(matrix_size)
    ]


def create_constraint_matrix(
    monomials: List[sp.Expr],
    constraint_polynomial: sp.Expr,
    rules: Dict[sp.Expr, Any],
    commutative: bool = True,
) -> List[List[sp.Expr]]:
    """Create the matrix of constraints
    The constraints are of the form `constraint_polynomial >= 0`
    """

    n = len(monomials)
    return [
        [
            apply_rule_to_polynomial(
                sp.expand(
                    (monomials[j] if commutative else monomials[j].adjoint())
                    * constraint_polynomial
                    * monomials[i]
                ),
                rules,
                commutative,  # type: ignore
            )
            for j in range(i + 1)
        ]
        for i in range(n)
    ]


def generate_needed_symbols(polynomials: List[sp.Expr]) -> List[sp.Symbol]:
    total: sp.Expr = sp.S.One
    for p in polynomials:
        total += p

    return list(total.free_symbols)  # type: ignore


class AlgebraSDP:
    def __init__(
        self,
        needed_variables: List[sp.Symbol],
        objective: sp.Expr,
        relaxation_order: int,
        substitution_rules: Dict[sp.Expr, sp.Expr],
        commutative: bool = True,
    ) -> None:
        """Construct the symbolic Moment Matrices and soundings data structures. Works for the commutative case"""
        self.relaxation_order: int = relaxation_order
        self.substitution_rules: Dict[sp.Expr, sp.Expr] = substitution_rules
        self.commutative = commutative
        self.monomials: List[sp.Expr] = needed_monomials(
            generate_monomials(needed_variables, relaxation_order, commutative),
            substitution_rules,
        )
        self.objective: sp.Expr = apply_rule_to_polynomial(
            sp.expand(objective),
            substitution_rules,
        )

        # In the commutative case, the moment matrix is symmetric
        self.moment_matrix = create_moment_matrix(
            self.monomials, self.substitution_rules, self.commutative
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

        # This is the positive semi-definite matrices in the sdp
        #                                       v TODO Should this be a new type? discuss
        self.constraint_moment_matrices: List[List[List[sp.Expr]]] = []
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

            k_i = math.floor(
                self.relaxation_order - degree_of_polynomial(constraint.polynomial) / 2
            )
            assert k_i >= 0, (
                "Insufficient relaxation order to capture the constraint {constraint.polynomial}"
            )

            # TODO This is redundant work, does this matter?
            constraint_monomials = needed_monomials(
                generate_monomials(self.objective.free_symbols, k_i, self.commutative),
                self.substitution_rules,
            )

            self.constraint_moment_matrices.append(
                create_constraint_matrix(
                    constraint_monomials,
                    constraint.polynomial,
                    self.substitution_rules,
                    self.commutative,
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
            lambda monomial: apply_rule(monomial * constraint, self.substitution_rules),
            self.monomials,
        )
        ruled_filtered_monomials: filter[sp.Expr] = filter(
            lambda monomial: sp.poly(monomial).total_degree()
            <= 2 * self.relaxation_order,
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
