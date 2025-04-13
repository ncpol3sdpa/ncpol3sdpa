from ..predicates.ntheory import CompositePredicate as CompositePredicate, EvenPredicate as EvenPredicate, OddPredicate as OddPredicate, PrimePredicate as PrimePredicate
from sympy.assumptions import Q as Q, ask as ask
from sympy.core import Add as Add, Basic as Basic, Expr as Expr, Float as Float, Mul as Mul, Pow as Pow, S as S
from sympy.core.numbers import ImaginaryUnit as ImaginaryUnit, Infinity as Infinity, Integer as Integer, NaN as NaN, NegativeInfinity as NegativeInfinity, NumberSymbol as NumberSymbol, Rational as Rational, int_valued as int_valued
from sympy.functions import Abs as Abs, im as im, re as re
from sympy.multipledispatch import MDNotImplementedError as MDNotImplementedError
from sympy.ntheory import isprime as isprime

def _(expr, assumptions): ...
