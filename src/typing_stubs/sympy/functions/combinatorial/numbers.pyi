from _typeshed import Incomplete
from sympy.core import Add as Add, Dummy as Dummy, S as S, Symbol as Symbol
from sympy.core.cache import cacheit as cacheit
from sympy.core.containers import Dict as Dict
from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, expand_mul as expand_mul
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import E as E, I as I, Integer as Integer, Rational as Rational, oo as oo, pi as pi
from sympy.core.relational import Eq as Eq, is_gt as is_gt, is_le as is_le, is_lt as is_lt
from sympy.external.gmpy import SYMPY_INTS as SYMPY_INTS, jacobi as jacobi, kronecker as kronecker, lcm as lcm, legendre as legendre, remove as remove
from sympy.functions.combinatorial.factorials import binomial as binomial, factorial as factorial, subfactorial as subfactorial
from sympy.functions.elementary.exponential import log as log
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.ntheory.factor_ import factorint as factorint, find_carmichael_numbers_in_range as find_carmichael_numbers_in_range, find_first_n_carmichaels as find_first_n_carmichaels, is_carmichael as is_carmichael
from sympy.ntheory.primetest import is_square as is_square, isprime as isprime
from sympy.polys.appellseqs import bernoulli_poly as bernoulli_poly, euler_poly as euler_poly, genocchi_poly as genocchi_poly
from sympy.polys.polytools import cancel as cancel
from sympy.utilities.enumerative import MultisetPartitionTraverser as MultisetPartitionTraverser
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import iterable as iterable, multiset as multiset, multiset_derangements as multiset_derangements
from sympy.utilities.memoization import recurrence_memo as recurrence_memo
from sympy.utilities.misc import as_int as as_int

class carmichael(Function):
    @staticmethod
    def is_perfect_square(n): ...
    @staticmethod
    def divides(p, n): ...
    @staticmethod
    def is_prime(n): ...
    @staticmethod
    def is_carmichael(n): ...
    @staticmethod
    def find_carmichael_numbers_in_range(x, y): ...
    @staticmethod
    def find_first_n_carmichaels(n): ...

class fibonacci(Function):
    @classmethod
    def eval(cls, n, sym: Incomplete | None = None): ...

class lucas(Function):
    @classmethod
    def eval(cls, n): ...

class tribonacci(Function):
    @classmethod
    def eval(cls, n, sym: Incomplete | None = None): ...

class bernoulli(Function):
    args: tuple[Integer]
    @classmethod
    def eval(cls, n, x: Incomplete | None = None): ...

class bell(Function):
    @classmethod
    def eval(cls, n, k_sym: Incomplete | None = None, symbols: Incomplete | None = None): ...

class harmonic(Function):
    @classmethod
    def eval(cls, n, m: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...

class euler(Function):
    @classmethod
    def eval(cls, n, x: Incomplete | None = None): ...

class catalan(Function):
    @classmethod
    def eval(cls, n): ...
    def fdiff(self, argindex: int = 1): ...

class genocchi(Function):
    @classmethod
    def eval(cls, n, x: Incomplete | None = None): ...

class andre(Function):
    @classmethod
    def eval(cls, n): ...

class partition(Function):
    is_integer: bool
    is_nonnegative: bool
    @classmethod
    def eval(cls, n): ...

class divisor_sigma(Function):
    is_integer: bool
    is_positive: bool
    @classmethod
    def eval(cls, n, k=...): ...

class udivisor_sigma(Function):
    is_integer: bool
    is_positive: bool
    @classmethod
    def eval(cls, n, k=...): ...

class legendre_symbol(Function):
    is_integer: bool
    is_prime: bool
    @classmethod
    def eval(cls, a, p): ...

class jacobi_symbol(Function):
    is_integer: bool
    is_prime: bool
    @classmethod
    def eval(cls, m, n): ...

class kronecker_symbol(Function):
    is_integer: bool
    is_prime: bool
    @classmethod
    def eval(cls, a, n): ...

class mobius(Function):
    is_integer: bool
    is_prime: bool
    @classmethod
    def eval(cls, n): ...

class primenu(Function):
    is_integer: bool
    is_nonnegative: bool
    @classmethod
    def eval(cls, n): ...

class primeomega(Function):
    is_integer: bool
    is_nonnegative: bool
    @classmethod
    def eval(cls, n): ...

class totient(Function):
    is_integer: bool
    is_positive: bool
    @classmethod
    def eval(cls, n): ...

class reduced_totient(Function):
    is_integer: bool
    is_positive: bool
    @classmethod
    def eval(cls, n): ...

class primepi(Function):
    is_integer: bool
    is_nonnegative: bool
    @classmethod
    def eval(cls, n): ...

class _MultisetHistogram(tuple): ...

def nP(n, k: Incomplete | None = None, replacement: bool = False): ...
def nC(n, k: Incomplete | None = None, replacement: bool = False): ...
def stirling(n, k, d: Incomplete | None = None, kind: int = 2, signed: bool = False): ...
def nT(n, k: Incomplete | None = None): ...

class motzkin(Function):
    @staticmethod
    def is_motzkin(n): ...
    @staticmethod
    def find_motzkin_numbers_in_range(x, y): ...
    @staticmethod
    def find_first_n_motzkins(n): ...
    @classmethod
    def eval(cls, n): ...

def nD(i: Incomplete | None = None, brute: Incomplete | None = None, *, n: Incomplete | None = None, m: Incomplete | None = None): ...
