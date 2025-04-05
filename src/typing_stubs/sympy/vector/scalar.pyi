from _typeshed import Incomplete
from sympy.core import AtomicExpr as AtomicExpr, S as S, Symbol as Symbol
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE
from sympy.printing.pretty.stringpict import prettyForm as prettyForm

class BaseScalar(AtomicExpr):
    def __new__(cls, index, system, pretty_str: Incomplete | None = None, latex_str: Incomplete | None = None): ...
    is_commutative: bool
    is_symbol: bool
    @property
    def free_symbols(self): ...
    precedence: Incomplete
    @property
    def system(self): ...
