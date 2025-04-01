from typing import Dict, Tuple
from sympy import Expr, Symbol, symbols


def coefficients_dict(expr: Expr) -> Dict[Expr, int]:
    return expr.as_coefficients_dict()  # type: ignore


def generate_n_variables(n: int) -> Tuple[Symbol, ...]:
    """returns n variables in a tuple, indexed (x0, x1, ... x{n-1})"""
    return list(symbols(f"x0:{n}"))
