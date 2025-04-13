from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.numbers import Integer as Integer, IntegerConstant as IntegerConstant, equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence

known_functions: Incomplete
number_symbols: Incomplete
spec_relational_ops: Incomplete
not_supported_symbol: Incomplete

class MapleCodePrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

def maple_code(expr, assign_to: Incomplete | None = None, **settings): ...
def print_maple_code(expr, **settings) -> None: ...
