from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.assumptions.refine import handlers_dict as handlers_dict
from sympy.core import Basic as Basic, S as S
from sympy.matrices.exceptions import NonSquareMatrixError as NonSquareMatrixError
from sympy.matrices.expressions.matpow import MatPow as MatPow

class Inverse(MatPow):
    is_Inverse: bool
    exp: Incomplete
    def __new__(cls, mat, exp=...): ...
    @property
    def arg(self): ...
    @property
    def shape(self): ...
    def doit(self, **hints): ...

def refine_Inverse(expr, assumptions): ...
