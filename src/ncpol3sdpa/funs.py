from typing import Dict, List
from sympy import Expr, Symbol, symbols


def coefficients_dict(expr: Expr) -> Dict[Expr, float]:
    return expr.as_coefficients_dict()


def generate_n_variables(n: int) -> List[Symbol]:
    """returns n variables in a list, indexed (x0, x1, ... x{n-1})"""
    return list(symbols(f"x0:{n}"))


def ith_bit(N: int, i: int) -> int:
    """returns the i-th bit of N"""
    b = (N >> i) % 2
    return b
