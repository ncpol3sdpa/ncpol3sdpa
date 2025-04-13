from _typeshed import Incomplete
from sympy.codegen.fnodes import Module as Module
from sympy.core.symbol import Dummy as Dummy
from sympy.printing.fortran import FCodePrinter as FCodePrinter

def render_as_module(definitions, name, declarations=(), printer_settings: Incomplete | None = None): ...
