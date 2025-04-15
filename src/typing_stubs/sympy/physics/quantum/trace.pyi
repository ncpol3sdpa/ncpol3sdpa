from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.sympify import sympify as sympify
from sympy.matrices import Matrix as Matrix

class Tr(Expr):
    def __new__(cls, *args): ...
    @property
    def kind(self): ...
    def doit(self, **hints): ...
    @property
    def is_number(self): ...
    def permute(self, pos): ...
