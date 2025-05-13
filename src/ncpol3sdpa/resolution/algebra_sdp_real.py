import sympy as sp
import math

from ncpol3sdpa.resolution.algebra import AlgebraSDP
from ncpol3sdpa.resolution.utils import degree_of_polynomial


class AlgebraSDPReal(AlgebraSDP):
    def get_adjoint(self, monomial: sp.Expr) -> sp.Expr:
        if self.is_commutative:
            return monomial
        else:
            return monomial.adjoint()  # type: ignore

    def get_length_constraint_matrix(self, deg_pol: int) -> int:
        k_i = math.floor(self.relaxation_order - deg_pol / 2)
        return k_i

    def is_expressible_as_moment_coeff(self, monomial: sp.Expr) -> bool:
        return degree_of_polynomial(monomial) <= 2 * self.relaxation_order
