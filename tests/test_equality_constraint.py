import sympy as sp
from ncpol3sdpa.constraints import Constraint
from ncpol3sdpa.equality_constraints import rule_of_constraint, rules_of_constraints, apply_rule


def test_rule_of_constraint():
    x, y = sp.symbols("x y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    pol3 = sp.poly(x-2)
    c1 = Constraint(True, pol1)
    c2 = Constraint(True, pol2)
    c3 = Constraint(True, pol3)
    assert rule_of_constraint(c1) == [x**2, x + 1]
    assert rule_of_constraint(c2) == [x * y**2, 2 * x**2 - 4 * y]
    assert rule_of_constraint(c3) == [x, 2]


def test_rules_of_constraints():
    x, y = sp.symbols("x y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    c1 = Constraint(True, pol1)
    c2 = Constraint(True, pol2)
    assert rules_of_constraints([c1, c2]) == {x**2: x + 1, x * y**2: 2 * x**2 - 4 * y}

def test_apply_rule():
    x, y = sp.symbols("x y")
    rules = {x**2 : x} 
    p1 = x*y 
    p2 = x**2*y 
    p3 = x**6*y**2 * 5 
    assert(apply_rule(p1, rules) == x*y)
    assert(apply_rule(p2, rules) == x*y)
    assert(apply_rule(p3, rules) == 5*x*y**2)

