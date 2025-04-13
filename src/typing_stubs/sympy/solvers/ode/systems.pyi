from _typeshed import Incomplete
from sympy.core import Add as Add, Mul as Mul, S as S
from sympy.core.containers import Tuple as Tuple
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, Subs as Subs, expand as expand, expand_mul as expand_mul
from sympy.core.numbers import I as I
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions import Piecewise as Piecewise, cos as cos, exp as exp, im as im, log as log, piecewise_fold as piecewise_fold, re as re, sin as sin, sqrt as sqrt
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.integrals.integrals import Integral as Integral, integrate as integrate
from sympy.matrices import Matrix as Matrix, MatrixBase as MatrixBase, NonSquareMatrixError as NonSquareMatrixError, eye as eye, zeros as zeros
from sympy.polys import Poly as Poly, together as together
from sympy.sets.sets import FiniteSet as FiniteSet
from sympy.simplify import collect as collect, radsimp as radsimp, signsimp as signsimp
from sympy.simplify.powsimp import powdenest as powdenest, powsimp as powsimp
from sympy.simplify.ratsimp import ratsimp as ratsimp
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers.deutils import ode_order as ode_order
from sympy.solvers.solveset import NonlinearError as NonlinearError, solveset as solveset
from sympy.utilities.iterables import connected_components as connected_components, iterable as iterable, strongly_connected_components as strongly_connected_components
from sympy.utilities.misc import filldedent as filldedent

class ODEOrderError(ValueError): ...
class ODENonlinearError(NonlinearError): ...

def simpsol(sol, wrt1, wrt2, doit: bool = True): ...
def linodesolve_type(A, t, b: Incomplete | None = None): ...
def linear_ode_to_matrix(eqs, funcs, t, order): ...
def matrix_exp(A, t): ...
def matrix_exp_jordan_form(A, t): ...
def linodesolve(A, t, b: Incomplete | None = None, B: Incomplete | None = None, type: str = 'auto', doit: bool = False, tau: Incomplete | None = None): ...
def canonical_odes(eqs, funcs, t): ...
def dsolve_system(eqs, funcs: Incomplete | None = None, t: Incomplete | None = None, ics: Incomplete | None = None, doit: bool = False, simplify: bool = True): ...
