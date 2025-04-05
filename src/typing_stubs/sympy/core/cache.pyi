from _typeshed import Incomplete
from typing import Callable

class _cache(list):
    def print_cache(self) -> None: ...
    def clear_cache(self) -> None: ...

CACHE: Incomplete
print_cache: Incomplete
clear_cache: Incomplete
USE_CACHE: Incomplete
scs: Incomplete
SYMPY_CACHE_SIZE: Incomplete
cacheit: Incomplete

def cached_property(func): ...
def lazy_function(module: str, name: str) -> Callable: ...
