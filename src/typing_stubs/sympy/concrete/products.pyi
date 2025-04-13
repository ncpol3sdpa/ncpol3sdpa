from .expr_with_intlimits import ExprWithIntLimits as ExprWithIntLimits
from .summations import Sum as Sum, summation as summation
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import Derivative as Derivative
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.combinatorial.factorials import RisingFactorial as RisingFactorial
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.polys import quo as quo, roots as roots

class Product(ExprWithIntLimits):
    limits: tuple[tuple[Symbol, Expr, Expr]]
    def __new__(cls, function, *symbols, **assumptions): ...
    @property
    def term(self): ...
    function = term
    def doit(self, **hints): ...
    def is_convergent(self): ...
    def reverse_order(expr, *indices): ...

def product(*args, **kwargs): ...
