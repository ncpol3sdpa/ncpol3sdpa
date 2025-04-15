from __future__ import annotations
from functools import cmp_to_key
from typing import List, Dict, Set, Any, Iterable
from sympy import Expr, Symbol, total_degree, sympify, S


class Poly:
    def __add__(self, other: Poly) -> Poly:
        raise NotImplementedError

    def __mul__(self, other: Poly) -> Poly:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    @classmethod
    def symbols(cls, name: str) -> Poly:
        """returns a Poly that represents a symbol"""
        raise NotImplementedError

    @classmethod
    def Zero(cls) -> Poly:
        raise NotImplementedError

    @classmethod
    def One(cls) -> Poly:
        raise NotImplementedError

    def expand(self) -> Poly:
        """Expand an expression"""
        raise NotImplementedError

    # def total_degree(self) -> int:
    #     """Return the total_degree in the given variables"""
    #     raise NotImplementedError

    def rem(self, other: Poly) -> Poly:
        """
        Compute polynomial remainder
        Could be replace by substitution
        """

        raise NotImplementedError

    def poly(self) -> Poly:
        """Not used"""
        raise NotImplementedError

    def terms(self) -> List[Poly]:
        """Returns all non-zero terms from ``f`` in lex order.

        Examples
        ========
        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).terms()
        [((2, 0), 1), ((1, 2), 2), ((1, 1), 1), ((0, 1), 3)]"""
        raise NotImplementedError

    def gens(self) -> List[Poly]:
        """Returns the generators of the polynomial

        Examples
        ========
        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).gens()
        [x, y]"""

        raise NotImplementedError

    def as_coefficients_dict(self) -> Dict[Poly, Any]:
        """Return the dictionary of the polynomial's coefficients

        Examples
        ========
        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).as_coefficients_dict()
        {x**2: 1, x*y**2: 2, x*y: 1, y: 3}"""
        raise NotImplementedError

    def free_symbols(self) -> Set[Poly]:
        """Return the free symbols of the polynomial
        same as gens"""

        return set(self.gens())


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
    symbols: Iterable[Symbol], relaxation_order: int, commutative: bool = True
) -> List[Expr]:
    """returns a list of all monomials that have degree less or equal to the relaxation_order"""
    
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
        
        return sorted(
            res,
            key = total_degree
        )
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
