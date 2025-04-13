from sympy.core import Add as Add, Function as Function, Mul as Mul, Pow as Pow, S as S
from sympy.core.function import expand_func as expand_func
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy
from sympy.functions import gamma as gamma, sin as sin, sqrt as sqrt
from sympy.polys import cancel as cancel, factor as factor
from sympy.utilities.iterables import sift as sift, uniq as uniq

def gammasimp(expr): ...

class _rf(Function):
    @classmethod
    def eval(cls, a, b): ...
