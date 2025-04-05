from .binrel import BinaryRelation
from _typeshed import Incomplete

__all__ = ['EqualityPredicate', 'UnequalityPredicate', 'StrictGreaterThanPredicate', 'GreaterThanPredicate', 'StrictLessThanPredicate', 'LessThanPredicate']

class EqualityPredicate(BinaryRelation):
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class UnequalityPredicate(BinaryRelation):
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class StrictGreaterThanPredicate(BinaryRelation):
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class GreaterThanPredicate(BinaryRelation):
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class StrictLessThanPredicate(BinaryRelation):
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class LessThanPredicate(BinaryRelation):
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...
