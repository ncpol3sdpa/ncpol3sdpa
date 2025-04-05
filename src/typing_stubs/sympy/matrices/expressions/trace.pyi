from sympy.core.basic import Basic as Basic
from sympy.core.expr import Expr as Expr, ExprBuilder as ExprBuilder
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import uniquely_named_symbol as uniquely_named_symbol
from sympy.core.sympify import sympify as sympify
from sympy.matrices.exceptions import NonSquareMatrixError as NonSquareMatrixError
from sympy.matrices.matrixbase import MatrixBase as MatrixBase

class Trace(Expr):
    is_Trace: bool
    is_commutative: bool
    def __new__(cls, mat): ...
    @property
    def arg(self): ...
    def doit(self, **hints): ...
    def as_explicit(self): ...

def trace(expr): ...
