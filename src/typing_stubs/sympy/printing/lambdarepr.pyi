from .numpy import NumPyPrinter as NumPyPrinter
from .pycode import MpmathPrinter as MpmathPrinter, PythonCodePrinter as PythonCodePrinter

__all__ = ['PythonCodePrinter', 'MpmathPrinter', 'NumPyPrinter', 'LambdaPrinter', 'NumPyPrinter', 'IntervalPrinter', 'lambdarepr']

class LambdaPrinter(PythonCodePrinter):
    printmethod: str

class NumExprPrinter(LambdaPrinter):
    printmethod: str
    module: str
    def blacklisted(self, expr) -> None: ...
    def doprint(self, expr): ...

class IntervalPrinter(MpmathPrinter, LambdaPrinter): ...

def lambdarepr(expr, **settings): ...
