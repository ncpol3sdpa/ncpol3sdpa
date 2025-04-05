from _typeshed import Incomplete
from sympy.core import Add as Add, Dummy as Dummy, Expr as Expr, Mul as Mul, S as S, Symbol as Symbol
from sympy.core.assumptions import check_assumptions as check_assumptions
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, UndefinedFunction as UndefinedFunction, expand as expand, expand_func as expand_func, expand_log as expand_log, expand_mul as expand_mul, expand_power_exp as expand_power_exp, nfloat as nfloat
from sympy.core.intfunc import ilcm as ilcm, integer_log as integer_log
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.numbers import Float as Float, Rational as Rational
from sympy.core.power import Pow as Pow
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.functions import Abs as Abs, LambertW as LambertW, acos as acos, arg as arg, asin as asin, atan as atan, atan2 as atan2, cos as cos, exp as exp, im as im, log as log, re as re, sin as sin, sqrt as sqrt, tan as tan
from sympy.functions.combinatorial.factorials import binomial as binomial
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction
from sympy.functions.elementary.piecewise import Piecewise as Piecewise, piecewise_fold as piecewise_fold
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction
from sympy.integrals.integrals import Integral as Integral
from sympy.logic.boolalg import And as And, BooleanAtom as BooleanAtom
from sympy.matrices import Matrix as Matrix, zeros as zeros
from sympy.matrices.exceptions import NonInvertibleMatrixError as NonInvertibleMatrixError
from sympy.ntheory.factor_ import divisors as divisors
from sympy.polys import Poly as Poly, cancel as cancel, factor as factor, roots as roots
from sympy.polys.polyerrors import GeneratorsNeeded as GeneratorsNeeded, PolynomialError as PolynomialError
from sympy.polys.polytools import gcd as gcd
from sympy.polys.solvers import solve_lin_sys as solve_lin_sys, sympy_eqs_to_ring as sympy_eqs_to_ring
from sympy.simplify import collect as collect, denom as denom, fraction as fraction, logcombine as logcombine, nsimplify as nsimplify, posify as posify, powdenest as powdenest, powsimp as powsimp, separatevars as separatevars, simplify as simplify, sqrtdenest as sqrtdenest
from sympy.simplify.fu import TR1 as TR1, TR10 as TR10, TR11 as TR11, TR2i as TR2i
from sympy.simplify.sqrtdenest import sqrt_depth as sqrt_depth
from sympy.solvers.bivariate import bivariate_type as bivariate_type
from sympy.solvers.polysys import solve_poly_system as solve_poly_system
from sympy.strategies.rl import rebuild as rebuild
from sympy.utilities.decorator import conserve_mpmath_dps as conserve_mpmath_dps
from sympy.utilities.iterables import connected_components as connected_components, flatten as flatten, generate_bell as generate_bell, is_sequence as is_sequence, iterable as iterable, sift as sift, subsets as subsets, uniq as uniq
from sympy.utilities.lambdify import lambdify as lambdify
from sympy.utilities.misc import debugf as debugf, filldedent as filldedent

def recast_to_symbols(eqs, symbols): ...
def denoms(eq, *symbols): ...
def checksol(f, symbol, sol: Incomplete | None = None, **flags): ...
def solve(f, *symbols, **flags): ...
def solve_linear(lhs, rhs: int = 0, symbols=[], exclude=[]): ...
def minsolve_linear_system(system, *symbols, **flags): ...
def solve_linear_system(system, *symbols, **flags): ...
def solve_undetermined_coeffs(equ, coeffs, *syms, **flags): ...
def solve_linear_system_LU(matrix, syms): ...
def det_perm(M): ...
def det_minor(M): ...
def det_quick(M, method: Incomplete | None = None): ...
def inv_quick(M): ...

multi_inverses: Incomplete

def nsolve(*args, dict: bool = False, **kwargs): ...
def unrad(eq, *syms, **flags): ...
