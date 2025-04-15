from _typeshed import Incomplete
from sympy.concrete import product as product
from sympy.core.add import Add as Add
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, Rational as Rational
from sympy.core.relational import Equality as Equality
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.core.sympify import sympify as sympify
from sympy.functions import FallingFactorial as FallingFactorial, RisingFactorial as RisingFactorial, binomial as binomial, factorial as factorial
from sympy.matrices import Matrix as Matrix, casoratian as casoratian
from sympy.polys import Poly as Poly, gcd as gcd, lcm as lcm, quo as quo, resultant as resultant, roots as roots
from sympy.simplify import hypersimilar as hypersimilar, hypersimp as hypersimp, simplify as simplify
from sympy.solvers import solve as solve, solve_undetermined_coeffs as solve_undetermined_coeffs
from sympy.utilities.iterables import numbered_symbols as numbered_symbols

def rsolve_poly(coeffs, f, n, shift: int = 0, **hints): ...
def rsolve_ratio(coeffs, f, n, **hints): ...
def rsolve_hyper(coeffs, f, n, **hints): ...
def rsolve(f, y, init: Incomplete | None = None): ...
