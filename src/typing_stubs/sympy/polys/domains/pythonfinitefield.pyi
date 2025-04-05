from sympy.polys.domains.finitefield import FiniteField

__all__ = ['PythonFiniteField']

class PythonFiniteField(FiniteField):
    alias: str
    def __init__(self, mod, symmetric: bool = True) -> None: ...
