from sympy.core.function import Add as Add, ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import log as log
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin

class cosm1(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...

class powm1(Function):
    nargs: int
    def fdiff(self, argindex: int = 1): ...
