from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.functions.elementary.integers import floor as floor
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr

def normalize(i, parentsize): ...

class MatrixSlice(MatrixExpr):
    parent: Incomplete
    rowslice: Incomplete
    colslice: Incomplete
    def __new__(cls, parent, rowslice, colslice): ...
    @property
    def shape(self): ...
    @property
    def on_diag(self): ...

def slice_of_slice(s, t): ...
def mat_slice_of_slice(parent, rowslice, colslice): ...
