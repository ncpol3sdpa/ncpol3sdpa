from ncpol3sdpa.resolution.algebra import AlgebraSDP
import sympy as sp
import math
from typing import List

from ncpol3sdpa.resolution.utils import Matrix, degree_of_polynomial


class AlgebraSDPReal(AlgebraSDP):
    def add_monomial_to_positions(self, monomial: sp.Expr, i: int, j: int) -> None:
        if monomial in self.monomial_to_positions.keys():
            self.monomial_to_positions[monomial].append((i, j))
        else:
            self.monomial_to_positions[monomial] = [(i, j)]

    def get_length_constraint_matrix(self, deg_pol: int) -> int:
        k_i = math.floor(self.relaxation_order - deg_pol / 2)
        return k_i

    def is_expressible_as_moment_coeff(self, monomial: sp.Expr) -> bool:
        return degree_of_polynomial(monomial) <= 2 * self.relaxation_order

    def create_moment_matrix(self) -> Matrix:
        matrix_size = len(self.monomials)
        return [
            [
                self.substitution_rules.apply_to_monomial(
                    (
                        self.monomials[j]
                        if self.is_commutative
                        else self.monomials[j].adjoint()  # type: ignore
                    )
                    * self.monomials[i],
                    self.is_commutative,
                )
                for j in range(i + 1)
            ]
            for i in range(matrix_size)
        ]

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
                        (
                            monomials[j]
                            if self.is_commutative
                            else monomials[j].adjoint()  # type: ignore
                        )
                        * constraint_polynomial
                        * monomials[i]
                    ),
                    self.is_commutative,
                )
                for j in range(i + 1)
            ]
            for i in range(n)
        ]
