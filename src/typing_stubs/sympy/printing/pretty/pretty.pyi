from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import Function as Function
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Number as Number, Rational as Rational
from sympy.core.power import Pow as Pow
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import SympifyError as SympifyError
from sympy.printing.conventions import requires_partial as requires_partial
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence, precedence_traditional as precedence_traditional
from sympy.printing.pretty.pretty_symbology import U as U, annotated as annotated, center_pad as center_pad, greek_unicode as greek_unicode, hobj as hobj, is_subscriptable_in_unicode as is_subscriptable_in_unicode, pretty_atom as pretty_atom, pretty_symbol as pretty_symbol, pretty_try_use_unicode as pretty_try_use_unicode, pretty_use_unicode as pretty_use_unicode, vobj as vobj, xobj as xobj, xsym as xsym
from sympy.printing.pretty.stringpict import prettyForm as prettyForm, stringPict as stringPict
from sympy.printing.printer import Printer as Printer, print_function as print_function
from sympy.printing.str import sstr as sstr
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import has_variety as has_variety

pprint_use_unicode = pretty_use_unicode
pprint_try_use_unicode = pretty_try_use_unicode

class PrettyPrinter(Printer):
    printmethod: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def emptyPrinter(self, expr): ...
    def doprint(self, expr): ...
    def join(self, delimiter, args): ...

def pretty(expr, **settings): ...
def pretty_print(expr, **kwargs) -> None: ...
pprint = pretty_print

def pager_print(expr, **settings) -> None: ...
