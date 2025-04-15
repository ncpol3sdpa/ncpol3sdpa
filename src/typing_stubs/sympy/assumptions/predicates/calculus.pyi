from _typeshed import Incomplete
from sympy.assumptions import Predicate as Predicate
from sympy.multipledispatch import Dispatcher as Dispatcher

class FinitePredicate(Predicate):
    name: str
    handler: Incomplete

class InfinitePredicate(Predicate):
    name: str
    handler: Incomplete

class PositiveInfinitePredicate(Predicate):
    name: str
    handler: Incomplete

class NegativeInfinitePredicate(Predicate):
    name: str
    handler: Incomplete
