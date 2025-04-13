from _typeshed import Incomplete
from sympy.core import Eq as Eq, Ge as Ge, S as S
from sympy.core.mul import Mul as Mul
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.matrices.expressions import MatrixExpr as MatrixExpr

class DiagonalMatrix(MatrixExpr):
    arg: Incomplete
    shape: Incomplete
    @property
    def diagonal_length(self): ...

class DiagonalOf(MatrixExpr):
    arg: Incomplete
    @property
    def shape(self): ...
    @property
    def diagonal_length(self): ...

class DiagMatrix(MatrixExpr):
    def __new__(cls, vector): ...
    @property
    def shape(self): ...
    def as_explicit(self): ...
    def doit(self, **hints): ...

def diagonalize_vector(vector): ...
