from __future__ import annotations
from typing import List, Tuple, Dict, Any
from sympy import Expr, Symbol, symbols, expand, S
from ncpol3sdpa.rules import apply_rule, apply_rule_to_polynom



def needed_monomials(monomials : List[Expr], rules : Dict[Expr,Expr]) -> List[Expr]:
    """Filter the monomials according to the rules"""
    # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
    return [
        monomial 
        for monomial in monomials 
        if monomial not in rules.keys()
    ]

def create_moment_matrix(monomials : List[Expr]) -> List[List[Expr]]:
    """Create the moment matrix of the monomials"""
    return [
        [ x*y for x in monomials ] 
        for y in monomials
    ]

def create_constraints_matrix(
    monomials : List[Expr],
    Q : Expr,
    q : Expr
) -> List[List[Expr]]:
    """Create the matrix of constraints
    The constraints are of the form Q(X,Y) < q
    """
    return [
        [ (q - Q) * (x * y) for x in monomials ]
        for y in monomials
    ]


def create_moment_matrix_cvxpy(
        monomials : List[Expr], 
        rules : Dict[Expr, Expr]
    ) -> Tuple[List[List[Symbol]], Dict[Expr, Any]]:
    """Return a moment matrix whith cvxpy variables"""

    n : int = len(monomials)
    index_var : int = 0
    variable_of_monomial : Dict[Expr, Any] = {}
    moment_matrix : List[List[Symbol]] = []

    for i, monom1 in enumerate(monomials):
        moment_matrix.append([])
        for monom2 in monomials:
            monom : Expr = apply_rule(monom1 * monom2, rules)
            if monom not in variable_of_monomial:
                variable_of_monomial[monom] = symbols(f"y{index_var}")
                index_var += 1
            moment_matrix[i].append(variable_of_monomial[monom])

    return moment_matrix, variable_of_monomial


def create_constraints_matrix_cvxpy(
        variable_of_monomial : Dict[Expr, Any],
        monomials : List[Expr], 
        polynom : Expr,
        rules : Dict[Expr, Any]
    ) -> List[List[Expr]]:
    """return the matrix of contraint with cvxpy variables"""

    n = len(monomials)
    matrix : List[List[Expr]] = [
        [S.Zero for _ in range(n)] 
        for _ in range(n)
    ]

    for i, monom1 in enumerate(monomials):
        for j, monom2 in enumerate(monomials):
            moment_coeff : Expr = expand(apply_rule_to_polynom(monom1 * monom2 * polynom, rules))
            constraints_dict = moment_coeff.as_coefficients_dict()
            for term, coeff in constraints_dict.items():
                matrix[i][j] += coeff * variable_of_monomial[term]
                
    return matrix


class MomentMatrix:
    def __init__(self, polynom : Expr, monomials : List[Expr]) -> None:
        self.optimized = None
        self.constraints = None

    def __mul__(self, other : MomentMatrix) -> MomentMatrix:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def _method1(self) -> None:
        raise NotImplementedError
