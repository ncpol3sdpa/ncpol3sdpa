from sympy.core.expr import Expr

__all__ = ['Commutator']

class Commutator(Expr):
    is_commutative: bool
    def __new__(cls, A, B): ...
    @classmethod
    def eval(cls, a, b): ...
    def doit(self, **hints): ...
