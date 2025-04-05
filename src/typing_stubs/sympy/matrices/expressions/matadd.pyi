from _typeshed import Incomplete
from sympy.core import Basic as Basic, sympify as sympify
from sympy.core.add import Add as Add, add as add
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions import adjoint as adjoint
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr
from sympy.matrices.expressions.special import GenericZeroMatrix as GenericZeroMatrix, ZeroMatrix as ZeroMatrix
from sympy.matrices.expressions.transpose import transpose as transpose
from sympy.matrices.matrixbase import MatrixBase as MatrixBase
from sympy.strategies import condition as condition, do_one as do_one, exhaust as exhaust, flatten as flatten, glom as glom, rm_id as rm_id, sort as sort, unpack as unpack
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import sift as sift

class MatAdd(MatrixExpr, Add):
    is_MatAdd: bool
    identity: Incomplete
    def __new__(cls, *args, evaluate: bool = False, check: Incomplete | None = None, _sympify: bool = True): ...
    @property
    def shape(self): ...
    def could_extract_minus_sign(self): ...
    def expand(self, **kwargs): ...
    def doit(self, **hints): ...

factor_of: Incomplete
matrix_of: Incomplete

def combine(cnt, mat): ...
def merge_explicit(matadd): ...

rules: Incomplete
canonicalize: Incomplete
