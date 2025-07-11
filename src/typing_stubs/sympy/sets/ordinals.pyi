from _typeshed import Incomplete
from sympy.core import Basic as Basic, Integer as Integer

class OmegaPower(Basic):
    def __new__(cls, a, b): ...
    @property
    def exp(self): ...
    @property
    def mult(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __lt__(self, other): ...

class Ordinal(Basic):
    def __new__(cls, *terms): ...
    @property
    def terms(self): ...
    @property
    def leading_term(self): ...
    @property
    def trailing_term(self): ...
    @property
    def is_successor_ordinal(self): ...
    @property
    def is_limit_ordinal(self): ...
    @property
    def degree(self): ...
    @classmethod
    def convert(cls, integer_value): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __pow__(self, other): ...

class OrdinalZero(Ordinal): ...

class OrdinalOmega(Ordinal):
    def __new__(cls): ...
    @property
    def terms(self): ...

ord0: Incomplete
omega: Incomplete
