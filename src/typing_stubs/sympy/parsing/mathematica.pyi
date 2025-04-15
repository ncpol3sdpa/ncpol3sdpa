from _typeshed import Incomplete
from sympy import Add as Add, And as And, Ci as Ci, Dummy as Dummy, Ei as Ei, Equality as Equality, Function as Function, GreaterThan as GreaterThan, I as I, Integer as Integer, Lambda as Lambda, LessThan as LessThan, Max as Max, Min as Min, Mod as Mod, Mul as Mul, Or as Or, Pow as Pow, Rational as Rational, S as S, Si as Si, StrictGreaterThan as StrictGreaterThan, StrictLessThan as StrictLessThan, Tuple as Tuple, UnevaluatedExpr as UnevaluatedExpr, acos as acos, acosh as acosh, acot as acot, acoth as acoth, acsc as acsc, acsch as acsch, airyai as airyai, airyaiprime as airyaiprime, airybi as airybi, asec as asec, asech as asech, asin as asin, asinh as asinh, atan as atan, atan2 as atan2, atanh as atanh, cancel as cancel, cos as cos, cosh as cosh, cot as cot, coth as coth, csc as csc, csch as csch, exp as exp, expand as expand, expand_trig as expand_trig, flatten as flatten, im as im, isprime as isprime, log as log, pi as pi, polylog as polylog, prime as prime, primepi as primepi, rf as rf, sec as sec, sech as sech, sign as sign, simplify as simplify, sin as sin, sinh as sinh, sqrt as sqrt, symbols as symbols, tan as tan, tanh as tanh
from sympy.core.sympify import sympify as sympify
from sympy.functions.special.bessel import airybiprime as airybiprime
from sympy.functions.special.error_functions import li as li
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from typing import Any

def mathematica(s, additional_translations: Incomplete | None = None): ...
def parse_mathematica(s): ...

class MathematicaParser:
    CORRESPONDENCES: Incomplete
    fm: Incomplete
    fs: Incomplete
    REPLACEMENTS: Incomplete
    RULES: Incomplete
    FM_PATTERN: Incomplete
    ARG_MTRX_PATTERN: Incomplete
    ARGS_PATTERN_TEMPLATE: str
    TRANSLATIONS: dict[tuple[str, int], dict[str, Any]]
    cache_original: dict[tuple[str, int], dict[str, Any]]
    cache_compiled: dict[tuple[str, int], dict[str, Any]]
    translations: Incomplete
    def __init__(self, additional_translations: Incomplete | None = None) -> None: ...
    def parse(self, s): ...
    INFIX: str
    PREFIX: str
    POSTFIX: str
    FLAT: str
    RIGHT: str
    LEFT: str
