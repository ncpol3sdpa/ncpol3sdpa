from _typeshed import Incomplete
from sympy.calculus.accumulationbounds import AccumulationBounds as AccumulationBounds
from sympy.core.add import Add as Add
from sympy.core.function import PoleError as PoleError
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import factorial as factorial, subfactorial as subfactorial
from sympy.functions.combinatorial.numbers import fibonacci as fibonacci
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.series.limits import Limit as Limit

def difference_delta(expr, n: Incomplete | None = None, step: int = 1): ...
def dominant(expr, n): ...
def limit_seq(expr, n: Incomplete | None = None, trials: int = 5): ...
