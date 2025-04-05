from .gruntz import gruntz as gruntz
from sympy.calculus.accumulationbounds import AccumBounds as AccumBounds
from sympy.core import Add as Add, Expr as Expr, Mul as Mul, PoleError as PoleError, S as S, Symbol as Symbol, sympify as sympify
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.numbers import Float as Float
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, re as re, sign as sign
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.polys import PolynomialError as PolynomialError, factor as factor
from sympy.series.order import Order as Order

def limit(e, z, z0, dir: str = '+'): ...
def heuristics(e, z, z0, dir): ...

class Limit(Expr):
    def __new__(cls, e, z, z0, dir: str = '+'): ...
    @property
    def free_symbols(self): ...
    def pow_heuristics(self, e): ...
    def doit(self, **hints): ...
