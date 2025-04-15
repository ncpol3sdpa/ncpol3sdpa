from _typeshed import Incomplete
from sympy.core import Mul as Mul, Pow as Pow, Rational as Rational, S as S
from sympy.core.numbers import equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence

known_fcns_src1: Incomplete
known_fcns_src2: Incomplete

class OctaveCodePrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings={}) -> None: ...
    def indent_code(self, code): ...

def octave_code(expr, assign_to: Incomplete | None = None, **settings): ...
def print_octave_code(expr, **settings) -> None: ...
