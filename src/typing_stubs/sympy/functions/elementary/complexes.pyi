from _typeshed import Incomplete
from sympy.core import Add as Add, Basic as Basic, Dummy as Dummy, Mul as Mul, S as S, Symbol as Symbol, sympify as sympify
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, ArgumentIndexError as ArgumentIndexError, Derivative as Derivative, Function as Function, expand_mul as expand_mul
from sympy.core.logic import fuzzy_not as fuzzy_not, fuzzy_or as fuzzy_or
from sympy.core.numbers import I as I, oo as oo, pi as pi
from sympy.core.power import Pow as Pow
from sympy.core.relational import Eq as Eq
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise

class re(Function):
    args: tuple[Expr]
    is_extended_real: bool
    unbranched: bool
    @classmethod
    def eval(cls, arg): ...
    def as_real_imag(self, deep: bool = True, **hints): ...

class im(Function):
    args: tuple[Expr]
    is_extended_real: bool
    unbranched: bool
    @classmethod
    def eval(cls, arg): ...
    def as_real_imag(self, deep: bool = True, **hints): ...

class sign(Function):
    is_complex: bool
    def doit(self, **hints): ...
    @classmethod
    def eval(cls, arg): ...

class Abs(Function):
    args: tuple[Expr]
    is_extended_real: bool
    is_extended_negative: bool
    is_extended_nonnegative: bool
    unbranched: bool
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class arg(Function):
    is_extended_real: bool
    is_real: bool
    is_finite: bool
    @classmethod
    def eval(cls, arg): ...

class conjugate(Function):
    @classmethod
    def eval(cls, arg): ...
    def inverse(self): ...

class transpose(Function):
    @classmethod
    def eval(cls, arg): ...

class adjoint(Function):
    @classmethod
    def eval(cls, arg): ...

class polar_lift(Function):
    is_polar: bool
    is_comparable: bool
    @classmethod
    def eval(cls, arg): ...

class periodic_argument(Function):
    @classmethod
    def eval(cls, ar, period): ...

def unbranched_argument(arg): ...

class principal_branch(Function):
    is_polar: bool
    is_comparable: bool
    @classmethod
    def eval(self, x, period): ...

def polarify(eq, subs: bool = True, lift: bool = False): ...
def unpolarify(eq, subs: Incomplete | None = None, exponents_only: bool = False): ...
