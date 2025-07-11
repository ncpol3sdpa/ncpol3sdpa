from _typeshed import Incomplete
from sympy.core.basic import Atom as Atom
from sympy.core.expr import Expr as Expr
from sympy.core.numbers import Integer as Integer, int_valued as int_valued
from sympy.core.parameters import global_parameters as global_parameters
from sympy.matrices import zeros as zeros
from sympy.multipledispatch import dispatch as dispatch
from sympy.polys.polytools import lcm as lcm
from sympy.printing.repr import srepr as srepr
from sympy.utilities.iterables import flatten as flatten, has_dups as has_dups, has_variety as has_variety, is_sequence as is_sequence, minlex as minlex, runs as runs
from sympy.utilities.misc import as_int as as_int

class Cycle(dict):
    def __missing__(self, arg): ...
    def __iter__(self): ...
    def __call__(self, *other): ...
    def list(self, size: Incomplete | None = None): ...
    def __init__(self, *args) -> None: ...
    @property
    def size(self): ...
    def copy(self): ...

class Permutation(Atom):
    is_Permutation: bool
    def __new__(cls, *args, size: Incomplete | None = None, **kwargs): ...
    def copy(self): ...
    def __getnewargs__(self): ...
    @property
    def array_form(self): ...
    def list(self, size: Incomplete | None = None): ...
    @property
    def cyclic_form(self): ...
    @property
    def full_cyclic_form(self): ...
    @property
    def size(self): ...
    def support(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    @staticmethod
    def rmul(*args): ...
    @classmethod
    def rmul_with_af(cls, *args): ...
    def mul_inv(self, other): ...
    def __rmul__(self, other): ...
    def __mul__(self, other): ...
    def commutes_with(self, other): ...
    def __pow__(self, n): ...
    def __rxor__(self, i): ...
    def __xor__(self, h): ...
    def transpositions(self): ...
    @classmethod
    def from_sequence(self, i, key: Incomplete | None = None): ...
    def __invert__(self): ...
    def __iter__(self): ...
    def __call__(self, *i): ...
    def atoms(self): ...
    def apply(self, i): ...
    def next_lex(self): ...
    @classmethod
    def unrank_nonlex(self, n, r): ...
    def rank_nonlex(self, inv_perm: Incomplete | None = None): ...
    def next_nonlex(self): ...
    def rank(self): ...
    @property
    def cardinality(self): ...
    def parity(self): ...
    @property
    def is_even(self): ...
    @property
    def is_odd(self): ...
    @property
    def is_Singleton(self): ...
    @property
    def is_Empty(self): ...
    @property
    def is_identity(self): ...
    @property
    def is_Identity(self): ...
    def ascents(self): ...
    def descents(self): ...
    def max(self) -> int: ...
    def min(self) -> int: ...
    def inversions(self): ...
    def commutator(self, x): ...
    def signature(self): ...
    def order(self): ...
    def length(self): ...
    @property
    def cycle_structure(self): ...
    @property
    def cycles(self): ...
    def index(self): ...
    def runs(self): ...
    def inversion_vector(self): ...
    def rank_trotterjohnson(self): ...
    @classmethod
    def unrank_trotterjohnson(cls, size, rank): ...
    def next_trotterjohnson(self): ...
    def get_precedence_matrix(self): ...
    def get_precedence_distance(self, other): ...
    def get_adjacency_matrix(self): ...
    def get_adjacency_distance(self, other): ...
    def get_positional_distance(self, other): ...
    @classmethod
    def josephus(cls, m, n, s: int = 1): ...
    @classmethod
    def from_inversion_vector(cls, inversion): ...
    @classmethod
    def random(cls, n): ...
    @classmethod
    def unrank_lex(cls, size, rank): ...
    def resize(self, n): ...
    print_cyclic: Incomplete
Perm = Permutation

class AppliedPermutation(Expr):
    def __new__(cls, perm, x, evaluate: Incomplete | None = None): ...
