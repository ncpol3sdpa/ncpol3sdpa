from __future__ import annotations
from typing import List, Iterable, Generator

from sympy import Expr, total_degree, sympify
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


def gen_monomials_commutative(
    degree: int, symbols: List[Expr | Operator]
) -> Generator[Expr]:
    """in the commutative case,
    returns a list of all monomials that have EXACTLY degree :param:`degree`"""
    n = len(symbols)
    if degree == 0:
        yield sympify(1)
    elif n != 0:
        other_symbols = symbols[0 : n - 1]
        x = symbols[n - 1]
        for k in range(degree + 1):
            for monomial in gen_monomials_commutative(degree - k, other_symbols):
                yield x**k * monomial


def generate_monomials(
    symbols: Iterable[Expr | Operator],
    relaxation_order: int,
    is_commutative: bool = True,
) -> List[Expr]:
    """returns a list of all monomials that have degree less or equal to the :param:`relaxation_order`"""

    if is_commutative:
        res: List[Expr] = []
        for i in range(relaxation_order + 1):
            for monomial in gen_monomials_commutative(i, list(symbols)):
                res.append(monomial)

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
