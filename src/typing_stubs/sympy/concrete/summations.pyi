from .expr_with_intlimits import ExprWithIntLimits as ExprWithIntLimits
from .expr_with_limits import AddWithLimits as AddWithLimits
from .gosper import gosper_sum as gosper_sum
from sympy.calculus.accumulationbounds import AccumulationBounds as AccumulationBounds
from sympy.calculus.singularities import is_decreasing as is_decreasing
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import Derivative as Derivative, expand as expand
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Float as Float
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild, symbols as symbols
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.combinatorial.numbers import bernoulli as bernoulli, harmonic as harmonic
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import cot as cot, csc as csc
from sympy.functions.special.hyper import hyper as hyper
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.functions.special.zeta_functions import zeta as zeta
from sympy.integrals.integrals import Integral as Integral
from sympy.logic.boolalg import And as And
from sympy.polys.partfrac import apart as apart
from sympy.polys.polyerrors import PolificationFailed as PolificationFailed, PolynomialError as PolynomialError
from sympy.polys.polytools import Poly as Poly, factor as factor, parallel_poly_from_expr as parallel_poly_from_expr
from sympy.polys.rationaltools import together as together
from sympy.series.limitseq import limit_seq as limit_seq
from sympy.series.order import O as O
from sympy.series.residues import residue as residue
from sympy.sets.sets import FiniteSet as FiniteSet, Interval as Interval
from sympy.utilities.iterables import sift as sift

class Sum(AddWithLimits, ExprWithIntLimits):
    limits: tuple[tuple[Symbol, Expr, Expr]]
    def __new__(cls, function, *symbols, **assumptions): ...
    def doit(self, **hints): ...
    def eval_zeta_function(self, f, limits): ...
    def is_convergent(self): ...
    def is_absolutely_convergent(self): ...
    def euler_maclaurin(self, m: int = 0, n: int = 0, eps: int = 0, eval_integral: bool = True): ...
    def reverse_order(self, *indices): ...

def summation(f, *symbols, **kwargs): ...
def telescopic_direct(L, R, n, limits): ...
def telescopic(L, R, limits): ...
def eval_sum(f, limits): ...
def eval_sum_direct(expr, limits): ...
def eval_sum_symbolic(f, limits): ...
def eval_sum_hyper(f, i_a_b): ...
def eval_sum_residue(f, i_a_b): ...
