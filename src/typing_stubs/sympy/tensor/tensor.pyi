import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from sympy.combinatorics import Permutation as Permutation
from sympy.combinatorics.tensor_can import bsgs_direct_product as bsgs_direct_product, canonicalize as canonicalize, get_symmetric_group_sgs as get_symmetric_group_sgs, riemann_bsgs as riemann_bsgs
from sympy.core import Add as Add, Basic as Basic, Expr as Expr, Mul as Mul, S as S, sympify as sympify
from sympy.core.cache import clear_cache as clear_cache
from sympy.core.containers import Dict as Dict, Tuple as Tuple
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.operations import AssocOp as AssocOp
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import Symbol as Symbol, symbols as symbols
from sympy.core.sympify import CantSympify as CantSympify
from sympy.external.gmpy import SYMPY_INTS as SYMPY_INTS
from sympy.matrices import eye as eye
from sympy.utilities.decorator import deprecated as deprecated, memoize_property as memoize_property
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning, ignore_warnings as ignore_warnings, sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import sift as sift

def deprecate_data() -> None: ...
def deprecate_fun_eval() -> None: ...
def deprecate_call() -> None: ...

class _IndexStructure(CantSympify):
    free: Incomplete
    dum: Incomplete
    index_types: Incomplete
    indices: Incomplete
    def __init__(self, free, dum, index_types, indices, canon_bp: bool = False) -> None: ...
    @staticmethod
    def from_indices(*indices): ...
    @staticmethod
    def from_components_free_dum(components, free, dum): ...
    def get_indices(self): ...
    @staticmethod
    def generate_indices_from_free_dum_index_types(free, dum, index_types): ...
    def get_free_indices(self) -> list[TensorIndex]: ...
    def perm2tensor(self, g, is_canon_bp: bool = False): ...
    def indices_canon_args(self): ...

def components_canon_args(components): ...

class _TensorDataLazyEvaluator(CantSympify):
    def __getitem__(self, key): ...
    @staticmethod
    def data_contract_dum(ndarray_list, dum, ext_rank): ...
    def data_tensorhead_from_tensmul(self, data, tensmul, tensorhead): ...
    def data_from_tensor(self, tensor): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def add_metric_data(self, metric, data) -> None: ...
    @staticmethod
    def inverse_matrix(ndarray): ...
    @staticmethod
    def inverse_transpose_matrix(ndarray): ...
    @staticmethod
    def add_rearrange_tensmul_parts(new_tensmul, old_tensmul): ...
    @staticmethod
    def parse_data(data): ...

class _TensorManager:
    def __init__(self) -> None: ...
    @property
    def comm(self): ...
    def comm_symbols2i(self, i): ...
    def comm_i2symbol(self, i): ...
    def set_comm(self, i, j, c) -> None: ...
    def set_comms(self, *args) -> None: ...
    def get_comm(self, i, j): ...
    def clear(self) -> None: ...

TensorManager: Incomplete

class TensorIndexType(Basic):
    def __new__(cls, name, dummy_name: Incomplete | None = None, dim: Incomplete | None = None, eps_dim: Incomplete | None = None, metric_symmetry: int = 1, metric_name: str = 'metric', **kwargs): ...
    @property
    def name(self): ...
    @property
    def dummy_name(self): ...
    @property
    def dim(self): ...
    @property
    def eps_dim(self): ...
    def metric(self): ...
    def delta(self): ...
    def epsilon(self): ...
    def set_metric(self, tensor) -> None: ...
    def __lt__(self, other): ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @data.deleter
    def data(self) -> None: ...
    def get_kronecker_delta(self): ...
    def get_epsilon(self): ...

class TensorIndex(Basic):
    def __new__(cls, name, tensor_index_type, is_up: bool = True): ...
    @property
    def name(self): ...
    @property
    def tensor_index_type(self): ...
    @property
    def is_up(self): ...
    def __lt__(self, other): ...
    def __neg__(self): ...

def tensor_indices(s, typ): ...

