from sympy.core import S as S, diff as diff
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.functions.elementary.complexes import im as im, sign as sign
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.polys.polyerrors import PolynomialError as PolynomialError
from sympy.polys.polyroots import roots as roots
from sympy.utilities.misc import filldedent as filldedent

class DiracDelta(Function):
    is_real: bool
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg, k=...): ...
    def is_simple(self, x): ...

class Heaviside(Function):
    is_real: bool
    def fdiff(self, argindex: int = 1): ...
    def __new__(cls, arg, H0=..., **options): ...
    @property
    def pargs(self): ...
    @classmethod
    def eval(cls, arg, H0=...): ...
