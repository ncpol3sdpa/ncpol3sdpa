from sympy import Expr, Symbol, symbols
from sympy.core.numbers import One as SymOne


from ncpol3sdpa.resolution import Rules

from typing import List


def test_needed_monomials() -> None:
    x: Symbol = symbols("x")
    y: Symbol = symbols("y")
    rules = Rules({x**2: x, y**3: 6 * x * y})
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
