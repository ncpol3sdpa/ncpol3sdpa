import sympy as sp

from ncpol3sdpa import Constraint
from ncpol3sdpa.resolution import Rule


def test_rule_of_constraint() -> None:
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    pol3 = sp.poly(x - 2)
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    c3 = Constraint.EqualityConstraint(pol3)
    assert Rule.of_single_constraint(c1) == (x**2, x + 1)
    assert Rule.of_single_constraint(c2) == (x * y**2, 2 * x**2 - 4 * y)
    # Oui c'est up peut stupide, mais nécessaire pour le bon typage
    assert Rule.of_single_constraint(c3) == (x, 2 * sp.core.numbers.One())


def test_rules_of_constraints() -> None:
    x, y = sp.symbols("x y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    assert Rule([c1, c2]).rules == {x**2: x + 1, x * y**2: 2 * x**2 - 4 * y}


def test_apply_rule() -> None:
    x, y = sp.symbols("x y")
    rules = Rule.from_dict({x**2: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x**6 * y**2 * 5
    assert rules.apply_to_monomial(p1) == x * y
    assert rules.apply_to_monomial(p2) == x * y
    assert rules.apply_to_monomial(p3) == 5 * x * y**2

    # non commutative tests
    x, y = sp.symbols("x y", commutative=False)
    rules = Rule.from_dict({x * y: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x * y * x * y
    p4 = x * y * y
    assert rules.apply_to_monomial(p1, False) == x
    assert rules.apply_to_monomial(p2, False) == x**2
    assert rules.apply_to_monomial(p3, False) == x**2
    assert rules.apply_to_monomial(p4, False) == x
