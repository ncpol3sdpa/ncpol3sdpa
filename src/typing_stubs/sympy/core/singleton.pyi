from .basic import Basic as Basic
from .core import Registry as Registry
from .sympify import sympify as sympify
from _typeshed import Incomplete

class SingletonRegistry(Registry):
    __call__: Incomplete
    def __init__(self) -> None: ...
    def register(self, cls) -> None: ...
    def __getattr__(self, name): ...

S: Incomplete

class Singleton(type):
    def __init__(cls, *args, **kwargs) -> None: ...
