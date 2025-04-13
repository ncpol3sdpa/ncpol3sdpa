from .basic import Basic as Basic
from .parameters import global_parameters as global_parameters
from _typeshed import Incomplete
from sympy.core.random import choice as choice
from sympy.utilities.iterables import iterable as iterable
from typing import Any, Callable

class SympifyError(ValueError):
    expr: Incomplete
    base_exc: Incomplete
    def __init__(self, expr, base_exc: Incomplete | None = None) -> None: ...

converter: dict[type[Any], Callable[[Any], Basic]]

class CantSympify: ...

def sympify(a, locals: Incomplete | None = None, convert_xor: bool = True, strict: bool = False, rational: bool = False, evaluate: Incomplete | None = None): ...
def kernS(s): ...
