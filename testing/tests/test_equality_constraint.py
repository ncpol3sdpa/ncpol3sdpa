import sympy as sp

from ncpol3sdpa.resolution.rules import RulesCommutative, RulesNoncommutative


def test_apply_rule() -> None:
    x, y = sp.symbols("x y")
    rules = RulesCommutative({x**2: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x**6 * y**2 * 5
    assert sp.simplify(rules.apply_to_monomial(p1) - x * y) == 0
    assert sp.simplify(rules.apply_to_monomial(p2) - x * y) == 0
    assert sp.simplify(rules.apply_to_monomial(p3) - 5 * x * y**2) == 0


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
