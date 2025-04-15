from _typeshed import Incomplete
from sympy.calculus.util import continuous_domain as continuous_domain, function_range as function_range, periodicity as periodicity
from sympy.core import Add as Add, Basic as Basic, Dummy as Dummy, Expr as Expr, Mul as Mul, Pow as Pow, S as S, Wild as Wild, pi as pi
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import AppliedUndef as AppliedUndef, Lambda as Lambda, expand_complex as expand_complex, expand_log as expand_log, expand_trig as expand_trig, nfloat as nfloat
from sympy.core.intfunc import integer_log as integer_log
from sympy.core.mod import Mod as Mod
from sympy.core.numbers import I as I, Number as Number, Rational as Rational, oo as oo
from sympy.core.relational import Eq as Eq, Ne as Ne, Relational as Relational
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.functions import Piecewise as Piecewise, acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan, cos as cos, cot as cot, csc as csc, exp as exp, log as log, piecewise_fold as piecewise_fold, sec as sec, sin as sin, tan as tan
from sympy.functions.combinatorial.numbers import totient as totient
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, im as im, re as re
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction, acosh as acosh, acoth as acoth, acsch as acsch, asech as asech, asinh as asinh, atanh as atanh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.miscellaneous import real_root as real_root
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction
from sympy.logic.boolalg import And as And, BooleanTrue as BooleanTrue
from sympy.matrices import Matrix as Matrix, MatrixBase as MatrixBase, zeros as zeros
from sympy.ntheory.factor_ import divisors as divisors
from sympy.ntheory.residue_ntheory import discrete_log as discrete_log, nthroot_mod as nthroot_mod
from sympy.polys import Poly as Poly, PolynomialError as PolynomialError, RootOf as RootOf, degree as degree, factor as factor, gcd as gcd, lcm as lcm, roots as roots, together as together
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.polys.polyroots import UnsolvableFactorError as UnsolvableFactorError
from sympy.polys.polytools import groebner as groebner, invert as invert, poly as poly
from sympy.polys.solvers import PolyNonlinearError as PolyNonlinearError, solve_lin_sys as solve_lin_sys, sympy_eqs_to_ring as sympy_eqs_to_ring
from sympy.sets import Complement as Complement, ConditionSet as ConditionSet, Contains as Contains, FiniteSet as FiniteSet, ImageSet as ImageSet, Intersection as Intersection, Interval as Interval, Union as Union, imageset as imageset
from sympy.sets.sets import ProductSet as ProductSet, Set as Set
from sympy.simplify import logcombine as logcombine, powdenest as powdenest
from sympy.simplify.simplify import fraction as fraction, nsimplify as nsimplify, simplify as simplify, trigsimp as trigsimp
from sympy.solvers.polysys import solve_poly_system as solve_poly_system
from sympy.solvers.solvers import checksol as checksol, denoms as denoms, recast_to_symbols as recast_to_symbols, unrad as unrad
from sympy.utilities import filldedent as filldedent
from sympy.utilities.iterables import has_dups as has_dups, is_sequence as is_sequence, iterable as iterable, numbered_symbols as numbered_symbols

class NonlinearError(ValueError): ...

invert_complex: Incomplete

def invert_real(f_x, y, x): ...
def domain_check(f, symbol, p): ...

class _SolveTrig1Error(Exception): ...

def solve_decomposition(f, symbol, domain): ...
def solveset(f, symbol: Incomplete | None = None, domain=...): ...
def solveset_real(f, symbol): ...
def solveset_complex(f, symbol): ...
def solvify(f, symbol, domain): ...
def linear_coeffs(eq, *syms, dict: bool = False): ...
def linear_eq_to_matrix(equations, *symbols): ...
def linsolve(system, *symbols): ...
def substitution(system, symbols, result=[{}], known_symbols=[], exclude=[], all_symbols: Incomplete | None = None): ...
def nonlinsolve(system, *symbols): ...
