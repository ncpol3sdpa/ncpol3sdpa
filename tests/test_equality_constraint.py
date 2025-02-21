import sys 
import sympy as sp


sys.path.append('../src/')
from equality_constraints import *
from constraints import *

def test_rule_of_constraint():
    x = sp.symbols('x')
    pol = x**2 - x -1 
    c = Constraint(True, pol)
    assert(rule_of_constraint(c)[0] - x**2 == 0)
    assert(rule_of_constraint(c)[1] - (x+1) == 0)

test_rule_of_constraint()
