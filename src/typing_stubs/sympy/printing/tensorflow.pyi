from _typeshed import Incomplete
from sympy.codegen.cfunctions import Sqrt as Sqrt
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.external import import_module as import_module
from sympy.external.importtools import version_tuple as version_tuple
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE
from sympy.printing.pycode import AbstractPythonCodePrinter as AbstractPythonCodePrinter, ArrayPrinter as ArrayPrinter

tensorflow: Incomplete

class TensorflowPrinter(ArrayPrinter, AbstractPythonCodePrinter):
    printmethod: str
    mapping: Incomplete
    tensorflow_version: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

def tensorflow_code(expr, **settings): ...
