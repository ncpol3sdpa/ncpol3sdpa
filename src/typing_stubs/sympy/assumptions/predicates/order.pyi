from _typeshed import Incomplete
from sympy.assumptions import Predicate as Predicate
from sympy.multipledispatch import Dispatcher as Dispatcher

class NegativePredicate(Predicate):
    name: str
    handler: Incomplete

class NonNegativePredicate(Predicate):
    name: str
    handler: Incomplete

class NonZeroPredicate(Predicate):
    name: str
    handler: Incomplete

class ZeroPredicate(Predicate):
    name: str
    handler: Incomplete

class NonPositivePredicate(Predicate):
    name: str
    handler: Incomplete

class PositivePredicate(Predicate):
    name: str
    handler: Incomplete

class ExtendedPositivePredicate(Predicate):
    name: str
    handler: Incomplete

class ExtendedNegativePredicate(Predicate):
    name: str
    handler: Incomplete

class ExtendedNonZeroPredicate(Predicate):
    name: str
    handler: Incomplete

class ExtendedNonPositivePredicate(Predicate):
    name: str
    handler: Incomplete

class ExtendedNonNegativePredicate(Predicate):
    name: str
    handler: Incomplete
