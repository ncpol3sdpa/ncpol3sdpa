from _typeshed import Incomplete
from sympy.assumptions import Predicate as Predicate
from sympy.multipledispatch import Dispatcher as Dispatcher

class PrimePredicate(Predicate):
    name: str
    handler: Incomplete

class CompositePredicate(Predicate):
    name: str
    handler: Incomplete

class EvenPredicate(Predicate):
    name: str
    handler: Incomplete

class OddPredicate(Predicate):
    name: str
    handler: Incomplete
