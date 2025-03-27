from __future__ import annotations
from typing import List, Tuple, Dict, Any
from sympy import Expr, Symbol, symbols, expand, S
import sympy as sp
from ncpol3sdpa.rules import apply_rule, apply_rule_to_polynom
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.constraints import Constraint
import math


def needed_monomials(monomials: List[Expr], rules: Dict[Expr, Expr]) -> List[Expr]:
    """Filter the monomials according to the rules"""
    # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
    return [monomial for monomial in monomials if monomial not in rules.keys()]


def create_moment_matrix(monomials: List[Expr]) -> List[List[Expr]]:
    """Create the moment matrix of the monomials"""
    return [[x * y for x in monomials] for y in monomials]


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


def create_constraint_matrix(
    monomials: List[sp.Expr], Q: sp.Expr, q: sp.Expr
) -> List[List[sp.Expr]]:
    """Create the matrix of constraints
    The constraints are of the form Q(X,Y) >= 0
    """
    return [[(q - Q) * (x * y) for x in monomials] for y in monomials]


def create_constraint_matrix_commutative(
    monomials: List[sp.Expr], constraint_polynomial: sp.Expr, rules: Dict[sp.Expr, Any]
) -> List[List[sp.Expr]]:
    """Create the matrix of constraints
    The constraints are of the form `constraint_polynomial >= 0`
    """

    n = len(monomials)
    return [
        [
            apply_rule_to_polynom(
                sp.expand(monomials[i] * monomials[j] * constraint_polynomial), rules
            )
            for j in range(i + 1)
        ]
        for i in range(n)
    ]


def create_moment_matrix_cvxpy(
    monomials: List[Expr], rules: Dict[Expr, Expr]
) -> Tuple[List[List[Symbol]], Dict[Expr, Any]]:
    """Return a moment matrix whith cvxpy variables"""

    index_var: int = 0
    variable_of_monomial: Dict[Expr, Any] = {}
    moment_matrix: List[List[Symbol]] = []

    for i, monom1 in enumerate(monomials):
        moment_matrix.append([])
        for monom2 in monomials:
            monom: Expr = apply_rule(monom1 * monom2, rules)
            if monom not in variable_of_monomial:
                variable_of_monomial[monom] = symbols(f"y{index_var}")
                index_var += 1
            moment_matrix[i].append(variable_of_monomial[monom])

    return moment_matrix, variable_of_monomial


def create_constraints_matrix_cvxpy(
    variable_of_monomial: Dict[Expr, Any],
    monomials: List[Expr],
    polynom: Expr,
    rules: Dict[Expr, Any],
) -> List[List[Expr]]:
    """return the matrix of contraint with cvxpy variables"""

    n = len(monomials)
    matrix: List[List[Expr]] = [[S.Zero for _ in range(n)] for _ in range(n)]

    for i, monom1 in enumerate(monomials):
        for j, monom2 in enumerate(monomials):
            moment_coeff: Expr = expand(
                apply_rule_to_polynom(monom1 * monom2 * polynom, rules)
            )  # type: ignore
            constraints_dict = moment_coeff.as_coefficients_dict()  # type: ignore
            for term, coeff in constraints_dict.items():
                matrix[i][j] += coeff * variable_of_monomial[term]

    return matrix


def generate_needed_symbols(polynomials: List[sp.Expr]) -> List[sp.Symbol]:
    sum: sp.Expr = 1
    for p in polynomials:
        sum += p

    # Type check
    for s in sum.free_symbols:
        assert isinstance(s, sp.Symbol)
    res: List[sp.Symbol] = list(sum.free_symbols)

    return res


class MomentMatrix:
    def __init__(self, polynom: Expr, monomials: List[Expr]) -> None:
        self.optimized = None
        self.constraints = None

    def __mul__(self, other: MomentMatrix) -> MomentMatrix:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def _method1(self) -> None:
        raise NotImplementedError


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
        self.objective = apply_rule_to_polynom(sp.expand(objective), substitution_rules)

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
            self.equality_constraints.append(constraint.polynom)
        else:
            # inequality constraint
            # p.10 of Semidefinite programming relaxations for quantum correlations

            k_i = math.floor(self.relaxation_order - sp.degree(constraint.polynom) / 2)
            assert k_i >= 0, (
                "Insufficient relaxation order to capture the constraint {constraint.polynom}"
            )

            # TODO This is redundant work, does this matter?
            constraint_monomials = needed_monomials(
                generate_monomials_commutative(self.objective.free_symbols, k_i),
                self.substitution_rules,
            )

            self.constraint_moment_matrices.append(
                create_constraint_matrix_commutative(
                    constraint_monomials, constraint.polynom, self.substitution_rules
                )
            )

    def expand_eq_constraint(self, constraint: sp.Expr) -> List[sp.Expr]:
        """Generate a list of polynomials {p = m * constraint | m : monomial & degre(p) <= 2*k }
        where k is the relaxation order. 2k are monomials that "fit inside" the moment matrix.
        Used for equality constraints."""
        res1 = [
            apply_rule_to_polynom(
                sp.expand(monomial * constraint), self.substitution_rules
            )
            for monomial in self.monomials
        ]

        # It is better to filter after expanding and substituting, maybe substitution rules can reduce the degree
        return [
            poly
            for poly in res1
            if sp.Poly(poly).total_degree() <= 2 * self.relaxation_order
        ]

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for constraint in constraints:
            self.add_constraint(constraint)

    def __string__(self) -> str:
        """return String representation is  for debugging"""

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
