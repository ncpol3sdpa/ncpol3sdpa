from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.numbers import equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence

known_functions: Incomplete

class JavascriptCodePrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings={}) -> None: ...
    def indent_code(self, code): ...

def jscode(expr, assign_to: Incomplete | None = None, **settings): ...
def print_jscode(expr, **settings) -> None: ...
