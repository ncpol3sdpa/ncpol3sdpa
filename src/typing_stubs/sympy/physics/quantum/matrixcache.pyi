from _typeshed import Incomplete
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.power import Pow as Pow
from sympy.functions.elementary.exponential import exp as exp
from sympy.matrices.dense import Matrix as Matrix
from sympy.physics.quantum.matrixutils import to_numpy as to_numpy, to_scipy_sparse as to_scipy_sparse, to_sympy as to_sympy

class MatrixCache:
    dtype: Incomplete
    def __init__(self, dtype: str = 'complex') -> None: ...
    def cache_matrix(self, name, m) -> None: ...
    def get_matrix(self, name, format): ...

sqrt2_inv: Incomplete
matrix_cache: Incomplete
