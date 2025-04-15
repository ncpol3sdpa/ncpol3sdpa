from .repr import ReprPrinter as ReprPrinter
from .str import StrPrinter as StrPrinter
from _typeshed import Incomplete

STRPRINT: Incomplete

class PythonPrinter(ReprPrinter, StrPrinter):
    symbols: Incomplete
    functions: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

def python(expr, **settings): ...
def print_python(expr, **settings) -> None: ...
