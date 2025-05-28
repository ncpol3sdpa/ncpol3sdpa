import sympy as sp

from ncpol3sdpa.resolution import Rules


def test_apply_rule() -> None:
    x, y = sp.symbols("x y")
    rules = Rules({x**2: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x**6 * y**2 * 5
    assert rules.apply_to_monomial(p1) == x * y
    assert rules.apply_to_monomial(p2) == x * y
    assert rules.apply_to_monomial(p3) == 5 * x * y**2


def test_apply_rule_nc() -> None:
    # non commutative tests
    x, y = sp.symbols("x y", commutative=False)
    rules = Rules({x * y: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x * y * x * y
    p4 = x * y * y
    assert rules.apply_to_monomial(p1, False) == x
    assert rules.apply_to_monomial(p2, False) == x**2
    assert rules.apply_to_monomial(p3, False) == x**2
    assert rules.apply_to_monomial(p4, False) == x
