from sympy.core.expr import Expr

__all__ = ['InnerProduct']

class InnerProduct(Expr):
    is_complex: bool
    def __new__(cls, bra, ket): ...
    @property
    def bra(self): ...
    @property
    def ket(self): ...
    def doit(self, **hints): ...
