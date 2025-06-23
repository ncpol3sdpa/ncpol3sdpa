from __future__ import annotations
from typing import List, Type, Any, TypeVar, Iterable, Set

from sympy import Expr
import sympy as sp


type Matrix = List[List[Expr]]


def sympy_sum(terms: Iterable[sp.Expr]) -> sp.Expr:
    res: sp.Expr = sp.sympify(0)
    for term in terms:
        res += term
    return res


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
    total: Set[sp.Symbol] = set([])
    for p in polynomials:
        total = total | set(p.free_symbols)  # type: ignore

    return list(total)


T = TypeVar("T")


class NoPublicConstructor(type):
    """Metaclass that ensures a private constructor

    If a class uses this metaclass like this:

        class SomeClass(metaclass=NoPublicConstructor):
            pass

    If you try to instantiate your class (`SomeClass()`),
    a `TypeError` will be thrown.
    """

    def __call__(cls, *args: Any, **kwargs: Any) -> None:
        raise TypeError(
            f"{cls.__module__}.{cls.__qualname__} has no public constructor"
        )

    def _create(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        return super().__call__(*args, **kwargs)  # type: ignore
