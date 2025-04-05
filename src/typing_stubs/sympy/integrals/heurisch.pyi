from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic, sympify as sympify
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.core.traversal import iterfreeargs as iterfreeargs
from sympy.functions import Ei as Ei, asin as asin, asinh as asinh, atan as atan, besseli as besseli, besselj as besselj, besselk as besselk, bessely as bessely, cos as cos, cosh as cosh, cot as cot, coth as coth, erf as erf, erfi as erfi, exp as exp, hankel1 as hankel1, hankel2 as hankel2, jn as jn, li as li, log as log, sin as sin, sinh as sinh, sqrt as sqrt, tan as tan, tanh as tanh, yn as yn
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, im as im, re as re, sign as sign
from sympy.functions.elementary.exponential import LambertW as LambertW
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.integrals.integrals import integrate as integrate
from sympy.logic.boolalg import And as And, Or as Or
from sympy.polys import PolynomialError as PolynomialError, cancel as cancel, factor_list as factor_list, gcd as gcd, lcm as lcm, quo as quo
from sympy.polys.constructor import construct_domain as construct_domain
from sympy.polys.monomials import itermonomials as itermonomials
from sympy.polys.polyroots import root_factors as root_factors
from sympy.polys.rings import PolyRing as PolyRing
from sympy.polys.solvers import solve_lin_sys as solve_lin_sys
from sympy.simplify.radsimp import collect as collect
from sympy.utilities.iterables import uniq as uniq

def components(f, x): ...
def heurisch_wrapper(f, x, rewrite: bool = False, hints: Incomplete | None = None, mappings: Incomplete | None = None, retries: int = 3, degree_offset: int = 0, unnecessary_permutations: Incomplete | None = None, _try_heurisch: Incomplete | None = None): ...

class BesselTable:
    table: Incomplete
    n: Incomplete
    z: Incomplete
    def __init__(self) -> None: ...
    def diffs(t, f, n, z): ...
    def has(t, f): ...

class DiffCache:
    cache: Incomplete
    x: Incomplete
    def __init__(self, x) -> None: ...
    def get_diff(self, f): ...

def heurisch(f, x, rewrite: bool = False, hints: Incomplete | None = None, mappings: Incomplete | None = None, retries: int = 3, degree_offset: int = 0, unnecessary_permutations: Incomplete | None = None, _try_heurisch: Incomplete | None = None): ...
