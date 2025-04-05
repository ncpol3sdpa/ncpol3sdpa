from sympy.core import Basic as Basic
from sympy.functions import adjoint as adjoint, conjugate as conjugate
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr

class Adjoint(MatrixExpr):
    is_Adjoint: bool
    def doit(self, **hints): ...
    @property
    def arg(self): ...
    @property
    def shape(self): ...