class TensorSymmetry(Basic):
    def __new__(cls, *args, **kw_args): ...
    @property
    def base(self): ...
    @property
    def generators(self): ...
    @property
    def rank(self): ...
    @classmethod
    def fully_symmetric(cls, rank): ...
    @classmethod
    def direct_product(cls, *args): ...
    @classmethod
    def riemann(cls): ...
    @classmethod
    def no_symmetry(cls, rank): ...

def tensorsymmetry(*args): ...

class TensorType(Basic):
    is_commutative: bool
    def __new__(cls, index_types, symmetry, **kw_args): ...
    @property
    def index_types(self): ...
    @property
    def symmetry(self): ...
    @property
    def types(self): ...
    def __call__(self, s, comm: int = 0): ...

def tensorhead(name, typ, sym: Incomplete | None = None, comm: int = 0): ...

class TensorHead(Basic):
    is_commutative: bool
    def __new__(cls, name, index_types, symmetry: Incomplete | None = None, comm: int = 0): ...
    @property
    def name(self): ...
    @property
    def index_types(self): ...
    @property
    def symmetry(self): ...
    @property
    def comm(self): ...
    @property
    def rank(self): ...
    def __lt__(self, other): ...
    def commutes_with(self, other): ...
    def __call__(self, *indices, **kw_args): ...
    def __pow__(self, other): ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @data.deleter
    def data(self) -> None: ...
    def __iter__(self): ...

def tensor_heads(s, index_types, symmetry: Incomplete | None = None, comm: int = 0): ...

class TensExpr(Expr, ABC, metaclass=abc.ABCMeta):
    is_commutative: bool
    def __neg__(self): ...
    def __abs__(self) -> None: ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other) -> None: ...
    def __pow__(self, other): ...
    def __rpow__(self, other) -> None: ...
    @property
    @abstractmethod
    def nocoeff(self): ...
    @property
    @abstractmethod
    def coeff(self): ...
    @abstractmethod
    def get_indices(self): ...
    @abstractmethod
    def get_free_indices(self) -> list[TensorIndex]: ...
    def fun_eval(self, *index_tuples): ...
    def get_matrix(self): ...
    def expand(self, **hints): ...
    def replace_with_arrays(self, replacement_dict, indices: Incomplete | None = None): ...

class TensAdd(TensExpr, AssocOp):
    def __new__(cls, *args, **kw_args): ...
    @property
    def coeff(self): ...
    @property
    def nocoeff(self): ...
    def get_free_indices(self) -> list[TensorIndex]: ...
    def rank(self): ...
    def free_args(self): ...
    def free_indices(self): ...
    def doit(self, **hints): ...
    def get_indices(self): ...
    def __call__(self, *indices): ...
    def canon_bp(self): ...
    def equals(self, other): ...
    def __getitem__(self, item): ...
    def contract_delta(self, delta): ...
    def contract_metric(self, g): ...
    def substitute_indices(self, *index_tuples): ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @data.deleter
    def data(self) -> None: ...
    def __iter__(self): ...

class Tensor(TensExpr):
    is_commutative: bool
    args: tuple[TensorHead, Tuple]
    def __new__(cls, tensor_head, indices, *, is_canon_bp: bool = False, **kw_args): ...
    @property
    def free(self): ...
    @property
    def dum(self): ...
    @property
    def ext_rank(self): ...
    @property
    def coeff(self): ...
    @property
    def nocoeff(self): ...
    @property
    def component(self): ...
    @property
    def components(self): ...
    @property
    def head(self): ...
    @property
    def indices(self): ...
    @property
    def free_indices(self): ...
    @property
    def index_types(self): ...
    @property
    def rank(self): ...
    def doit(self, **hints): ...
    @property
    def free_in_args(self): ...
    @property
    def dum_in_args(self): ...
    @property
    def free_args(self): ...
    def commutes_with(self, other): ...
    def perm2tensor(self, g, is_canon_bp: bool = False): ...
    def canon_bp(self): ...
    def split(self): ...
    def sorted_components(self): ...
    def get_indices(self) -> list[TensorIndex]: ...
    def get_free_indices(self) -> list[TensorIndex]: ...
    def as_base_exp(self): ...
    def substitute_indices(self, *index_tuples): ...
    def matches(self, expr, repl_dict: Incomplete | None = None, old: bool = False): ...
    def __call__(self, *indices): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @data.deleter
    def data(self) -> None: ...
    def equals(self, other): ...
    def contract_metric(self, g): ...
    def contract_delta(self, metric): ...

