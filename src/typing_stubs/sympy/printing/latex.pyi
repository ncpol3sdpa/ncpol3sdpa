from _typeshed import Incomplete
from sympy.core import Add as Add, Expr as Expr, Float as Float, Mod as Mod, Mul as Mul, Number as Number, S as S, Symbol as Symbol
from sympy.core.alphabets import greeks as greeks
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function
from sympy.core.operations import AssocOp as AssocOp
from sympy.core.power import Pow as Pow
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.sympify import SympifyError as SympifyError
from sympy.logic.boolalg import BooleanFalse as BooleanFalse, BooleanTrue as BooleanTrue, true as true
from sympy.printing.conventions import requires_partial as requires_partial, split_super_sub as split_super_sub
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence, precedence_traditional as precedence_traditional
from sympy.printing.printer import Printer as Printer, print_function as print_function
from sympy.tensor.array import NDimArray as NDimArray
from sympy.utilities.iterables import has_variety as has_variety, sift as sift
from sympy.vector.basisdependent import BasisDependent as BasisDependent
from typing import Callable

accepted_latex_functions: Incomplete
tex_greek_dictionary: Incomplete
other_symbols: Incomplete
modifier_dict: dict[str, Callable[[str], str]]
greek_letters_set: Incomplete

def latex_escape(s: str) -> str: ...

class LatexPrinter(Printer):
    printmethod: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def parenthesize(self, item, level, is_neg: bool = False, strict: bool = False) -> str: ...
    def parenthesize_super(self, s): ...
    def doprint(self, expr) -> str: ...
    def emptyPrinter(self, expr): ...

def translate(s: str) -> str: ...
def latex(expr, **settings): ...
def print_latex(expr, **settings) -> None: ...
def multiline_latex(lhs, rhs, terms_per_line: int = 1, environment: str = 'align*', use_dots: bool = False, **settings): ...
