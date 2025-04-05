from _typeshed import Incomplete
from sympy.core.numbers import NumberSymbol
from sympy.core.singleton import Singleton

__all__ = ['hbar', 'HBar']

class HBar(NumberSymbol, metaclass=Singleton):
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: bool

hbar: Incomplete
