from _typeshed import Incomplete
from sympy.core import Float as Float, Lambda as Lambda, Rational as Rational, S as S
from sympy.core.numbers import equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter

known_functions: Incomplete
reserved_words: Incomplete

class RustCodePrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    reserved_words: Incomplete
    def __init__(self, settings={}) -> None: ...
    def indent_code(self, code): ...

def rust_code(expr, assign_to: Incomplete | None = None, **settings): ...
def print_rust_code(expr, **settings) -> None: ...
