from sympy.core.containers import Tuple as Tuple
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.integrals.integrals import Integral as Integral
from sympy.tensor import Indexed as Indexed

class IndexedIntegral(Integral):
    def __new__(cls, function, *limits, **assumptions): ...
    def doit(self): ...
