from __future__ import annotations
from typing import List, Iterable

from sympy import Expr, Symbol, total_degree, sympify, S


def list_increment(degrees: List[int], k: int) -> bool:
    """increment l as a base k number. returns True if overflows, False otherwise"""

    for i, x in enumerate(degrees):
        if x < k - 1:
            degrees[i] += 1
            return False
        else:
            assert x == k - 1
            degrees[i] = 0
    return True


def generate_monomials(
    symbols: Iterable[Symbol],
    relaxation_order: int,
    commutative: bool = True,
    real: bool = True,
) -> List[Expr]:
    """returns a list of all monomials that have degree less or equal to the relaxation_order"""
    symbols = list(symbols)

    if commutative:
        current_degrees = [0 for _ in symbols]
        res: List[Expr] = []

        while True:
            expr = S.One
            for i, symbol in enumerate(symbols):
                expr *= symbol ** current_degrees[i]
            if total_degree(expr) <= relaxation_order:
                res.append(expr)

            if list_increment(current_degrees, relaxation_order + 1):
                break

        return sorted(res, key=total_degree)
    else:
        res = [sympify(1)]

        def dfs(i: int, curr_monomials: List[Expr], pred_monomials: List[Expr]) -> None:
            if i > relaxation_order:
                return
            for monomial in pred_monomials:
                for symbol in symbols:
                    if symbol != 1:
                        res.append(monomial * symbol)
                        curr_monomials.append(monomial * symbol)
            dfs(i + 1, [], curr_monomials)

        dfs(0, [sympify(1)], [])
        return res
