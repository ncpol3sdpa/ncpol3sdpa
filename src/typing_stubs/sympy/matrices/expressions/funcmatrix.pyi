from .matexpr import MatrixExpr as MatrixExpr
from sympy.core.function import FunctionClass as FunctionClass, Lambda as Lambda
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.complexes import im as im, re as re
from sympy.matrices import Matrix as Matrix

class FunctionMatrix(MatrixExpr):
    def __new__(cls, rows, cols, lamda): ...
    @property
    def shape(self): ...
    @property
    def lamda(self): ...
