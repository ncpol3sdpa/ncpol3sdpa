from typing import Dict
from sympy import Expr

def coefficients_dict(expr : Expr) -> Dict[Expr, int]:
    return expr.as_coefficients_dict() # type: ignore
