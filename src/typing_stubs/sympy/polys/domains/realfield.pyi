from _typeshed import Incomplete
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain

__all__ = ['RealField']

class RealField(Field, CharacteristicZero, SimpleDomain):
    rep: str
    is_RealField: bool
    is_RR: bool
    is_Exact: bool
    is_Numerical: bool
    is_PID: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    @property
    def has_default_precision(self): ...
    @property
    def precision(self): ...
    @property
    def dps(self): ...
    @property
    def tolerance(self): ...
    zero: Incomplete
    one: Incomplete
    def __init__(self, prec=..., dps: Incomplete | None = None, tol: Incomplete | None = None) -> None: ...
    @property
    def tp(self): ...
    def dtype(self, arg): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def to_sympy(self, element): ...
    def from_sympy(self, expr): ...
    def from_ZZ(self, element, base): ...
    def from_ZZ_python(self, element, base): ...
    def from_ZZ_gmpy(self, element, base): ...
    def from_QQ(self, element, base): ...
    def from_QQ_python(self, element, base): ...
    def from_QQ_gmpy(self, element, base): ...
    def from_AlgebraicField(self, element, base): ...
    def from_RealField(self, element, base): ...
    def from_ComplexField(self, element, base): ...
    def to_rational(self, element, limit: bool = True): ...
    def get_ring(self): ...
    def get_exact(self): ...
    def gcd(self, a, b): ...
    def lcm(self, a, b): ...
    def almosteq(self, a, b, tolerance: Incomplete | None = None): ...
    def is_square(self, a): ...
    def exsqrt(self, a): ...
