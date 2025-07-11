from _typeshed import Incomplete
from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.polys.domains.ring import Ring
from sympy.polys.polyclasses import DMF, DMP

__all__ = ['PolynomialRingBase', 'GlobalPolynomialRing', 'PolynomialRing']

class PolynomialRingBase(Ring, CompositeDomain):
    has_assoc_Ring: bool
    has_assoc_Field: bool
    default_order: str
    ngens: Incomplete
    zero: Incomplete
    one: Incomplete
    domain: Incomplete
    symbols: Incomplete
    order: Incomplete
    def __init__(self, dom, *gens, **opts) -> None: ...
    def set_domain(self, dom): ...
    def new(self, element): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_RealField(K1, a, K0): ...
    def from_AlgebraicField(K1, a, K0): ...
    def from_PolynomialRing(K1, a, K0): ...
    def from_GlobalPolynomialRing(K1, a, K0): ...
    def get_field(self): ...
    def poly_ring(self, *gens) -> None: ...
    def frac_field(self, *gens) -> None: ...
    def revert(self, a): ...
    def gcdex(self, a, b): ...
    def gcd(self, a, b): ...
    def lcm(self, a, b): ...
    def factorial(self, a): ...
    def free_module(self, rank): ...

class GlobalPolynomialRing(PolynomialRingBase):
    is_PolynomialRing: bool
    is_Poly: bool
    dtype = DMP
    def new(self, element): ...
    def from_FractionField(K1, a, K0): ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def is_positive(self, a): ...
    def is_negative(self, a): ...
    def is_nonpositive(self, a): ...
    def is_nonnegative(self, a): ...

class GeneralizedPolynomialRing(PolynomialRingBase):
    dtype = DMF
    def new(self, a): ...
    def __contains__(self, a) -> bool: ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def exquo(self, a, b): ...
    def from_FractionField(K1, a, K0): ...

def PolynomialRing(dom, *gens, **opts): ...
