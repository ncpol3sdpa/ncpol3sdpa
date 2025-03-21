from __future__ import annotations
from functools import cmp_to_key
from typing import List, Dict, Any, TypeVar, Iterable
from sympy import total_degree

class Monomial:
    def __init__(self) -> None: ...

    def __add__(self, other: Monomial) -> Monomial:
        raise NotImplementedError

    def simplify(self) -> None: ...



def list_increment(degrees: List[int], k: int) -> bool:
    """increment l as a base k number. returns True if overflows, False otherwirse"""

    for i, x in enumerate(degrees):
        if x < k - 1:
            degrees[i] += 1
            return False
        else:
            assert x == k - 1
            degrees[i] = 0
    return True


def generate_monomials_commutative(
    symbols: Iterable[Any], relaxation_order: int
) -> List[Any]:
    """returns a list of all monomials that have degree less or equal to the relaxation_order"""
    current_degres = [0 for _ in symbols]
    res = []

    while True:
        expr = 1
        for i, symbol in enumerate(symbols):
            expr *= symbol ** current_degres[i]
        if total_degree(expr) <= relaxation_order:
            res.append(expr)

        if list_increment(current_degres, relaxation_order + 1):
            break

    return sorted(
        res,
        key=cmp_to_key(
            lambda item1, item2: total_degree(item1) - total_degree(item2)
        ),
    )

T = TypeVar("T")
def create_backward_dictionary(monomials: List[T]) -> Dict[T, int]:
    """returns a dictionary that maps monomials to their index in the list"""
    return {
        monomial: i for i, monomial in enumerate(monomials)
    }
