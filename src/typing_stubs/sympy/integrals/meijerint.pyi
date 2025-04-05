from .integrals import Integral as Integral
from _typeshed import Incomplete
from sympy import SYMPY_DEBUG as SYMPY_DEBUG
from sympy.core import Expr as Expr, S as S
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.cache import cacheit as cacheit
from sympy.core.containers import Tuple as Tuple
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import Function as Function, expand as expand, expand_mul as expand_mul, expand_power_base as expand_power_base, expand_trig as expand_trig
from sympy.core.intfunc import ilcm as ilcm
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Rational as Rational, pi as pi
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild, symbols as symbols
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, im as im, periodic_argument as periodic_argument, polar_lift as polar_lift, polarify as polarify, principal_branch as principal_branch, re as re, sign as sign, unbranched_argument as unbranched_argument, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, exp_polar as exp_polar, log as log
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction, cosh as cosh, sinh as sinh
from sympy.functions.elementary.integers import ceiling as ceiling
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise, piecewise_fold as piecewise_fold
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction, cos as cos, sin as sin, sinc as sinc
from sympy.functions.special.bessel import besseli as besseli, besselj as besselj, besselk as besselk, bessely as bessely
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.functions.special.elliptic_integrals import elliptic_e as elliptic_e, elliptic_k as elliptic_k
from sympy.functions.special.error_functions import Chi as Chi, Ci as Ci, Ei as Ei, Shi as Shi, Si as Si, erf as erf, erfc as erfc, erfi as erfi, expint as expint, fresnelc as fresnelc, fresnels as fresnels
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.functions.special.hyper import hyper as hyper, meijerg as meijerg
from sympy.functions.special.singularity_functions import SingularityFunction as SingularityFunction
from sympy.logic.boolalg import And as And, BooleanAtom as BooleanAtom, BooleanFunction as BooleanFunction, Not as Not, Or as Or
from sympy.polys import cancel as cancel, factor as factor
from sympy.utilities.iterables import multiset_partitions as multiset_partitions
from sympy.utilities.timeutils import timethis as timethis

z: Incomplete
timeit: Incomplete

class _CoeffExpValueError(ValueError): ...

def meijerint_indefinite(f, x): ...
def meijerint_definite(f, x, a, b): ...
def meijerint_inversion(f, x, t): ...
