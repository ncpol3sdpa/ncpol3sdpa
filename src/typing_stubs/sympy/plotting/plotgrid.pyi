from _typeshed import Incomplete
from sympy.external import import_module as import_module

__doctest_requires__: Incomplete

class PlotGrid:
    matplotlib: Incomplete
    nrows: Incomplete
    ncolumns: Incomplete
    args: Incomplete
    size: Incomplete
    def __init__(self, nrows, ncolumns, *args, show: bool = True, size: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def fig(self): ...
    def close(self) -> None: ...
    def show(self) -> None: ...
    def save(self, path) -> None: ...
