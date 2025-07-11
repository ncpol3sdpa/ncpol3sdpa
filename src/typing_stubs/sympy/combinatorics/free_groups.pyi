from _typeshed import Incomplete
from sympy.core.expr import Expr
from sympy.core.sympify import CantSympify
from sympy.printing.defaults import DefaultPrinting

__all__ = ['free_group', 'xfree_group', 'vfree_group']

def free_group(symbols): ...
def xfree_group(symbols): ...
def vfree_group(symbols): ...

class FreeGroup(DefaultPrinting):
    is_associative: bool
    is_group: bool
    is_FreeGroup: bool
    is_PermutationGroup: bool
    relators: list[Expr]
    def __new__(cls, symbols): ...
    def clone(self, symbols: Incomplete | None = None): ...
    def __contains__(self, i) -> bool: ...
    def __hash__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __eq__(self, other): ...
    def index(self, gen): ...
    def order(self): ...
    @property
    def elements(self): ...
    @property
    def rank(self): ...
    @property
    def is_abelian(self): ...
    @property
    def identity(self): ...
    def contains(self, g): ...
    def center(self): ...

class FreeGroupElement(CantSympify, DefaultPrinting, tuple):
    is_assoc_word: bool
    def new(self, init): ...
    def __hash__(self): ...
    def copy(self): ...
    @property
    def is_identity(self): ...
    @property
    def array_form(self): ...
    @property
    def letter_form(self): ...
    def __getitem__(self, i): ...
    def index(self, gen): ...
    @property
    def letter_form_elm(self): ...
    @property
    def ext_rep(self): ...
    def __contains__(self, gen) -> bool: ...
    def __pow__(self, n): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __add__(self, other): ...
    def inverse(self): ...
    def order(self): ...
    def commutator(self, other): ...
    def eliminate_words(self, words, _all: bool = False, inverse: bool = True): ...
    def eliminate_word(self, gen, by: Incomplete | None = None, _all: bool = False, inverse: bool = True): ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def exponent_sum(self, gen): ...
    def generator_count(self, gen): ...
    def subword(self, from_i, to_j, strict: bool = True): ...
    def subword_index(self, word, start: int = 0): ...
    def is_dependent(self, word): ...
    def is_independent(self, word): ...
    def contains_generators(self): ...
    def cyclic_subword(self, from_i, to_j): ...
    def cyclic_conjugates(self): ...
    def is_cyclic_conjugate(self, w): ...
    def number_syllables(self): ...
    def exponent_syllable(self, i): ...
    def generator_syllable(self, i): ...
    def sub_syllables(self, from_i, to_j): ...
    def substituted_word(self, from_i, to_j, by): ...
    def is_cyclically_reduced(self): ...
    def identity_cyclic_reduction(self): ...
    def cyclic_reduction(self, removed: bool = False): ...
    def power_of(self, other): ...
