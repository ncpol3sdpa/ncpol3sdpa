from __future__ import annotations
from typing import List, Iterable

from sympy import Expr, total_degree, sympify, S
from sympy.physics.quantum import Operator


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
    symbols: Iterable[Expr | Operator],
    relaxation_order: int,
    is_commutative: bool = True,
) -> List[Expr]:
    """returns a list of all monomials that have degree less or equal to the relaxation_order"""

    if is_commutative:
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
        pred_monomials: List[Expr] = [sympify(1)]

        new_symbols = list(symbols)
        for symbol in symbols:
            if not symbol.is_hermitian:  # type: ignore
                new_symbols.append(symbol.adjoint())  # type: ignore

        for _ in range(relaxation_order):
            pred_monomials = [
                monomial * symbol
                for monomial in pred_monomials
                for symbol in new_symbols
                if symbol != 1
            ]
            res.extend(pred_monomials)

        return res
