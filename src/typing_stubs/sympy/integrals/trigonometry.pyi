from .integrals import integrate as integrate
from sympy.core import Dummy as Dummy, Integer as Integer, Ne as Ne, Rational as Rational, S as S, Wild as Wild, cacheit as cacheit
from sympy.functions import Abs as Abs, Piecewise as Piecewise, binomial as binomial, cos as cos, sin as sin

def trigintegrate(f, x, conds: str = 'piecewise'): ...
