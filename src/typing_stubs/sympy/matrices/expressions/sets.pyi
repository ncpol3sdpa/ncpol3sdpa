from .matexpr import MatrixExpr as MatrixExpr
from sympy.core.assumptions import check_assumptions as check_assumptions
from sympy.core.kind import NumberKind as NumberKind
from sympy.core.logic import fuzzy_and as fuzzy_and
from sympy.matrices.kind import MatrixKind as MatrixKind
from sympy.sets.sets import Set as Set, SetKind as SetKind

class MatrixSet(Set):
    is_empty: bool
    def __new__(cls, n, m, set): ...
    @property
    def shape(self): ...
    @property
    def set(self): ...
