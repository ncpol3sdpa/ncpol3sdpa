from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.symbol import Dummy as Dummy, uniquely_named_symbol as uniquely_named_symbol
from sympy.functions.combinatorial.numbers import catalan as catalan
from sympy.functions.elementary.complexes import conjugate as conjugate
from sympy.functions.special.gamma_functions import digamma as digamma, gamma as gamma

def betainc_mpmath_fix(a, b, x1, x2, reg: int = 0): ...

class beta(Function):
    unbranched: bool
    def fdiff(self, argindex): ...
    @classmethod
    def eval(cls, x, y: Incomplete | None = None): ...
    def doit(self, **hints): ...

class betainc(Function):
    nargs: int
    unbranched: bool
    def fdiff(self, argindex): ...

class betainc_regularized(Function):
    nargs: int
    unbranched: bool
    def __new__(cls, a, b, x1, x2): ...
    def fdiff(self, argindex): ...
