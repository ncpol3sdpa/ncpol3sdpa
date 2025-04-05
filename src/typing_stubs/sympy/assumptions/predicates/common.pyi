from _typeshed import Incomplete
from sympy.assumptions import AppliedPredicate as AppliedPredicate, Predicate as Predicate, Q as Q
from sympy.core.relational import Eq as Eq, Ge as Ge, Gt as Gt, Le as Le, Lt as Lt, Ne as Ne
from sympy.multipledispatch import Dispatcher as Dispatcher

class CommutativePredicate(Predicate):
    name: str
    handler: Incomplete

binrelpreds: Incomplete

class IsTruePredicate(Predicate):
    name: str
    handler: Incomplete
    def __call__(self, arg): ...
