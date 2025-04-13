from _typeshed import Incomplete
from sympy.core import Basic as Basic, S as S
from sympy.core.function import Lambda as Lambda
from sympy.core.numbers import equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import precedence as precedence

known_functions: Incomplete

class GLSLPrinter(CodePrinter):
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings={}) -> None: ...
    def indent_code(self, code): ...

def glsl_code(expr, assign_to: Incomplete | None = None, **settings): ...
def print_glsl(expr, **settings) -> None: ...
