from _typeshed import Incomplete
from sympy.assumptions import Predicate as Predicate
from sympy.multipledispatch import Dispatcher as Dispatcher

class IntegerPredicate(Predicate):
    name: str
    handler: Incomplete

class NonIntegerPredicate(Predicate):
    name: str
    handler: Incomplete

class RationalPredicate(Predicate):
    name: str
    handler: Incomplete

class IrrationalPredicate(Predicate):
    name: str
    handler: Incomplete

class RealPredicate(Predicate):
    name: str
    handler: Incomplete

class ExtendedRealPredicate(Predicate):
    name: str
    handler: Incomplete

class HermitianPredicate(Predicate):
    name: str
    handler: Incomplete

class ComplexPredicate(Predicate):
    name: str
    handler: Incomplete

class ImaginaryPredicate(Predicate):
    name: str
    handler: Incomplete

class AntihermitianPredicate(Predicate):
    name: str
    handler: Incomplete

class AlgebraicPredicate(Predicate):
    name: str
    AlgebraicHandler: Incomplete

class TranscendentalPredicate(Predicate):
    name: str
    handler: Incomplete
