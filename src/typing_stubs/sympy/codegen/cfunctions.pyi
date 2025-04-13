from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.numbers import Rational as Rational
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.miscellaneous import sqrt as sqrt

class expm1(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class log1p(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class exp2(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class log2(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class fma(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...

class log10(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class Sqrt(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...

class Cbrt(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...

class hypot(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...

class isnan(Function):
    nargs: int
