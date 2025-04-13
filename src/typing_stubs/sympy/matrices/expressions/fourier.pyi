from _typeshed import Incomplete
from sympy.core.numbers import I as I
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.matrices.expressions import MatrixExpr as MatrixExpr

class DFT(MatrixExpr):
    def __new__(cls, n): ...
    n: Incomplete
    shape: Incomplete

class IDFT(DFT): ...
