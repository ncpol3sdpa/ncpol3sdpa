from _typeshed import Incomplete
from sympy.external.gmpy import MPQ
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain

__all__ = ['RationalField']

class RationalField(Field, CharacteristicZero, SimpleDomain):
    rep: str
    alias: str
    is_RationalField: bool
    is_QQ: bool
    is_Numerical: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    dtype = MPQ
    zero: Incomplete
    one: Incomplete
    tp: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def get_ring(self): ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def algebraic_field(self, *extension, alias: Incomplete | None = None): ...
    def from_AlgebraicField(K1, a, K0): ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_GaussianRationalField(K1, a, K0): ...
    def from_RealField(K1, a, K0): ...
    def exquo(self, a, b): ...
    def quo(self, a, b): ...
    def rem(self, a, b): ...
    def div(self, a, b): ...
    def numer(self, a): ...
    def denom(self, a): ...
    def is_square(self, a): ...
    def exsqrt(self, a): ...
