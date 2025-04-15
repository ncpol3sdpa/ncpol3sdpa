from sympy.core import Dummy as Dummy, Mod as Mod, S as S, sympify as sympify
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, PoleError as PoleError
from sympy.core.logic import fuzzy_and as fuzzy_and
from sympy.core.numbers import I as I, Integer as Integer, pi as pi
from sympy.core.relational import Eq as Eq
from sympy.ntheory import sieve as sieve
from sympy.ntheory.residue_ntheory import binomial_mod as binomial_mod
from sympy.polys.polytools import Poly as Poly

class CombinatorialFunction(Function): ...

class factorial(CombinatorialFunction):
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, n): ...

class MultiFactorial(CombinatorialFunction): ...

class subfactorial(CombinatorialFunction):
    @classmethod
    def eval(cls, arg): ...

class factorial2(CombinatorialFunction):
    @classmethod
    def eval(cls, arg): ...

class RisingFactorial(CombinatorialFunction):
    @classmethod
    def eval(cls, x, k): ...

class FallingFactorial(CombinatorialFunction):
    @classmethod
    def eval(cls, x, k): ...
rf = RisingFactorial
ff = FallingFactorial

class binomial(CombinatorialFunction):
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, n, k): ...
