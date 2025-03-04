import sys

import monomial 
sys.path.append('../src/')

import sympy as sp
from equality_constraints import *
from constraints import *
from momentmatrix import * 

def test_needed_monomials():
    x, y = sp.symbols('x y')
    pol1 = sp.poly(x**2 - x -1) 
    pol2 = sp.poly(3*x*y**2 - 6*x**2 + 12*y) 
    c1 = Constraint(True, pol1)
    c2 = Constraint(True, pol2)
    rules = rules_of_constraints([c1, c2])
    monomials = [1, x, x**2, y, y**2, x*y, x**2*y, x*y**2, x**3, y**3]
    assert(needed_monomials(monomials, rules) == [1, x, y, y**2, x*y, x**2*y, x**3, y**3])


def test_create_matrix([1,2,3]):
    M = create_matrix([1,2,3])
    N = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
[[1, 2, 0], [0, 0, 0], [0, 0, 0]]
[[1, 2, 3], [0, 0, 0], [0, 0, 0]]
[[1, 2, 3], [2, 0, 0], [0, 0, 0]]
[[1, 2, 3], [2, 4, 0], [0, 0, 0]]
[[1, 2, 3], [2, 4, 6], [0, 0, 0]]
[[1, 2, 3], [2, 4, 6], [3, 0, 0]]
[[1, 2, 3], [2, 4, 6], [3, 6, 0]]
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]

    assert ( M== N)

