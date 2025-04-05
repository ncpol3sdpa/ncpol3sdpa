from .codeprinter import CodePrinter as CodePrinter
from .pycode import ArrayPrinter as ArrayPrinter, PythonCodePrinter as PythonCodePrinter
from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.function import Lambda as Lambda
from sympy.core.power import Pow as Pow

class NumPyPrinter(ArrayPrinter, PythonCodePrinter):
    language: Incomplete
    printmethod: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class SciPyPrinter(NumPyPrinter):
    language: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class CuPyPrinter(NumPyPrinter):
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class JaxPrinter(NumPyPrinter):
    printmethod: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...
