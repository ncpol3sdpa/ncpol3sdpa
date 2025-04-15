from sympy.core import Basic as Basic, Expr as Expr
from sympy.core.numbers import oo as oo
from sympy.core.symbol import symbols as symbols
from sympy.multipledispatch import Dispatcher as Dispatcher
from sympy.sets.setexpr import set_mul as set_mul
from sympy.sets.sets import Interval as Interval, Set as Set

def _(x, y) -> None: ...
