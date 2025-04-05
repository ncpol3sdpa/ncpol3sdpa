from .codeprinter import CodePrinter as CodePrinter
from .precedence import precedence as precedence
from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.mod import Mod as Mod

class AbstractPythonCodePrinter(CodePrinter):
    printmethod: str
    language: str
    reserved_words: Incomplete
    modules: Incomplete
    tab: str
    standard: Incomplete
    module_imports: Incomplete
    known_functions: Incomplete
    known_constants: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class ArrayPrinter: ...
class PythonCodePrinter(AbstractPythonCodePrinter): ...

def pycode(expr, **settings): ...

class MpmathPrinter(PythonCodePrinter):
    printmethod: str
    language: str

class SymPyPrinter(AbstractPythonCodePrinter):
    language: str
