from sympy.core.function import Add as Add, ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions.elementary.exponential import exp as exp, log as log

class logaddexp(Function):
    nargs: int
    def __new__(cls, *args): ...
    def fdiff(self, argindex: int = 1): ...

class logaddexp2(Function):
    nargs: int
    def __new__(cls, *args): ...
    def fdiff(self, argindex: int = 1): ...
