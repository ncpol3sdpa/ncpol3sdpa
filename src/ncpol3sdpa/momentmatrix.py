from __future__ import annotations
from typing import List, Tuple, Dict, Any
import sympy as sp
from ncpol3sdpa.rules import apply_rule, apply_rule_to_polynom


def needed_monomials(monomials : List[sp.Poly], rules : Dict[sp.Poly, Any]) -> List[sp.Poly]:
    """Filter the monomials according to the rules"""
    # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
    return [
        monomial 
        for monomial in monomials 
        if monomial not in rules.keys()
    ]

def create_moment_matrix(monomials : List[sp.Poly]) -> List[List[sp.Poly]]:
    """Create the moment matrix of the monomials"""
    return [
        [ x*y for x in monomials ] 
        for y in monomials
    ]

def create_constraints_matrix(
    monomials : List[sp.Poly],
    Q : sp.Poly,
    q : sp.Poly
) -> List[List[sp.Poly]]:
    """Create the matrix of constraints
    The constraints are of the form Q(X,Y) < q
    """
    return [
        [ (q - Q) * (x * y) for x in monomials ]
        for y in monomials
    ]


def create_moment_matrix_cvxpy(
        monomials : List[sp.Poly], 
        rules : Dict[sp.Poly, Any]
    ) -> Tuple[List[List[sp.Poly]], Dict[sp.Poly, Any]]:
    """Return a moment matrix whith cvxpy variables"""

    n : int = len(monomials)
    index_var : int = 0
    moment_matrix : List[List[sp.Poly]] = [[0 for _ in range(n)] for _ in range(n)]

    for i, monom1 in enumerate(monomials):
        for j, monom2 in enumerate(monomials):
            monom : sp.Poly = apply_rule(monom1 * monom2, rules)
            if monom not in variable_of_monomial:
                variable_of_monomial[monom] = sp.symbols(f"y{index_var}")
                index_var += 1
            moment_matrix[i][j] = variable_of_monomial[monom]

    return moment_matrix, variable_of_monomial


def create_constraints_matrix_cvxpy(
        variable_of_monomial : Dict[sp.Poly, Any],
        monomials : List[sp.Poly], 
        polynom : sp.Poly,
        rules : Dict[sp.Poly, Any]
    ) -> List[List[sp.Poly]]:
    """return the matrix of contraint with cvxpy variables"""

    n = len(monomials)
    matrix : List[List[sp.Poly]] = [[0 for _ in range(n)] for _ in range(n)]

    for i, monom1 in enumerate(monomials):
        for j, monom2 in enumerate(monomials):
            moment_coeff : sp.Poly = apply_rule_to_polynom(monom1 * monom2 * polynom, rules)
            constraints_dict = sp.expand(moment_coeff).as_coefficients_dict()
            for term, coeff in constraints_dict.items():
                matrix[i][j] += coeff * variable_of_monomial[term]
                
    return matrix


class MomentMatrix:
    def __init__(self, polynom : sp.Poly, monomials : List[sp.Poly]) -> None:
        self.optimized = None
        self.constraints = None

    def __mul__(self, other : MomentMatrix) -> MomentMatrix:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def _method1(self) -> None:
        raise NotImplementedError
