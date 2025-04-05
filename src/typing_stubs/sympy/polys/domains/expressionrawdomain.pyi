from _typeshed import Incomplete
from sympy.core import Expr
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain

__all__ = ['ExpressionRawDomain']

class ExpressionRawDomain(Field, CharacteristicZero, SimpleDomain):
    is_SymbolicRawDomain: bool
    is_EXRAW: bool
    dtype = Expr
    zero: Incomplete
    one: Incomplete
    rep: str
    has_assoc_Ring: bool
    has_assoc_Field: bool
    def __init__(self) -> None: ...
    @classmethod
    def new(self, a): ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def convert_from(self, a, K): ...
    def get_field(self): ...
    def sum(self, items): ...
