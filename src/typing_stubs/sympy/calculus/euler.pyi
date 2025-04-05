from sympy.core.function import Derivative as Derivative, Function as Function, diff as diff
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.utilities.iterables import iterable as iterable

def euler_equations(L, funcs=(), vars=()): ...
