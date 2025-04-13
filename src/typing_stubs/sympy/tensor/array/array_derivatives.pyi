from .arrayop import derive_by_array as derive_by_array
from .ndim_array import NDimArray as NDimArray
from sympy.core.expr import Expr as Expr
from sympy.core.function import Derivative as Derivative
from sympy.core.numbers import Integer as Integer
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr
from sympy.matrices.expressions.special import ZeroMatrix as ZeroMatrix
from sympy.matrices.matrixbase import MatrixBase as MatrixBase

class ArrayDerivative(Derivative):
    is_scalar: bool
    def __new__(cls, expr, *variables, **kwargs): ...
    @property
    def shape(self): ...
