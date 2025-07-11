from _typeshed import Incomplete
from sympy.core._print_helpers import Printable as Printable
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import diff as diff
from sympy.core.singleton import S as S
from sympy.tensor.array.dense_ndim_array import DenseNDimArray as DenseNDimArray, ImmutableDenseNDimArray as ImmutableDenseNDimArray
from sympy.tensor.array.ndim_array import NDimArray as NDimArray
from sympy.tensor.array.sparse_ndim_array import SparseNDimArray as SparseNDimArray

def tensorproduct(*args): ...
def tensorcontraction(array, *contraction_axes): ...
def tensordiagonal(array, *diagonal_axes): ...
def derive_by_array(expr, dx): ...
def permutedims(expr, perm: Incomplete | None = None, index_order_old: Incomplete | None = None, index_order_new: Incomplete | None = None): ...

class Flatten(Printable):
    def __init__(self, iterable) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def next(self): ...
