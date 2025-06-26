import sympy as sp
from numpy import float64
from typing import Tuple

from ncpol3sdpa.resolution.algebra import AlgebraSDP, ConstraintGroup
from ncpol3sdpa.resolution.utils import degree_of_polynomial


class AlgebraSDPReal(AlgebraSDP):
    def get_adjoint(self, monomial: sp.Expr) -> sp.Expr:
        return monomial

    @property
    def is_commutative(self) -> bool:
        return True

    def get_length_constraint_matrix(self, deg_pol: int) -> int:
        k_i = self.relaxation_order - deg_pol // 2
        return k_i

    def is_expressible_as_moment_coeff(self, monomial: sp.Expr) -> bool:
        return degree_of_polynomial(monomial) <= 2 * self.relaxation_order

    @property
    def DTYPE(self) -> type:
        """Return the type of the objects in the algebra"""
        return float64

    @property
    def is_real(self) -> bool:
        return True

    def expand_eq_constraint(self, constraint: sp.Expr) -> ConstraintGroup:
        """
        Generate a list of polynomials {p = m * constraint | m : monomial & degre(p) <= 2*k }
        where k is the relaxation order. 2k are monomials that "fit inside" the moment matrix.

        Used for equality constraints.
        """

        # Map and filter are lazy
        # so intermediate lists are not created
        ruled: map[Tuple[sp.Expr, sp.Expr]] = map(
            lambda monomial: (
                monomial,
                self.substitution_rules.apply_to_polynomial(monomial * constraint),
            ),
            self.monomials,
        )
        ruled_filtered: filter[Tuple[sp.Expr, sp.Expr]] = filter(
            lambda t: self.is_expressible_as_moment_coeff(t[1]),
            ruled,
        )
        mon, z_poly = list(zip(*ruled_filtered))
        monomial_multipliers: map[Tuple[sp.Expr, sp.Expr]] = map(
            lambda m: (sp.S.One, m), mon
        )

        return ConstraintGroup(
            zero_polynomials=list(z_poly), monomial_multiples=list(monomial_multipliers)
        )