class TensMul(TensExpr, AssocOp):
    identity: Incomplete
    def __new__(cls, *args, **kw_args): ...
    index_types: Incomplete
    free: Incomplete
    dum: Incomplete
    free_indices: Incomplete
    rank: Incomplete
    ext_rank: Incomplete
    def doit(self, **hints): ...
    @staticmethod
    def from_data(coeff, components, free, dum, **kw_args): ...
    @property
    def free_args(self): ...
    @property
    def components(self): ...
    @property
    def free_in_args(self): ...
    @property
    def coeff(self): ...
    @property
    def nocoeff(self): ...
    @property
    def dum_in_args(self): ...
    def equals(self, other): ...
    def get_indices(self): ...
    def get_free_indices(self) -> list[TensorIndex]: ...
    def split(self): ...
    def __neg__(self): ...
    def __getitem__(self, item): ...
    def sorted_components(self): ...
    def perm2tensor(self, g, is_canon_bp: bool = False): ...
    def canon_bp(self): ...
    def contract_delta(self, delta): ...
    def contract_metric(self, g): ...
    def substitute_indices(self, *index_tuples): ...
    def __call__(self, *indices): ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @data.deleter
    def data(self) -> None: ...
    def __iter__(self): ...

class TensorElement(TensExpr):
    def __new__(cls, expr, index_map): ...
    @property
    def free(self): ...
    @property
    def dum(self): ...
    @property
    def expr(self): ...
    @property
    def index_map(self): ...
    @property
    def coeff(self): ...
    @property
    def nocoeff(self): ...
    def get_free_indices(self): ...
    def get_indices(self): ...

class WildTensorHead(TensorHead):
    def __new__(cls, name, index_types: Incomplete | None = None, symmetry: Incomplete | None = None, comm: int = 0, unordered_indices: bool = False): ...
    @property
    def unordered_indices(self): ...
    def __call__(self, *indices, **kwargs): ...

class WildTensor(Tensor):
    def __new__(cls, tensor_head, indices, **kw_args): ...
    def matches(self, expr, repl_dict: Incomplete | None = None, old: bool = False): ...

class WildTensorIndex(TensorIndex):
    def __new__(cls, name, tensor_index_type, is_up: bool = True, ignore_updown: bool = False): ...
    @property
    def ignore_updown(self): ...
    def __neg__(self): ...
    def matches(self, expr, repl_dict: Incomplete | None = None, old: bool = False): ...

class _WildTensExpr(Basic):
    expr: Incomplete
    def __init__(self, expr) -> None: ...
    def __call__(self, *indices): ...
    def __neg__(self): ...
    def __abs__(self) -> None: ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other) -> None: ...
    def __rmul__(self, other) -> None: ...
    def __truediv__(self, other) -> None: ...
    def __rtruediv__(self, other) -> None: ...
    def __pow__(self, other) -> None: ...
    def __rpow__(self, other) -> None: ...

def canon_bp(p): ...
def tensor_mul(*a): ...
def riemann_cyclic_replace(t_r): ...
def riemann_cyclic(t2): ...
def get_lines(ex, index_type): ...
def get_free_indices(t): ...
def get_indices(t): ...
def get_dummy_indices(t): ...
def get_index_structure(t): ...
def get_coeff(t): ...
def contract_metric(t, g): ...
def perm2tensor(t, g, is_canon_bp: bool = False): ...
def substitute_indices(t, *index_tuples): ...
def get_postprocessor(cls): ...
