from sympy.core import Pow as Pow, S as S
from sympy.core.function import expand as expand
from sympy.core.relational import Eq as Eq
from sympy.core.symbol import Symbol as Symbol, Wild as Wild
from sympy.functions import exp as exp, hyper as hyper, sqrt as sqrt
from sympy.integrals import Integral as Integral
from sympy.polys import gcd as gcd, roots as roots
from sympy.polys.polytools import cancel as cancel, factor as factor
from sympy.simplify import collect as collect, logcombine as logcombine, simplify as simplify
from sympy.simplify.powsimp import powdenest as powdenest
from sympy.solvers.ode.ode import get_numbered_constants as get_numbered_constants

def match_2nd_hypergeometric(eq, func): ...
def equivalence_hypergeometric(A, B, func): ...
def match_2nd_2F1_hypergeometric(I, k, sing_point, func): ...
def equivalence(max_num_pow, dem_pow): ...
def get_sol_2F1_hypergeometric(eq, func, match_object): ...
