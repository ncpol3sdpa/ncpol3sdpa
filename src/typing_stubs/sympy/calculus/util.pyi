from .accumulationbounds import AccumBounds as AccumBounds, AccumulationBounds as AccumulationBounds
from .singularities import singularities as singularities
from sympy.core import Pow as Pow, S as S
from sympy.core.function import Function as Function, diff as diff, expand_mul as expand_mul
from sympy.core.kind import NumberKind as NumberKind
from sympy.core.mod import Mod as Mod
from sympy.core.numbers import equal_valued as equal_valued
from sympy.core.relational import Relational as Relational
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.elementary.complexes import Abs as Abs, im as im, re as re
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.hyperbolic import acosh as acosh, acoth as acoth, acsch as acsch, asech as asech, asinh as asinh, atanh as atanh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.integers import frac as frac
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction, acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan, cos as cos, cot as cot, csc as csc, sec as sec, sin as sin, tan as tan
from sympy.matrices.dense import hessian as hessian
from sympy.polys.polytools import degree as degree, lcm_list as lcm_list
from sympy.sets.conditionset import ConditionSet as ConditionSet
from sympy.sets.fancysets import ImageSet as ImageSet
from sympy.sets.sets import Complement as Complement, FiniteSet as FiniteSet, Intersection as Intersection, Interval as Interval, Union as Union
from sympy.utilities import filldedent as filldedent
from sympy.utilities.iterables import iterable as iterable

def continuous_domain(f, symbol, domain): ...
def function_range(f, symbol, domain): ...
def not_empty_in(finset_intersection, *syms): ...
def periodicity(f, symbol, check: bool = False): ...
def lcim(numbers): ...
def is_convex(f, *syms, domain=...): ...
def stationary_points(f, symbol, domain=...): ...
def maximum(f, symbol, domain=...): ...
def minimum(f, symbol, domain=...): ...
