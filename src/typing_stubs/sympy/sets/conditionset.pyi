from .contains import Contains as Contains
from .sets import FiniteSet as FiniteSet, Set as Set, SetKind as SetKind, Union as Union
from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import BadSignatureError as BadSignatureError, Lambda as Lambda
from sympy.core.logic import fuzzy_bool as fuzzy_bool
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.logic.boolalg import And as And, as_Boolean as as_Boolean
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import flatten as flatten, has_dups as has_dups, sift as sift

adummy: Incomplete

class ConditionSet(Set):
    def __new__(cls, sym, condition, base_set=...): ...
    sym: Incomplete
    condition: Incomplete
    base_set: Incomplete
    @property
    def free_symbols(self): ...
    @property
    def bound_symbols(self): ...
    def as_relational(self, other): ...
