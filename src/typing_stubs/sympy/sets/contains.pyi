from .sets import Set as Set
from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.parameters import global_parameters as global_parameters
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.sympify import sympify as sympify
from sympy.logic.boolalg import Boolean as Boolean
from sympy.utilities.misc import func_name as func_name

class Contains(Boolean):
    def __new__(cls, x, s, evaluate: Incomplete | None = None): ...
    @property
    def binary_symbols(self): ...
    def as_set(self): ...
