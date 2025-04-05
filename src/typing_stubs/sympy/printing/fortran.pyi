from _typeshed import Incomplete
from sympy.codegen.ast import Assignment as Assignment, Declaration as Declaration, Pointer as Pointer, bool_ as bool_, complex128 as complex128, complex64 as complex64, complex_ as complex_, float32 as float32, float64 as float64, float80 as float80, int16 as int16, int32 as int32, int64 as int64, int8 as int8, intc as intc, integer as integer, none as none, real as real, stderr as stderr, stdout as stdout, value_const as value_const
from sympy.codegen.fnodes import allocatable as allocatable, cmplx as cmplx, dsign as dsign, elemental as elemental, intent_in as intent_in, intent_inout as intent_inout, intent_out as intent_out, isign as isign, literal_dp as literal_dp, merge as merge, pure as pure
from sympy.core import Add as Add, Float as Float, N as N, S as S, Symbol as Symbol
from sympy.core.function import Function as Function
from sympy.core.numbers import equal_valued as equal_valued
from sympy.core.relational import Eq as Eq
from sympy.printing.codeprinter import CodePrinter as CodePrinter, fcode as fcode, print_fcode as print_fcode
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence
from sympy.printing.printer import printer_context as printer_context
from sympy.sets import Range as Range

known_functions: Incomplete

class FCodePrinter(CodePrinter):
    printmethod: str
    language: str
    type_aliases: Incomplete
    type_mappings: Incomplete
    type_modules: Incomplete
    mangled_symbols: Incomplete
    used_name: Incomplete
    known_functions: Incomplete
    module_uses: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def indent_code(self, code): ...
