from _typeshed import Incomplete
from collections.abc import Generator
from sympy.core.function import expand_mul as expand_mul
from threading import local

class DotProdSimpState(local):
    state: Incomplete
    def __init__(self) -> None: ...

def dotprodsimp(x) -> Generator[None]: ...
