from __future__ import annotations
from typing import List, Tuple, Dict, Any
from sympy import Expr
import sympy as sp
from ncpol3sdpa.rules import apply_rule, apply_rule_to_polynomial
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.constraints import Constraint
import math


def needed_monomials(monomials: List[Expr], rules: Dict[Expr, Expr]) -> List[Expr]:
    """Filter the monomials according to the rules"""
    # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
    return [monomial for monomial in monomials if monomial not in rules.keys()]


def create_moment_matrix_commutative(
    monomials: List[sp.Expr], substitution_rules: Dict[sp.Expr, Any]
) -> List[List[sp.Expr]]:
    """Create the moment matrix of the monomials for the commutative case"""

    matrix_size = len(monomials)
    return [
        [
            apply_rule(monomials[i] * monomials[j], substitution_rules)
            for j in range(i + 1)
        ]
        for i in range(matrix_size)
    ]


def create_constraint_matrix_commutative(
    monomials: List[sp.Expr], constraint_polynomial: sp.Expr, rules: Dict[sp.Expr, Any]
) -> List[List[sp.Expr]]:
    """Create the matrix of constraints
    The constraints are of the form `constraint_polynomial >= 0`
    """

    n = len(monomials)
    return [
        [
            apply_rule_to_polynomial(
                sp.expand(monomials[i] * monomials[j] * constraint_polynomial), rules # type: ignore
            )
            for j in range(i + 1)
        ]
        for i in range(n)
    ]


def generate_needed_symbols(polynomials: List[sp.Expr]) -> List[sp.Symbol]:
    total: sp.Expr = sp.S.One
    for p in polynomials:
        total += p

    # Type check (useless ???)
    for s in total.free_symbols:
        assert isinstance(s, sp.Symbol)

    return list(total.free_symbols) # type: ignore


class AlgebraSDP:
    def __init__(
        self,
        needed_variables: List[sp.Symbol],
        objective: sp.Expr,
        relaxation_order: int,
        substitution_rules: Dict[sp.Expr, sp.Expr],
    ) -> None:
        """Construct the symbolic Moment Matrices and soundings data structures. Works for the commutative case"""
        self.relaxation_order = relaxation_order
        self.substitution_rules = substitution_rules
        self.monomials: List[sp.Expr] = needed_monomials(
            generate_monomials_commutative(needed_variables, relaxation_order),
            substitution_rules,
        )
        self.objective = apply_rule_to_polynomial(
            sp.expand(objective), substitution_rules # type: ignore
        )

        # In the commutative case, the moment matrix is symmetric
        self.moment_matrix = create_moment_matrix_commutative(
            self.monomials, self.substitution_rules
        )
        matrix_size = len(self.moment_matrix)

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
        if constraint.is_equality_constraint:
            self.equality_constraints.append(constraint.polynomial)
        else:
            # inequality constraint
            # p.10 of Semidefinite programming relaxations for quantum correlations

            k_i = math.floor(
                self.relaxation_order - sp.degree(constraint.polynomial) / 2
            )
            assert k_i >= 0, (
                "Insufficient relaxation order to capture the constraint {constraint.polynomial}"
            )

            # TODO This is redundant work, does this matter?
            constraint_monomials = needed_monomials(
                generate_monomials_commutative(self.objective.free_symbols, k_i),
                self.substitution_rules,
            )

            self.constraint_moment_matrices.append(
                create_constraint_matrix_commutative(
                    constraint_monomials, constraint.polynomial, self.substitution_rules
                )
            )

    def expand_eq_constraint(self, constraint: sp.Expr) -> List[sp.Expr]:
        """Generate a list of polynomials {p = m * constraint | m : monomial & degre(p) <= 2*k }
        where k is the relaxation order. 2k are monomials that "fit inside" the moment matrix.
        Used for equality constraints."""
        res1 = [
            apply_rule_to_polynomial(
                sp.expand(monomial * constraint),  # type: ignore
                self.substitution_rules
            )
            for monomial in self.monomials
        ]

        # It is better to filter after expanding and substituting, maybe substitution rules can reduce the degree
        return [
            poly
            for poly in res1
            if sp.Poly(poly).total_degree() <= 2 * self.relaxation_order # type: ignore
        ]

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for constraint in constraints:
            self.add_constraint(constraint)

    def __string__(self) -> str:
        """return String representation for debugging"""

        # The print on the moment matrix is not very good
        return f"Algebra:\
\n\
relaxation_order: {self.relaxation_order}\n\
monomials\n\
{self.monomials}\n\
moment_matrix\n\
{self.moment_matrix}\n\
substitution_rules\n\
{self.substitution_rules}\n\
monomial_to_positions\n\
{self.monomial_to_positions}\n\
equality_constraints\n\
{self.equality_constraints}\n\
constraint_moment_matrices\n\
{self.constraint_moment_matrices}\n"
