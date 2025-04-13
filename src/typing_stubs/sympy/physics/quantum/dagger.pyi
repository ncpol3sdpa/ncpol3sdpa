from sympy.functions.elementary.complexes import adjoint

__all__ = ['Dagger']

class Dagger(adjoint):
    def __new__(cls, arg, evaluate: bool = True): ...
    def __mul__(self, other): ...
