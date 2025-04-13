from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import AppliedUndef as AppliedUndef, UndefinedFunction as UndefinedFunction
from sympy.core.mul import Mul as Mul
from sympy.core.relational import Equality as Equality, Relational as Relational
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.piecewise import Piecewise as Piecewise, piecewise_fold as piecewise_fold
from sympy.logic.boolalg import BooleanFunction as BooleanFunction
from sympy.matrices.matrixbase import MatrixBase as MatrixBase
from sympy.sets.fancysets import Range as Range
from sympy.sets.sets import Interval as Interval, Set as Set
from sympy.tensor.indexed import Idx as Idx
from sympy.utilities import flatten as flatten
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence, sift as sift

class ExprWithLimits(Expr):
    def __new__(cls, function, *symbols, **assumptions): ...
    @property
    def function(self): ...
    @property
    def kind(self): ...
    @property
    def limits(self): ...
    @property
    def variables(self): ...
    @property
    def bound_symbols(self): ...
    @property
    def free_symbols(self): ...
    @property
    def is_number(self): ...
    @property
    def has_finite_limits(self): ...
    @property
    def has_reversed_limits(self): ...

class AddWithLimits(ExprWithLimits):
    def __new__(cls, function, *symbols, **assumptions): ...
