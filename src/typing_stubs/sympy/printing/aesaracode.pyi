from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.printing.printer import Printer as Printer
from sympy.utilities.iterables import is_sequence as is_sequence
from typing import Any

aesara: Incomplete
aes: Incomplete
aet: Incomplete
true_divide: Incomplete
mapping: Incomplete

class AesaraPrinter(Printer):
    printmethod: str
    cache: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def emptyPrinter(self, expr): ...
    def doprint(self, expr, dtypes: Incomplete | None = None, broadcastables: Incomplete | None = None): ...

global_cache: dict[Any, Any]

def aesara_code(expr, cache: Incomplete | None = None, **kwargs): ...
def dim_handling(inputs, dim: Incomplete | None = None, dims: Incomplete | None = None, broadcastables: Incomplete | None = None): ...
def aesara_function(inputs, outputs, scalar: bool = False, *, dim: Incomplete | None = None, dims: Incomplete | None = None, broadcastables: Incomplete | None = None, **kwargs): ...
