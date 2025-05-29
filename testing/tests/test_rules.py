import sympy as sp
from sympy import Expr, Symbol, symbols
from sympy.simplify import simplify
from sympy.core.numbers import One as SymOne

from typing import List

from ncpol3sdpa.resolution import RulesCommutative, RulesNoncommutative


def test_apply_rule() -> None:
    x, y = sp.symbols("x y")
    rules = RulesCommutative({x**2: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x**6 * y**2 * 5
    assert simplify(rules.apply_to_monomial(p1) - x * y) == 0
    assert simplify(rules.apply_to_monomial(p2) - x * y) == 0
    assert simplify(rules.apply_to_monomial(p3) - 5 * x * y**2) == 0


def test_apply_rule_nc() -> None:
    # non commutative tests
    x, y = sp.symbols("x y", commutative=False)
    rules = RulesNoncommutative({x * y: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x * y * x * y
    p4 = x * y * y
    assert rules.apply_to_monomial(p1) == x
    assert rules.apply_to_monomial(p2) == x**2
    assert rules.apply_to_monomial(p3) == x**2
    assert rules.apply_to_monomial(p4) == x


def test_needed_monomials() -> None:
    x: Symbol = symbols("x")
    y: Symbol = symbols("y")
    rules = RulesCommutative({x**2: x, y**3: 6 * x * y})
    monomials_list: List[Expr] = [
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


def test_needed_monomials_noncommutative() -> None:
    x: Symbol = symbols("x", commutative=False)
    y: Symbol = symbols("y", commutative=False)
    rules = RulesNoncommutative({x * y: x})
    monomials_list: List[Expr] = [
        SymOne(),
        x,
        y,
        #
        x**2,
        y**2,
        x * y,
        y * x,
        #
        x**2 * y,
        x * y * x,
        y * x**2,
        #
        x * y**2,
        y * x * y,
        y**2 * x,
        #
        x**3,
        y**3,
    ]
    res = set(rules.filter_monomials(monomials_list))
    expected = [
        SymOne(),
        x,
        y,
        #
        x**2,
        y**2,
        # x * y,
        y * x,
        #
        # x**2 * y,
        # x * y * x,
        y * x**2,
        #
        # x * y**2,
        # y * x * y,
        y**2 * x,
        #
        x**3,
        y**3,
    ]
    assert len(res) == len(expected)
    for monomial in expected:
        assert monomial in res


def test_needed_monomials_noncommutative2() -> None:
    x: Symbol = symbols("x", commutative=False)
    y: Symbol = symbols("y", commutative=False)
    rules = RulesNoncommutative({x * y: x, y**2: 6 * y * x})
    monomials_list: List[Expr] = [
        SymOne(),
        x,
        y,
        #
        x**2,
        y**2,
        x * y,
        y * x,
        #
        x**2 * y,
        x * y * x,
        y * x**2,
        #
        x * y**2,
        y * x * y,
        y**2 * x,
        #
        x**3,
        y**3,
    ]
    res = set(rules.filter_monomials(monomials_list))
    expected = [
        SymOne(),
        x,
        y,
        #
        x**2,
        # y**2,
        # x * y,
        y * x,
        #
        # x**2 * y,
        # x * y * x,
        y * x**2,
        #
        # x * y**2,
        # y * x * y,
        # y**2 * x,
        #
        x**3,
        # y**3,
    ]
    assert len(res) == len(expected)
    for monomial in expected:
        assert monomial in res
