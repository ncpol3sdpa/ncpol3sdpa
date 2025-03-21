from __future__ import annotations
from functools import cmp_to_key
from typing import List, Dict, Set, Any, TypeVar, Iterable
from sympy import total_degree

class Monomial:
    def __init__(self) -> None: ...

    def __add__(self, other: Monomial) -> Monomial:
        raise NotImplementedError

    def __mul__(self, other: Monomial) -> Monomial:
        raise NotImplementedError
    
    def __repr__(self) -> str:
        raise NotImplementedError
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError
    

    @classmethod
    def symbols(cls, name : str) -> Monomial:
        """returns a monomial that represents a symbol"""
        raise NotImplementedError
    
    @classmethod
    def Zero(cls) -> Monomial:
        raise NotImplementedError
    
    @classmethod
    def One(cls) -> Monomial:
        raise NotImplementedError
    

    def expand(self) -> Monomial:
        """Expand an expression"""
        raise NotImplementedError
    
    def total_degree(self) -> int:
        """Return the total_degree in the given variables"""
        raise NotImplementedError
    
    def rem(self, other: Monomial) -> Monomial:
        """
        Compute polynomial remainder
        Could be replace by substitution
        """

        raise NotImplementedError
    
    def poly(self) -> Monomial:
        """Not used"""
        raise NotImplementedError
    
    def terms(self) -> List[Monomial]:
        """Returns all non-zero terms from ``f`` in lex order.

        Examples
        ========
        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).terms()
        [((2, 0), 1), ((1, 2), 2), ((1, 1), 1), ((0, 1), 3)]"""
        raise NotImplementedError
    
    def gens(self) -> List[Monomial]:
        """Returns the generators of the polynomial
        
        Examples
        ========
        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).gens()
        [x, y]"""

        raise NotImplementedError
    
    def as_coefficients_dict(self) -> Dict[Monomial, Any]:
        """Return the dictionary of the polynomial's coefficients
        
        Examples
        ========
        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).as_coefficients_dict()
        {x**2: 1, x*y**2: 2, x*y: 1, y: 3}"""
        raise NotImplementedError
    
    def free_symbols(self) -> Set[Monomial]:
        """Return the free symbols of the polynomial
        same as gens"""
        raise NotImplementedError


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
