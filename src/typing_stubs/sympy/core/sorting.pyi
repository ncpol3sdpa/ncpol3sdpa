from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['default_sort_key', 'ordered']

def default_sort_key(item, order: Incomplete | None = None): ...
def ordered(seq, keys: Incomplete | None = None, default: bool = True, warn: bool = False) -> Generator[Incomplete, Incomplete]: ...
