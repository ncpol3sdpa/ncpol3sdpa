# from sympy.polys import monomials
import sympy as sp
from sympy import Expr, Symbol, symbols

from ncpol3sdpa.constraints import Constraint
from ncpol3sdpa.rules import Rule
from ncpol3sdpa.momentmatrix import (
    create_moment_matrix,
    create_moment_matrix_cvxpy,
    needed_monomials,
)

from typing import List


def test_needed_monomials() -> None:
    x: Symbol = symbols("x")
    y: Symbol = symbols("y")
    pol1: Expr = x**2 - x - 1
    pol2: Expr = 3 * x * y**2 - 6 * x**2 + 12 * y
    c1 = Constraint.EqualityConstraint(pol1)
    c2 = Constraint.EqualityConstraint(pol2)
    rules = Rule.of_constraints([c1, c2])
    monomials_list: List[Expr] = [
        1,
        x,
        x**2,
        y,
        y**2,
        x * y,
        x**2 * y,
        x * y**2,
        x**3,
        y**3,
    ]
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


def test_create_moment_matrix() -> None:
    assert create_moment_matrix([1, 2, 3]) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_create_moment_matrix_cvxpy() -> None:
    x, y = sp.symbols("x y")
    monomial = [1, x, y]
    matrix, variable_of_monomial = create_moment_matrix_cvxpy(monomial, {})
    n = len(matrix)
    assert matrix == [
        [variable_of_monomial[monomial[i] * monomial[j]] for i in range(n)]
        for j in range(n)
    ]
