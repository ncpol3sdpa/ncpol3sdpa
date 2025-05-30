from __future__ import annotations
from typing import Dict, List, Tuple

from sympy import Expr, S, Mul


# TODO This is a temporary fix. Should be removed when issue #15 "Substitution rule oversight/bug" is resolved
def remove_one_coeff(expr: Expr) -> Expr:
    if isinstance(expr, Mul):
        coef, rest = expr.as_coeff_Mul()
        if coef == 1.0:
            return rest  # type: ignore
    return expr


class Rules:
    def __init__(self, dictionary: Dict[Expr, Expr] | None = None) -> None:
        if dictionary is None:
            self.rules = {}
        else:
            self.rules = dictionary

    def add_rule(self, old: Expr, new: Expr) -> None:
        """Appends a new substitution rule in place"""
        self.rules[old] = new

    def _divides_factors(
        self, monomial1: Expr, monomial2: Expr
    ) -> None | Tuple[Expr, Expr]:
        """If monomial1 divides monomial2 (ie there exists a,b s.t. monomial2 = a * monomial1 * b),
        returns a and b. otherwise return None.
        The monomials must be nonzero and without a numeric coefficient in from of them
        """
        # implemented by subclasses, different if the problem is commutative or not
        raise NotImplementedError

    def divides_factors(
        self, monomial1: Expr, monomial2: Expr
    ) -> None | Tuple[Expr, Expr]:
        """If monomial1 divides monomial2 (ie there exists a,b s.t. monomial2 = a * monomial1 * b),
        returns a and b. otherwise return None.
        This version also accepts monomials with coefficients on them
        """
        if monomial2 == S.Zero:
            return S.Zero, S.Zero
        if monomial1 == S.Zero:
            return None
        if len(monomial1.free_symbols) == 0:
            return (monomial2 / monomial1) * S.One, S.One

        c1, c2 = 1, 1
        if isinstance(monomial1, Mul):
            c1, monomial1 = monomial1.as_coeff_Mul()
        if isinstance(monomial2, Mul):
            c2, monomial2 = monomial2.as_coeff_Mul()

        res = self._divides_factors(monomial1, monomial2)
        if res is not None:
            a, b = res
            return (c2 / c1) * a, b
        else:
            return None

    def divides(self, monomial1: Expr, monomial2: Expr) -> bool:
        """Check if monomial1 divides monomial2.
        ie there exists a,b s.t. monomial2 = a * monomial1 * b"""

        return self.divides_factors(monomial1, monomial2) is not None

    def apply_to_monomial(self, monomial: Expr) -> Expr:
        """Apply rules to a monomial.
        Expects monomials to be non zero and without a numeric coefficient"""
        for key in self.rules.keys():
            result = self.divides_factors(key, monomial)
            if result is not None:
                a, b = result
                return self.apply_to_monomial(a * self.rules[key] * b)
        return remove_one_coeff(monomial)  # TODO remove remove_one coeff #15

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
            return any([self.divides(key, p) for key in self.rules.keys()])

        return [monomial for monomial in monomials if not bigger_than_a_key(monomial)]
