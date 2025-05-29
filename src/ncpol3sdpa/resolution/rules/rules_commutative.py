from ncpol3sdpa.resolution.rules import Rules

from typing import Tuple
from sympy import Expr, div
from sympy.core.numbers import S


class RulesCommutative(Rules):
    def divisible_factors(
        self, monomial1: Expr, monomial2: Expr
    ) -> None | Tuple[Expr, Expr]:
        """If monomial1 divides monomial2 (ie there exists a,b s.t. monomial2 = a * monomial1 * b),
        returns a and b. otherwise return None
        """
        q, r = div(monomial2, monomial1, domain="RR")

        if r == 0:
            return S.One, q
        else:
            return None
