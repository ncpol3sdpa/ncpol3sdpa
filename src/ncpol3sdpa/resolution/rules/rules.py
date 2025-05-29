from __future__ import annotations
from typing import Dict, List, Tuple

from sympy import Expr, S


class Rules:
    def __init__(self, dictionary: Dict[Expr, Expr] = {}) -> None:
        self.rules = dictionary

    def add_rule(self, old: Expr, new: Expr) -> None:
        """Appends a new substitution rule in place"""
        self.rules[old] = new

    def divisible_factors(
        self, monomial1: Expr, monomial2: Expr
    ) -> None | Tuple[Expr, Expr]:
        """If monomial1 divides monomial2 (ie there exists a,b s.t. monomial2 = a * monomial1 * b),
        returns a and b. otherwise return None
        """
        # implemented by subclasses, different if the problem is commutative or not
        raise NotImplementedError

    def divisible(self, monomial1: Expr, monomial2: Expr) -> bool:
        """Check if monomial1 divides monomial2.
        ie there exists a,b s.t. monomial2 = a * monomial1 * b"""

        return self.divisible_factors(monomial1, monomial2) is not None

    def apply_to_monomial(self, monomial: Expr) -> Expr:
        """Apply rules to a monomial"""
        for key in self.rules.keys():
            result = self.divisible_factors(key, monomial)
            if result is not None:
                a, b = result
                return self.apply_to_monomial(a * self.rules[key] * b)
        return monomial

    def apply_to_polynomial(self, polynomial: Expr) -> Expr:
        """Apply rules to a polynomial"""

        poly_dict: Dict[Expr, float] = polynomial.as_coefficients_dict()

        res: Expr = S.Zero
        for monomial, coef in poly_dict.items():
            res += coef * self.apply_to_monomial(monomial)
        return res

    def filter_monomials(self, monomials: List[Expr]) -> List[Expr]:
        """Filter the monomials according to the rules"""

        # TODO This could be more optimized
        # if a monomial M divides a N such that N -> _ is a rule, then it should not be
        # in the final moment matrix
        def bigger_than_a_key(p: Expr) -> bool:
            return any([self.divisible(key, p) for key in self.rules.keys()])

        return [monomial for monomial in monomials if not bigger_than_a_key(monomial)]
