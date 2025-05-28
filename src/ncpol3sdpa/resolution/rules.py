from __future__ import annotations
from typing import Dict, List

from sympy import Expr, S, rem, Mul, Pow


def list_of_monomial(monomial: Expr) -> List[Expr]:
    """return a list of the factor a a monomial non commutative"""
    if isinstance(monomial, int):
        return [monomial]
    res = []
    for factor in monomial.as_ordered_factors():
        if isinstance(factor, Pow):
            base, exp = factor.as_base_exp()  # type: ignore
            res.extend([base] * exp)
        else:
            res.append(factor)
    return res


class Rules:
    def __init__(self, dictionary: Dict[Expr, Expr] = {}) -> None:
        self.rules = dictionary

    def add_rule(self, old: Expr, new: Expr) -> None:
        """Appends a new substitution rule in place"""
        self.rules[old] = new

    def apply_to_monomial(self, monomial: Expr, is_commutative: bool = True) -> Expr:
        """Apply rules to a monomial"""
        if is_commutative:
            for key in self.rules.keys():
                if rem(monomial, key) == 0:
                    return self.apply_to_monomial(
                        monomial * self.rules[key] / key, is_commutative
                    )
            return monomial
        else:
            to_change_monomial = list_of_monomial(monomial)
            for key in self.rules.keys():
                rule_monomial = list_of_monomial(key)
                for i in range(len(to_change_monomial) - len(rule_monomial) + 1):
                    if to_change_monomial[i : i + len(rule_monomial)] == rule_monomial:
                        return self.apply_to_monomial(
                            Mul(*(to_change_monomial[: max(0, i)]))
                            * self.rules[key]
                            * Mul(*to_change_monomial[(i + len(rule_monomial)) :]),
                            is_commutative,
                        )
            return monomial

    def apply_to_polynomial(
        self, polynomial: Expr, is_commutative: bool = True
    ) -> Expr:
        """Apply rules to a polynomial"""

        poly_dict: Dict[Expr, float] = polynomial.as_coefficients_dict()

        res: Expr = S.Zero
        for monomial, coef in poly_dict.items():
            res += coef * self.apply_to_monomial(monomial, is_commutative)
        return res

    def filter_monomials(self, monomials: List[Expr]) -> List[Expr]:
        """Filter the monomials according to the rules"""

        # TODO This could be more optimized
        # if a monomial M divides a N such that N -> _ is a rule, then it should not be
        # in the final moment matrix
        def bigger_than_a_key(p: Expr) -> bool:
            return any([rem(p, r) == 0 for r in self.rules.keys()])

        return [monomial for monomial in monomials if not bigger_than_a_key(monomial)]
