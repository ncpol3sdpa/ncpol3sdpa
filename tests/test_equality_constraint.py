import sympy as sp
from ncpol3sdpa.constraints import Constraint
from ncpol3sdpa.rules import Rule, apply_rule


def test_rule_of_constraint() -> None:
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    pol3 = sp.poly(x - 2)
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    c3 = Constraint.EqualityConstraint(pol3)
    assert Rule._of_constraint(c1) == (x**2, x + 1)
    assert Rule._of_constraint(c2) == (x * y**2, 2 * x**2 - 4 * y)
    # Oui c'est up peut stupide, mais nécessaire pour le bon typage
    assert Rule._of_constraint(c3) == (x, 2 * sp.core.numbers.One())


def test_rules_of_constraints() -> None:
    x, y = sp.symbols("x y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    assert Rule.of_constraints([c1, c2]) == {x**2: x + 1, x * y**2: 2 * x**2 - 4 * y}


def test_apply_rule() -> None:
    x, y = sp.symbols("x y")
    rules = {x**2: x}
    p1 = x * y
    p2 = x**2 * y
    p3 = x**6 * y**2 * 5
    assert apply_rule(p1, rules) == x * y
    assert apply_rule(p2, rules) == x * y
    assert apply_rule(p3, rules) == 5 * x * y**2

    # non commutative tests
    x, y = sp.symbols("x y", commutative=False)
    rules = {x * y: x}
    p1 = x * y
    p2 = x**2 * y
    p3 = x * y * x * y
    p4 = x * y * y
    assert apply_rule(p1, rules, False) == x
    assert apply_rule(p2, rules, False) == x**2
    assert apply_rule(p3, rules, False) == x**2
    assert apply_rule(p4, rules, False) == x
