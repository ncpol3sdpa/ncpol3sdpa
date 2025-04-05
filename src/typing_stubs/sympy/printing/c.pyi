from _typeshed import Incomplete
from sympy.codegen.ast import Assignment as Assignment, Declaration as Declaration, Pointer as Pointer, Type as Type, Variable as Variable, bool_ as bool_, complex128 as complex128, complex64 as complex64, complex_ as complex_, float32 as float32, float64 as float64, float80 as float80, int16 as int16, int32 as int32, int64 as int64, int8 as int8, intc as intc, integer as integer, none as none, pointer_const as pointer_const, real as real, uint16 as uint16, uint32 as uint32, uint64 as uint64, uint8 as uint8, untyped as untyped, value_const as value_const
from sympy.core import S as S
from sympy.core.numbers import Float as Float, equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter, ccode as ccode, print_ccode as print_ccode, requires as requires
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence
from sympy.sets.fancysets import Range as Range
from typing import Any

known_functions_C89: Incomplete
known_functions_C99: Incomplete
reserved_words: Incomplete
reserved_words_c99: Incomplete

def get_math_macros(): ...

class C89CodePrinter(CodePrinter):
    printmethod: str
    language: str
    standard: str
    reserved_words: Incomplete
    type_aliases: Incomplete
    type_mappings: dict[Type, Any]
    type_headers: Incomplete
    type_macros: dict[Type, tuple[str, ...]]
    type_func_suffixes: Incomplete
    type_literal_suffixes: Incomplete
    type_math_macro_suffixes: Incomplete
    math_macros: Incomplete
    known_functions: Incomplete
    headers: Incomplete
    libraries: Incomplete
    macros: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def indent_code(self, code): ...

class C99CodePrinter(C89CodePrinter):
    standard: str
    reserved_words: Incomplete
    type_mappings: Incomplete
    type_headers: Incomplete

class C11CodePrinter(C99CodePrinter): ...

c_code_printers: Incomplete
