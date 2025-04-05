from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.numbers import I as I, pi as pi
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.functions import assoc_legendre as assoc_legendre
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.complexes import Abs as Abs, conjugate as conjugate
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, cot as cot, sin as sin

class Ynm(Function):
    @classmethod
    def eval(cls, n, m, theta, phi): ...
    def fdiff(self, argindex: int = 4): ...
    def as_real_imag(self, deep: bool = True, **hints): ...

def Ynm_c(n, m, theta, phi): ...

class Znm(Function):
    @classmethod
    def eval(cls, n, m, theta, phi): ...
