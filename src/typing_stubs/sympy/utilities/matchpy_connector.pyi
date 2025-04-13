from _typeshed import Incomplete
from matchpy import Wildcard
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.expr import Expr as Expr
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.relational import Equality as Equality, Unequality as Unequality
from sympy.core.symbol import Symbol as Symbol
from sympy.external import import_module as import_module
from sympy.functions import cos as cos, cot as cot, csc as csc, erf as erf, gamma as gamma, log as log, sec as sec, sin as sin, tan as tan, uppergamma as uppergamma
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.hyperbolic import acosh as acosh, acoth as acoth, acsch as acsch, asech as asech, asinh as asinh, atanh as atanh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.trigonometric import acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan
from sympy.functions.special.error_functions import Ei as Ei, erfc as erfc, erfi as erfi, fresnelc as fresnelc, fresnels as fresnels
from sympy.integrals.integrals import Integral as Integral
from sympy.printing.repr import srepr as srepr
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from typing import Any, NamedTuple

matchpy: Incomplete
__doctest_requires__: Incomplete

def _(operation): ...
def sympy_op_factory(old_operation, new_operands, variable_name: bool = True): ...

class Wildcard:
    min_count: Incomplete
    fixed_size: Incomplete
    variable_name: Incomplete
    optional: Incomplete
    def __init__(self, min_length, fixed_size, variable_name, optional) -> None: ...

class _WildAbstract(Wildcard, Symbol):
    min_length: int
    fixed_size: bool
    def __init__(self, variable_name: Incomplete | None = None, optional: Incomplete | None = None, **assumptions) -> None: ...
    def __new__(cls, variable_name: Incomplete | None = None, optional: Incomplete | None = None, **assumptions): ...
    def __getnewargs__(self): ...
    @staticmethod
    def __xnew__(cls, variable_name: Incomplete | None = None, optional: Incomplete | None = None, **assumptions): ...
    def __copy__(self) -> _WildAbstract: ...

class WildDot(_WildAbstract):
    min_length: int
    fixed_size: bool

class WildPlus(_WildAbstract):
    min_length: int
    fixed_size: bool

class WildStar(_WildAbstract):
    min_length: int
    fixed_size: bool

class ReplacementInfo(NamedTuple):
    replacement: Any
    info: Any

class Replacer:
    def __init__(self, common_constraints: list = [], lambdify: bool = False, info: bool = False) -> None: ...
    def add(self, expr: Expr, replacement, conditions_true: list[Expr] = [], conditions_nonfalse: list[Expr] = [], info: Any = None) -> None: ...
    def replace(self, expression, max_count: int = -1): ...
