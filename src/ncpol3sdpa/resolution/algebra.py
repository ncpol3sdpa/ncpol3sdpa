from __future__ import annotations
from typing import List, Tuple, Dict, Callable, NamedTuple, Generator
from functools import reduce

import sympy as sp
from scipy.sparse import lil_matrix

from .constraints import Constraint, ConstraintType
from .monomial import generate_monomials
from .rules import Rules
from .utils import Matrix, degree_of_polynomial, tensor_product_lower_triangle


class ConstraintGroup(NamedTuple):
    """Stores Equality constraint metadata for the SOS decomposition

    Invariants:
       * monomial_multiples[0] = (1,1)
       * for all i, zero_polynomials[i] = adjoint(monomial_multiples[i][0]) * zero_polynomials[0] * monomial_multiples[i][1]
    """

    """Zero polynomials have substitution rules already applied to them"""
    zero_polynomials: List[sp.Expr]
    monomial_multiples: List[Tuple[sp.Expr, sp.Expr]]


def create_moment_matrix(
    monomials: List[sp.Expr],
    substitution_rules: Rules,
    is_commutative: bool = True,
    get_adjoint: Callable[[sp.Expr], sp.Expr] = lambda x: x,
) -> Matrix:
    """Creates a moment matrix with monomials, substitution rules. Defaults to the real commutative case"""
    matrix_size = len(monomials)
    return [
        [
            substitution_rules.apply_to_monomial(
                get_adjoint(monomials[j]) * monomials[i]
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
        needed_variables: List[List[sp.Symbol]],
        objective: sp.Expr,
        relaxation_order: int,
        substitution_rules: Rules,
        more_monomials: List[sp.Expr] = [],
    ) -> None:
        """
        Construct the symbolic Moment Matrices and soundings data structures.

        Works for the commutative case only.
        """

        self.needed_variables = needed_variables
        self.relaxation_order: int = relaxation_order
        self.substitution_rules: Rules = substitution_rules
        self.all_monomials: List[List[sp.Expr]] = [
            substitution_rules.filter_monomials(
                generate_monomials(
                    needed_variables[i], relaxation_order, self.is_commutative
                )
                + more_monomials
            )
            for i in range(len(needed_variables))
        ]
        self.objective: sp.Expr = substitution_rules.apply_to_polynomial(
            sp.expand(objective)
        )

        self.moment_matrices = [
            create_moment_matrix(
                substitution_rules=self.substitution_rules,
                monomials=self.all_monomials[i],
                is_commutative=self.is_commutative,
                get_adjoint=self.get_adjoint,
            )
            for i in range(len(self.all_monomials))
        ]

        # In the commutative case, the moment matrix is symmetric
        self.moment_matrix = (
            self.moment_matrices[0]
            if len(self.moment_matrices) == 1
            else reduce(tensor_product_lower_triangle, self.moment_matrices)
        )
        matrix_size: int = len(self.moment_matrix)

        self.monomials: List[sp.Expr] = [x for xs in self.all_monomials for x in xs]

        # equivalence classes of equal coefficients
        self.monomial_to_positions: Dict[sp.Expr, List[Tuple[int, int]]] = {}
        for i in range(matrix_size):
            for j in range(i + 1):
                monomial = self.moment_matrix[i][j]
                self.add_monomial_to_positions(monomial, i, j)

        # This is the positive semi-definite matrices in the sdp
        self.constraint_moment_matrices: List[Matrix] = []
        self.psd_polynomials_gi: List[sp.Expr] = []
        # List of polynomials that equal 0
        self.equality_constraints: List[ConstraintGroup] = []
        # List of local inequality constraints
        self.local_inequality_constraints: List[sp.Expr] = []

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

    def polynomial_to_matrix(self, poly: sp.Expr, real_part: bool = True) -> lil_matrix:
        """Returns a hermitian A matrix such that poly = Tr(A.T @ G) where G is the moment matrix.
        In the complex case, Re(tr(ρ poly)) = Tr(A.T @ G), or Im(tr(ρ poly)) = Tr(A.T @ G) depending on real_part parameter
        In other words express poly as a linear combination of the coefficients of G.
        Requires that all monomials of poly exist within the moment matrix:
        poly.free_vars included in algebra.moment_matrix free_vars
        and deg(poly) <= 2*algebra.relaxation_order"""
        moment_matrix_size = len(self.moment_matrix)
        a_0: lil_matrix = lil_matrix(
            (moment_matrix_size, moment_matrix_size), dtype=self.DTYPE
        )

        for monomial, coef in sp.expand(poly).as_coefficients_dict().items():
            if sp.I in coef.atoms():  # type: ignore
                coef /= sp.I
                coef = float(coef)
                coef *= 1j  # type: ignore
            if sp.I in monomial.atoms():  # type: ignore
                monomial /= sp.I
                coef = float(coef)
                coef *= 1j  # type: ignore

            assert monomial in self.monomial_to_positions.keys()
            assert 0 < len(self.monomial_to_positions[monomial])

            # The 0 is arbitrary (?) could be any other element of the list.
            # TODO/Idea What happens if we chose other than 0? at random?
            monomial_x, monomial_y = self.monomial_to_positions[monomial][0]

            # The matrices must be hermitian
            if real_part:
                # real part constraint
                a_0[monomial_x, monomial_y] += 0.5 * coef
                a_0[monomial_y, monomial_x] += 0.5 * coef.conjugate()
            else:
                # imaginary part constraint
                a_0[monomial_x, monomial_y] += -0.5j * coef
                a_0[monomial_y, monomial_x] += 0.5j * coef.conjugate()

        return a_0

    def add_inequality_constraint(self, constraint: sp.Expr) -> None:
        # inequality constraint
        # p.10 of Semidefinite programming relaxations for quantum correlations

        k_i = self.get_length_constraint_matrix(degree_of_polynomial(constraint))
        assert k_i >= 0, (
            "Insufficient relaxation order to capture the constraint {constraint.polynomial}"
        )

        # TODO This is redundant work, does this matter?
        constraint_monomials = self.substitution_rules.filter_monomials(
            generate_monomials(
                [var for vars in self.needed_variables for var in vars],
                k_i,
                self.is_commutative,
            )
        )

        self.constraint_moment_matrices.append(
            self.create_constraint_matrix(
                constraint_monomials,
                constraint,
            )
        )
        self.psd_polynomials_gi.append(constraint)

    def add_equality_constraint(self, constraint: sp.Expr) -> None:
        self.equality_constraints.append(self.expand_eq_constraint(constraint))

    def add_constraint(self, constraint: Constraint) -> None:
        """Add a constraint to the algebra

        Save the constraint if it is an equality constraint,
        otherwise update the moment matrix for the inequality constraint"""
        match constraint.constraint_type:
            case ConstraintType.EQUALITY:
                self.add_equality_constraint(constraint.polynomial)
            case ConstraintType.INEQUALITY:
                self.add_inequality_constraint(constraint.polynomial)
            case ConstraintType.LOCAL_INEQUALITY:
                self.local_inequality_constraints.append(constraint.polynomial)

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for constraint in constraints:
            self.add_constraint(constraint)

    def add_monomial_to_positions(self, monomial: sp.Expr, i: int, j: int) -> None:
        """Add a monomial to the list of monomials and its position in the moment matrix"""

        if monomial in self.monomial_to_positions.keys():
            self.monomial_to_positions[monomial].append((i, j))
        else:
            self.monomial_to_positions[monomial] = [(i, j)]

    def _cross_product_monomials(self) -> Generator[Tuple[sp.Expr, sp.Expr]]:
        for n in self.monomials:
            for m in self.monomials:
                yield (n, m)

    def expand_eq_constraint(self, constraint: sp.Expr) -> ConstraintGroup:
        """
        Generate a list of polynomials {p = m * constraint | m : monomial & degre(p) <= 2*k }
        where k is the relaxation order. 2k are monomials that "fit inside" the moment matrix.

        Used for equality constraints.
        """

        # Map and filter are lazy
        # so intermediate lists are not created
        monomial_pairs = self._cross_product_monomials()
        ruled: map[Tuple[sp.Expr, sp.Expr, sp.Expr]] = map(
            lambda monomials: (
                monomials[0],
                self.substitution_rules.apply_to_polynomial(
                    self.get_adjoint(monomials[0]) * constraint * monomials[1]
                ),
                monomials[1],
            ),
            monomial_pairs,
        )
        ruled_filtered: filter[Tuple[sp.Expr, sp.Expr, sp.Expr]] = filter(
            lambda t: self.is_expressible_as_moment_coeff(t[1]),
            ruled,
        )
        z_poly = map(lambda t: t[1], ruled_filtered)
        monomial_multipliers = map(lambda t: (t[0], t[2]), ruled_filtered)

        return ConstraintGroup(
            zero_polynomials=list(z_poly), monomial_multiples=list(monomial_multipliers)
        )

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
                        self.get_adjoint(monomials[j])
                        * constraint_polynomial
                        * monomials[i]
                    )
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
