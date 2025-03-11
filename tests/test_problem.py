from ncpol3sdpa.problem import *
from ncpol3sdpa.constraints import *
import sympy as sp
from sympy.abc import x, y

def test_1():
    obj = 2*x*y
    p = Problem(obj)
    c1 = Constraint(True, x*x-x)
    c2 = Constraint(False, -y*y + y + 0.25)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert(abs(p.solve(1) - 2.4142) <= 0.01)
    assert(abs(p.solve(2) - 2.4142) <= 0.01)
    assert(abs(p.solve(3) - 2.4142) <= 0.01)


