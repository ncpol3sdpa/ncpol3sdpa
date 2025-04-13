from sympy.core import Add as Add, Dummy as Dummy, symbols as symbols
from sympy.core.numbers import Rational as Rational
from sympy.polys import ComputationFailed as ComputationFailed, Poly as Poly, cancel as cancel, parallel_poly_from_expr as parallel_poly_from_expr, reduced as reduced
from sympy.polys.monomials import Monomial as Monomial, monomial_div as monomial_div
from sympy.polys.polyerrors import DomainError as DomainError, PolificationFailed as PolificationFailed
from sympy.utilities.misc import debug as debug, debugf as debugf

def ratsimp(expr): ...
def ratsimpmodprime(expr, G, *gens, quick: bool = True, polynomial: bool = False, **args): ...
