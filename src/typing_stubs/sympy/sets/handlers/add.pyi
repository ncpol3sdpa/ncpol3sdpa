from sympy.core import Basic as Basic, Expr as Expr
from sympy.core.numbers import Infinity as Infinity, NegativeInfinity as NegativeInfinity, oo as oo
from sympy.core.singleton import S as S
from sympy.multipledispatch import Dispatcher as Dispatcher
from sympy.sets import FiniteSet as FiniteSet, Interval as Interval

def _(x, y) -> None: ...
