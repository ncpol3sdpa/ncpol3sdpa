import sympy as sp

from ncpol3sdpa.resolution.algebra import AlgebraSDP
from ncpol3sdpa.resolution.utils import degree_of_polynomial


class AlgebraSDPComplex(AlgebraSDP):
    def get_adjoint(self, monomial: sp.Expr) -> sp.Expr:
        if self.is_commutative:
            return monomial.conjugate()  # type: ignore
        else:
            return monomial.adjoint()  # type: ignore

    def add_monomial_to_positions(self, monomial: sp.Expr, i: int, j: int) -> None:
        if monomial in self.monomial_to_positions.keys():
            self.monomial_to_positions[monomial].append((i, j))
        else:
            self.monomial_to_positions[monomial] = [(i, j)]

        if i != j:
            monomial = self.get_adjoint(self.moment_matrix[i][j])
            if monomial in self.monomial_to_positions.keys():
                self.monomial_to_positions[monomial].append((j, i))
            else:
                self.monomial_to_positions[monomial] = [(j, i)]

    def get_length_constraint_matrix(self, deg_pol: int) -> int:
        k_i = self.relaxation_order - deg_pol
        return k_i

    def is_expressible_as_moment_coeff(self, monomial: sp.Expr) -> bool:
        return degree_of_polynomial(monomial) <= self.relaxation_order
