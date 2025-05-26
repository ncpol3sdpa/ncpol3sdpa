from sympy import Expr, Symbol, symbols
from sympy.core.numbers import One as SymOne


from ncpol3sdpa import Constraint
from ncpol3sdpa.resolution import Rule

from typing import List


def test_needed_monomials() -> None:
    x: Symbol = symbols("x")
    y: Symbol = symbols("y")
    pol1: Expr = x**2 - x
    pol2: Expr = y**3 - 6 * x * y
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    rules = Rule([c1, c2])
    monomials_list: List[Expr] = [
        # TODO fix this typing error
        SymOne(),
        x,
        x**2,
        y,
        y**2,
        x * y,
        x**2 * y,
        x * y**2,
        x**3,
        y**3,
    ]
    res = set(rules.filter_monomials(monomials_list))
    expected = [1, x, y, x * y, y**2, x * y**2]
    assert len(res) == len(expected)
    for monomial in expected:
        assert monomial in res
