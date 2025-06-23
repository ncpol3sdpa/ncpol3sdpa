from ncpol3sdpa.resolution.rules import Rules

from typing import List, Tuple
from sympy import Expr, Mul, Pow


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


class RulesNoncommutative(Rules):
    def _divides_factors(
        self, monomial1: Expr, monomial2: Expr
    ) -> None | Tuple[Expr, Expr]:
        """If monomial1 divides monomial2 (ie there exists a,b s.t. monomial2 = a * monomial1 * b),
        returns a and b. otherwise return None
        """
        m1_list = list_of_monomial(monomial1)
        m2_list = list_of_monomial(monomial2)

        for i in range(len(m2_list) - len(m1_list) + 1):
            if m2_list[i : i + len(m1_list)] == m1_list:
                return (
                    Mul(*m2_list[: max(0, i)]),
                    Mul(*m2_list[(i + len(m1_list)) :]),
                )

        return None
