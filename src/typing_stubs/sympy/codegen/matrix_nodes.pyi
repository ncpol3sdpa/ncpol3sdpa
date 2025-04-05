from .ast import Token as Token
from sympy.core.sympify import sympify as sympify
from sympy.matrices import MatrixExpr as MatrixExpr

class MatrixSolve(Token, MatrixExpr):
    @property
    def shape(self): ...
