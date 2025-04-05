from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q
from sympy.matrices.expressions import MatrixExpr as MatrixExpr

class Factorization(MatrixExpr):
    arg: Incomplete
    shape: Incomplete

class LofLU(Factorization):
    @property
    def predicates(self): ...

class UofLU(Factorization):
    @property
    def predicates(self): ...

class LofCholesky(LofLU): ...
class UofCholesky(UofLU): ...

class QofQR(Factorization):
    @property
    def predicates(self): ...

class RofQR(Factorization):
    @property
    def predicates(self): ...

class EigenVectors(Factorization):
    @property
    def predicates(self): ...

class EigenValues(Factorization):
    @property
    def predicates(self): ...

class UofSVD(Factorization):
    @property
    def predicates(self): ...

class SofSVD(Factorization):
    @property
    def predicates(self): ...

class VofSVD(Factorization):
    @property
    def predicates(self): ...

def lu(expr): ...
def qr(expr): ...
def eig(expr): ...
def svd(expr): ...
