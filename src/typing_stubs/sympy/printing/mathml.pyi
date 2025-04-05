from _typeshed import Incomplete
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.sympify import sympify as sympify
from sympy.printing.conventions import requires_partial as requires_partial, split_super_sub as split_super_sub
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, PRECEDENCE_TRADITIONAL as PRECEDENCE_TRADITIONAL, precedence_traditional as precedence_traditional
from sympy.printing.pretty.pretty_symbology import greek_unicode as greek_unicode
from sympy.printing.printer import Printer as Printer, print_function as print_function

class MathMLPrinterBase(Printer):
    dom: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def doprint(self, expr): ...

class MathMLContentPrinter(MathMLPrinterBase):
    printmethod: str
    def mathml_tag(self, e): ...

class MathMLPresentationPrinter(MathMLPrinterBase):
    printmethod: str
    def mathml_tag(self, e): ...
    def parenthesize(self, item, level, strict: bool = False): ...

def mathml(expr, printer: str = 'content', **settings): ...
def print_mathml(expr, printer: str = 'content', **settings) -> None: ...
MathMLPrinter = MathMLContentPrinter
