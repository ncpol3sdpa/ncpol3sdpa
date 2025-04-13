from sympy.core import S as S, diff as diff, oo as oo
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.relational import Eq as Eq
from sympy.functions.elementary.complexes import im as im
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.special.delta_functions import Heaviside as Heaviside

class SingularityFunction(Function):
    is_real: bool
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, variable, offset, exponent): ...
