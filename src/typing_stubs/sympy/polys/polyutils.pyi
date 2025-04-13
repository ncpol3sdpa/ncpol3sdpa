from _typeshed import Incomplete
from sympy.core import Add as Add, Eq as Eq, Expr as Expr, Mul as Mul, Pow as Pow, S as S, expand_mul as expand_mul, expand_multinomial as expand_multinomial
from sympy.core.exprtools import decompose_power as decompose_power, decompose_power_rat as decompose_power_rat
from sympy.external.gmpy import GROUND_TYPES as GROUND_TYPES
from sympy.polys.domains.modularinteger import ModularInteger as ModularInteger
from sympy.polys.polyerrors import GeneratorsError as GeneratorsError, PolynomialError as PolynomialError
from sympy.polys.polyoptions import build_options as build_options

illegal_types: Incomplete
finf: Incomplete

def parallel_dict_from_expr(exprs, **args): ...
def dict_from_expr(expr, **args): ...
def expr_from_dict(rep, *gens): ...
parallel_dict_from_basic = parallel_dict_from_expr
dict_from_basic = dict_from_expr
basic_from_dict = expr_from_dict

class PicklableWithSlots: ...

class IntegerPowerable:
    def __pow__(self, e, modulo: Incomplete | None = None): ...
