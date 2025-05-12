from sympy import Expr, Symbol, symbols
from sympy.core.numbers import One as SymOne


from ncpol3sdpa import Constraint
from ncpol3sdpa.resolution import Rule
from ncpol3sdpa.resolution.utils import needed_monomials

from typing import List


def test_needed_monomials() -> None:
    x: Symbol = symbols("x")
    y: Symbol = symbols("y")
    pol1: Expr = x**2 - x - 1
    pol2: Expr = 3 * x * y**2 - 6 * x**2 + 12 * y
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    rules = Rule.of_constraints([c1, c2])
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
    assert needed_monomials(monomials_list, rules) == [
        1,
        x,
        y,
        y**2,
        x * y,
        x**2 * y,
        x**3,
        y**3,
    ]
