from _typeshed import Incomplete
from sympy.core.numbers import equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence
from sympy.sets.fancysets import Range as Range

known_functions: Incomplete
reserved_words: Incomplete

class RCodePrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    reserved_words: Incomplete
    def __init__(self, settings={}) -> None: ...
    def indent_code(self, code): ...

def rcode(expr, assign_to: Incomplete | None = None, **settings): ...
def print_rcode(expr, **settings) -> None: ...
