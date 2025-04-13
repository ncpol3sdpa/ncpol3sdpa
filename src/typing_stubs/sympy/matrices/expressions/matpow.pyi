from .matexpr import MatrixExpr as MatrixExpr
from .special import Identity as Identity
from sympy.core import S as S
from sympy.core.cache import cacheit as cacheit
from sympy.core.expr import ExprBuilder as ExprBuilder
from sympy.core.power import Pow as Pow
from sympy.matrices import MatrixBase as MatrixBase
from sympy.matrices.exceptions import NonSquareMatrixError as NonSquareMatrixError

class MatPow(MatrixExpr):
    def __new__(cls, base, exp, evaluate: bool = False, **options): ...
    @property
    def base(self): ...
    @property
    def exp(self): ...
    @property
    def shape(self): ...
    def doit(self, **hints): ...
