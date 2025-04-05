from ..predicates.calculus import FinitePredicate as FinitePredicate, InfinitePredicate as InfinitePredicate, NegativeInfinitePredicate as NegativeInfinitePredicate, PositiveInfinitePredicate as PositiveInfinitePredicate
from sympy.assumptions import Q as Q, ask as ask
from sympy.core import Add as Add, Mul as Mul, Pow as Pow, Symbol as Symbol
from sympy.core.numbers import ComplexInfinity as ComplexInfinity, E as E, Exp1 as Exp1, GoldenRatio as GoldenRatio, ImaginaryUnit as ImaginaryUnit, Infinity as Infinity, NaN as NaN, NegativeInfinity as NegativeInfinity, Number as Number, Pi as Pi, TribonacciConstant as TribonacciConstant
from sympy.functions import cos as cos, exp as exp, log as log, sign as sign, sin as sin
from sympy.logic.boolalg import conjuncts as conjuncts

def _(expr, assumptions): ...
