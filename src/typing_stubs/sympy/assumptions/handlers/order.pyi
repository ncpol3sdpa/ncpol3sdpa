from ..predicates.order import ExtendedNegativePredicate as ExtendedNegativePredicate, ExtendedNonNegativePredicate as ExtendedNonNegativePredicate, ExtendedNonPositivePredicate as ExtendedNonPositivePredicate, ExtendedNonZeroPredicate as ExtendedNonZeroPredicate, ExtendedPositivePredicate as ExtendedPositivePredicate, NegativePredicate as NegativePredicate, NonNegativePredicate as NonNegativePredicate, NonPositivePredicate as NonPositivePredicate, NonZeroPredicate as NonZeroPredicate, PositivePredicate as PositivePredicate, ZeroPredicate as ZeroPredicate
from sympy.assumptions import Q as Q, ask as ask
from sympy.core import Add as Add, Basic as Basic, Expr as Expr, Mul as Mul, Pow as Pow
from sympy.core.logic import fuzzy_and as fuzzy_and, fuzzy_not as fuzzy_not, fuzzy_or as fuzzy_or
from sympy.core.numbers import E as E, I as I, ImaginaryUnit as ImaginaryUnit, NaN as NaN, pi as pi
from sympy.functions import Abs as Abs, acos as acos, acot as acot, asin as asin, atan as atan, exp as exp, factorial as factorial, log as log
from sympy.matrices import Determinant as Determinant, Trace as Trace
from sympy.matrices.expressions.matexpr import MatrixElement as MatrixElement
from sympy.multipledispatch import MDNotImplementedError as MDNotImplementedError

def _(expr, assumptions): ...
