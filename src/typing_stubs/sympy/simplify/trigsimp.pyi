from sympy.core import Add as Add, Basic as Basic, Expr as Expr, Mul as Mul, S as S, bottom_up as bottom_up, factor_terms as factor_terms, sympify as sympify
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import Derivative as Derivative, FunctionClass as FunctionClass, count_ops as count_ops, expand as expand, expand_mul as expand_mul
from sympy.core.intfunc import igcd as igcd
from sympy.core.numbers import I as I, Integer as Integer
from sympy.core.symbol import Dummy as Dummy, Wild as Wild, symbols as symbols
from sympy.external.gmpy import SYMPY_INTS as SYMPY_INTS
from sympy.functions import atan2 as atan2, cos as cos, cosh as cosh, cot as cot, coth as coth, exp as exp, sin as sin, sinh as sinh, tan as tan, tanh as tanh
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction
from sympy.polys import Poly as Poly, cancel as cancel, factor as factor, parallel_poly_from_expr as parallel_poly_from_expr
from sympy.polys.domains import ZZ as ZZ
from sympy.polys.polyerrors import PolificationFailed as PolificationFailed
from sympy.polys.polytools import groebner as groebner
from sympy.simplify.cse_main import cse as cse
from sympy.strategies.core import identity as identity
from sympy.strategies.tree import greedy as greedy
from sympy.utilities.iterables import iterable as iterable
from sympy.utilities.misc import debug as debug

def trigsimp_groebner(expr, hints=[], quick: bool = False, order: str = 'grlex', polynomial: bool = False): ...
def trigsimp(expr, inverse: bool = False, **opts): ...
def exptrigsimp(expr): ...
def trigsimp_old(expr, *, first: bool = True, **opts): ...
def futrig(e, *, hyper: bool = True, **kwargs): ...
