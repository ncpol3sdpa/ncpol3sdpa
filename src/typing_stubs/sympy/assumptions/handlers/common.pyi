from ..predicates.common import CommutativePredicate as CommutativePredicate, IsTruePredicate as IsTruePredicate
from sympy.assumptions import AppliedPredicate as AppliedPredicate, Q as Q, ask as ask
from sympy.core import Basic as Basic, Symbol as Symbol
from sympy.core.numbers import NaN as NaN, Number as Number
from sympy.logic.boolalg import And as And, BooleanFalse as BooleanFalse, BooleanTrue as BooleanTrue, Equivalent as Equivalent, Implies as Implies, Not as Not, Or as Or, conjuncts as conjuncts
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning

class AskHandler:
    def __new__(cls, *args, **kwargs): ...

class CommonHandler(AskHandler):
    @staticmethod
    def AlwaysTrue(expr, assumptions): ...
    @staticmethod
    def AlwaysFalse(expr, assumptions): ...
    @staticmethod
    def AlwaysNone(expr, assumptions) -> None: ...
    NaN = AlwaysFalse

def _(expr, assumptions): ...
def test_closed_group(expr, assumptions, key): ...
