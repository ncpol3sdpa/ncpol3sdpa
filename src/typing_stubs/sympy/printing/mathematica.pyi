from _typeshed import Incomplete
from sympy.core import Basic as Basic, Expr as Expr, Float as Float
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import precedence as precedence

known_functions: Incomplete

class MCodePrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings={}) -> None: ...

def mathematica_code(expr, **settings): ...
