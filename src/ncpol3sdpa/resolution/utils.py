from __future__ import annotations
from typing import List, Dict, Any

from sympy import Expr
import sympy as sp

from .rules import Rule

type Matrix = List[List[Expr]]


def degree_of_polynomial(polynomial: Expr) -> int:
    polynomial = polynomial.expand()
    terms = polynomial.as_ordered_terms()
    res = 0
    for term in terms:
        factors = term.as_ordered_factors()
        deg = 0
        for factor in factors:
            if not factor.is_number:
                _, exp = factor.as_base_exp()
                deg += exp
        res = max(deg, res)
    return res


# def needed_monomials(monomials: List[Expr], rules: Dict[Expr, Expr]) -> List[Expr]:
#     """Filter the monomials according to the rules"""
#     # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]

#     return Rule.filter_monomials(
#         monomials,
#         rules,
#     )


def create_moment_matrix(
    monomials: List[sp.Expr],
    substitution_rules: Dict[sp.Expr, Any],
    is_commutative: bool = True,
    is_real: bool = True,
) -> Matrix:
    """Create the moment matrix of the monomials"""

    matrix_size = len(monomials)
    return [
        [
            Rule.apply_to_monomial(
                (
                    monomials[j]
                    if (is_commutative and is_real)
                    else (
                        monomials[j].conjugate()  # type: ignore
                        if not is_real
                        else monomials[j].adjoint()  # type: ignore
                    )
                )
                * monomials[i],
                substitution_rules,
                is_commutative,
            )
            for j in range(i + 1)
        ]
        for i in range(matrix_size)
    ]


def create_constraint_matrix(
    monomials: List[sp.Expr],
    constraint_polynomial: sp.Expr,
    rules: Dict[sp.Expr, Any],
    is_commutative: bool = True,
    is_real: bool = True,
) -> Matrix:
    """Create the matrix of constraints
    The constraints are of the form `constraint_polynomial >= 0`
    """

    n = len(monomials)
    return [
        [
            Rule.apply_to_polynomial(
                sp.expand(
                    (
                        monomials[j]
                        if is_commutative and is_real
                        else (
                            monomials[j].conjugate()  # type: ignore
                            if not is_real
                            else monomials[j].adjoint()  # type: ignore
                        )
                    )
                    * constraint_polynomial
                    * monomials[i]
                ),
                rules,
                is_commutative,
            )
            for j in range(i + 1)
        ]
        for i in range(n)
    ]


def generate_needed_symbols(polynomials: List[sp.Expr]) -> List[sp.Symbol]:
    total: sp.Expr = sp.S.One
    for p in polynomials:
        total += p

    return list(total.free_symbols)  # type: ignore
