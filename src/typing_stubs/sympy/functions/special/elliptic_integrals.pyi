from _typeshed import Incomplete
from sympy.core import I as I, Rational as Rational, S as S, pi as pi
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.symbol import Dummy as Dummy, uniquely_named_symbol as uniquely_named_symbol
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.hyperbolic import atanh as atanh
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import sin as sin, tan as tan
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.functions.special.hyper import hyper as hyper, meijerg as meijerg

class elliptic_k(Function):
    @classmethod
    def eval(cls, m): ...
    def fdiff(self, argindex: int = 1): ...

class elliptic_f(Function):
    @classmethod
    def eval(cls, z, m): ...
    def fdiff(self, argindex: int = 1): ...

class elliptic_e(Function):
    @classmethod
    def eval(cls, m, z: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...

class elliptic_pi(Function):
    @classmethod
    def eval(cls, n, m, z: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...
