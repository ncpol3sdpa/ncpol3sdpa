from .c import C89CodePrinter as C89CodePrinter, C99CodePrinter as C99CodePrinter
from .codeprinter import requires as requires
from _typeshed import Incomplete
from sympy.codegen.ast import Type as Type, none as none
from sympy.printing.codeprinter import cxxcode as cxxcode

reserved: Incomplete

class _CXXCodePrinterBase:
    printmethod: str
    language: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class CXX98CodePrinter(_CXXCodePrinterBase, C89CodePrinter):
    standard: str
    reserved_words: Incomplete

class CXX11CodePrinter(_CXXCodePrinterBase, C99CodePrinter):
    standard: str
    reserved_words: Incomplete
    type_mappings: Incomplete

class CXX17CodePrinter(_CXXCodePrinterBase, C99CodePrinter):
    standard: str
    reserved_words: Incomplete

cxx_code_printers: Incomplete
