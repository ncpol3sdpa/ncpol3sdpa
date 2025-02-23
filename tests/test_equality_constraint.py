import sys 
sys.path.append('../src/')

import sympy as sp
from equality_constraints import *
from constraints import *

def test_rule_of_constraint():
    x, y = sp.symbols('x y')
    pol1 = sp.poly(x**2 - x -1) 
    pol2 = sp.poly(3*x*y**2 - 6*x**2 + 12*y) 
    c1 = Constraint(True, pol1)
    c2 = Constraint(True, pol2)
    assert(rule_of_constraint(c1) == [x**2,x+1]) 
    assert(rule_of_constraint(c2) == [x*y**2, 2*x**2 - 4*y])
    
def test_rules_of_constraints():
    x, y = sp.symbols('x y')
    pol1 = sp.poly(x**2 - x -1) 
    pol2 = sp.poly(3*x*y**2 - 6*x**2 + 12*y) 
    c1 = Constraint(True, pol1)
    c2 = Constraint(True, pol2)
    assert(rules_of_constraints([c1, c2]) == {x**2: x + 1, x*y**2: 2*x**2 - 4*y})


