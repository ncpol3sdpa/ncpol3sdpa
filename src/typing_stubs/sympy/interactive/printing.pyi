from _typeshed import Incomplete
from sympy.external.importtools import version_tuple as version_tuple
from sympy.printing.defaults import Printable as Printable
from sympy.printing.preview import preview as preview
from sympy.utilities.misc import debug as debug

NO_GLOBAL: bool

def init_printing(pretty_print: bool = True, order: Incomplete | None = None, use_unicode: Incomplete | None = None, use_latex: Incomplete | None = None, wrap_line: Incomplete | None = None, num_columns: Incomplete | None = None, no_global: bool = False, ip: Incomplete | None = None, euler: bool = False, forecolor: Incomplete | None = None, backcolor: str = 'Transparent', fontsize: str = '10pt', latex_mode: str = 'plain', print_builtin: bool = True, str_printer: Incomplete | None = None, pretty_printer: Incomplete | None = None, latex_printer: Incomplete | None = None, scale: float = 1.0, **settings): ...
