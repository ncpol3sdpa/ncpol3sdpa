from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, expand_mul as expand_mul
from sympy.core.numbers import I as I, Integer as Integer, pi as pi
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.numbers import bernoulli as bernoulli, factorial as factorial, genocchi as genocchi, harmonic as harmonic
from sympy.functions.elementary.complexes import Abs as Abs, polar_lift as polar_lift, re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, exp_polar as exp_polar, log as log
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.polys.polytools import Poly as Poly

class lerchphi(Function):
    def fdiff(self, argindex: int = 1): ...

class polylog(Function):
    @classmethod
    def eval(cls, s, z): ...
    def fdiff(self, argindex: int = 1): ...

class zeta(Function):
    @classmethod
    def eval(cls, s, a: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...

class dirichlet_eta(Function):
    @classmethod
    def eval(cls, s, a: Incomplete | None = None): ...

class riemann_xi(Function):
    @classmethod
    def eval(cls, s): ...

class stieltjes(Function):
    @classmethod
    def eval(cls, n, a: Incomplete | None = None): ...
