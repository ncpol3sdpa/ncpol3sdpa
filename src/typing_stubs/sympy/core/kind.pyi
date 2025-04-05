from .cache import cacheit as cacheit
from _typeshed import Incomplete
from sympy.multipledispatch.dispatcher import Dispatcher as Dispatcher, RaiseNotImplementedError as RaiseNotImplementedError, ambiguity_register_error_ignore_dup as ambiguity_register_error_ignore_dup, ambiguity_warn as ambiguity_warn, str_signature as str_signature

class KindMeta(type):
    def __new__(cls, clsname, bases, dct): ...

class Kind(metaclass=KindMeta):
    def __new__(cls, *args): ...

class _UndefinedKind(Kind):
    def __new__(cls): ...

UndefinedKind: Incomplete

class _NumberKind(Kind):
    def __new__(cls): ...

NumberKind: Incomplete

class _BooleanKind(Kind):
    def __new__(cls): ...

BooleanKind: Incomplete

class KindDispatcher:
    name: Incomplete
    doc: Incomplete
    commutative: Incomplete
    def __init__(self, name, commutative: bool = False, doc: Incomplete | None = None) -> None: ...
    def register(self, *types, **kwargs): ...
    def __call__(self, *args, **kwargs): ...
    def dispatch_kinds(self, kinds, **kwargs): ...
    @property
    def __doc__(self): ...
