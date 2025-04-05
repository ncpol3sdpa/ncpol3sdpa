from sympy.core import Add as Add, Dummy as Dummy, S as S, expand_func as expand_func
from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, PoleError as PoleError
from sympy.core.logic import fuzzy_and as fuzzy_and, fuzzy_not as fuzzy_not
from sympy.core.numbers import I as I, Rational as Rational, oo as oo, pi as pi
from sympy.core.power import Pow as Pow
from sympy.functions.combinatorial.factorials import RisingFactorial as RisingFactorial, factorial as factorial, rf as rf
from sympy.functions.combinatorial.numbers import bernoulli as bernoulli, harmonic as harmonic
from sympy.functions.elementary.complexes import re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, cot as cot, sin as sin
from sympy.functions.special.error_functions import Ei as Ei, erf as erf, erfc as erfc
from sympy.functions.special.zeta_functions import zeta as zeta
from sympy.utilities.misc import as_int as as_int

def intlike(n): ...

class gamma(Function):
    unbranched: bool
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class lowergamma(Function):
    def fdiff(self, argindex: int = 2): ...
    @classmethod
    def eval(cls, a, x): ...

class uppergamma(Function):
    def fdiff(self, argindex: int = 2): ...
    @classmethod
    def eval(cls, a, z): ...

class polygamma(Function):
    @classmethod
    def eval(cls, n, z): ...
    def fdiff(self, argindex: int = 2): ...

class loggamma(Function):
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...

class digamma(Function):
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, z): ...

class trigamma(Function):
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, z): ...

class multigamma(Function):
    unbranched: bool
    def fdiff(self, argindex: int = 2): ...
    @classmethod
    def eval(cls, x, p): ...
