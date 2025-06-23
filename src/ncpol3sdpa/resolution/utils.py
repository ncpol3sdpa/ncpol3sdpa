from __future__ import annotations
from typing import List, TypeAlias

from sympy import Expr
import sympy as sp


Matrix: TypeAlias = List[List[Expr]]


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


def generate_needed_symbols(polynomials: List[sp.Expr]) -> List[sp.Symbol]:
    total: sp.Expr = sp.S.One
    for p in polynomials:
        total += p

    return list(total.free_symbols)  # type: ignore
