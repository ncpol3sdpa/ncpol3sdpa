from ..predicates.sets import AlgebraicPredicate as AlgebraicPredicate, AntihermitianPredicate as AntihermitianPredicate, ComplexPredicate as ComplexPredicate, ExtendedRealPredicate as ExtendedRealPredicate, HermitianPredicate as HermitianPredicate, ImaginaryPredicate as ImaginaryPredicate, IntegerPredicate as IntegerPredicate, IrrationalPredicate as IrrationalPredicate, RationalPredicate as RationalPredicate, RealPredicate as RealPredicate
from .common import test_closed_group as test_closed_group
from sympy.assumptions import Q as Q, ask as ask
from sympy.core import Add as Add, Basic as Basic, Expr as Expr, Mul as Mul, Pow as Pow, S as S
from sympy.core.logic import fuzzy_bool as fuzzy_bool
from sympy.core.numbers import AlgebraicNumber as AlgebraicNumber, ComplexInfinity as ComplexInfinity, E as E, Exp1 as Exp1, Float as Float, GoldenRatio as GoldenRatio, I as I, ImaginaryUnit as ImaginaryUnit, Infinity as Infinity, Integer as Integer, NaN as NaN, NegativeInfinity as NegativeInfinity, Number as Number, NumberSymbol as NumberSymbol, Pi as Pi, Rational as Rational, TribonacciConstant as TribonacciConstant, pi as pi
from sympy.core.relational import Eq as Eq
from sympy.functions import Abs as Abs, acos as acos, acot as acot, asin as asin, atan as atan, cos as cos, cot as cot, exp as exp, im as im, log as log, re as re, sin as sin, tan as tan
from sympy.functions.elementary.complexes import conjugate as conjugate
from sympy.matrices import Determinant as Determinant, MatrixBase as MatrixBase, Trace as Trace
from sympy.matrices.expressions.matexpr import MatrixElement as MatrixElement
from sympy.multipledispatch import MDNotImplementedError as MDNotImplementedError

def _(expr, assumptions): ...
