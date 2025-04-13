from _typeshed import Incomplete
from sympy import Function as Function
from sympy.combinatorics import Permutation as Permutation
from sympy.concrete.summations import Sum as Sum
from sympy.core.add import Add as Add
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Integer as Integer
from sympy.core.power import Pow as Pow
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.matrices.expressions.matexpr import MatrixElement as MatrixElement
from sympy.tensor.array.expressions import ArrayElementwiseApplyFunc as ArrayElementwiseApplyFunc
from sympy.tensor.array.expressions.array_expressions import ArrayAdd as ArrayAdd, ArrayDiagonal as ArrayDiagonal, ArrayElement as ArrayElement, OneArray as OneArray, get_shape as get_shape
from sympy.tensor.indexed import Indexed as Indexed, IndexedBase as IndexedBase

def convert_indexed_to_array(expr, first_indices: Incomplete | None = None): ...
