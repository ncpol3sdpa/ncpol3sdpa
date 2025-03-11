# from sympy.polys import monomials
import sympy as sp
from ncpol3sdpa.equality_constraints import rules_of_constraints
from ncpol3sdpa.constraints import Constraint
from ncpol3sdpa.momentmatrix import (
    needed_monomials,
    create_matrix,
    create_moment_matrix,
)


def test_needed_monomials():
    x, y = sp.symbols("x y")
    pol1 = sp.poly(x**2 - x - 1)
    pol2 = sp.poly(3 * x * y**2 - 6 * x**2 + 12 * y)
    c1 = Constraint(True, pol1)
    c2 = Constraint(True, pol2)
    rules = rules_of_constraints([c1, c2])
    monomials_list = [1, x, x**2, y, y**2, x * y, x**2 * y, x * y**2, x**3, y**3]
    assert needed_monomials(monomials_list, rules) == [
        1,
        x,
        y,
        y**2,
        x * y,
        x**2 * y,
        x**3,
        y**3,
    ]


def test_create_matrix():
    assert create_matrix([1, 2, 3]) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_create_moment_matrix():
    x, y = sp.symbols("x y")
    monomial = [1, x, y]
    matrix, variable_of_monomial = create_moment_matrix(monomial)
    n = len(matrix)
    assert matrix == [
        [variable_of_monomial[monomial[i] * monomial[j]] for i in range(n)]
        for j in range(n)
    ]
