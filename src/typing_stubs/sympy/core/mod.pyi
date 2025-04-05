from .add import Add as Add
from .exprtools import gcd_terms as gcd_terms
from .function import Function as Function
from .kind import NumberKind as NumberKind
from .logic import fuzzy_and as fuzzy_and, fuzzy_not as fuzzy_not
from .mul import Mul as Mul
from .numbers import equal_valued as equal_valued
from .singleton import S as S

class Mod(Function):
    kind = NumberKind
    @classmethod
    def eval(cls, p, q): ...
