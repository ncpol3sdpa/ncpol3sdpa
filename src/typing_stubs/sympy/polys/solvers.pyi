from _typeshed import Incomplete
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.sympify import sympify as sympify
from sympy.matrices.dense import MutableDenseMatrix as MutableDenseMatrix
from sympy.polys.domainmatrix import DomainMatrix as DomainMatrix
from sympy.polys.domains import EX as EX, QQ as QQ, ZZ as ZZ
from sympy.polys.polyerrors import NotInvertible as NotInvertible
from sympy.polys.rings import sring as sring
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import connected_components as connected_components

class PolyNonlinearError(Exception): ...

class RawMatrix(MutableDenseMatrix):
    ring: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

def eqs_to_matrix(eqs_coeffs, eqs_rhs, gens, domain): ...
def sympy_eqs_to_ring(eqs, symbols): ...
def solve_lin_sys(eqs, ring, _raw: bool = True): ...
