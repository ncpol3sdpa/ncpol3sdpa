from sympy import Basic as Basic, KroneckerProduct as KroneckerProduct, MatMul as MatMul, Wild as Wild
from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.combinatorics.permutations import Permutation as Permutation
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.matrices.expressions.applyfunc import ElementwiseApplyFunction as ElementwiseApplyFunction
from sympy.matrices.expressions.diagonal import DiagMatrix as DiagMatrix
from sympy.matrices.expressions.hadamard import HadamardPower as HadamardPower, hadamard_product as hadamard_product
from sympy.matrices.expressions.matexpr import MatrixElement as MatrixElement, MatrixExpr as MatrixExpr
from sympy.matrices.expressions.special import Identity as Identity, OneMatrix as OneMatrix, ZeroMatrix as ZeroMatrix
from sympy.matrices.expressions.trace import Trace as Trace
from sympy.matrices.expressions.transpose import Transpose as Transpose
from sympy.matrices.matrixbase import MatrixBase as MatrixBase
from sympy.tensor.array.expressions.array_expressions import ArrayAdd as ArrayAdd, ArrayContraction as ArrayContraction, ArrayDiagonal as ArrayDiagonal, ArrayElement as ArrayElement, ArrayElementwiseApplyFunc as ArrayElementwiseApplyFunc, ArrayTensorProduct as ArrayTensorProduct, OneArray as OneArray, PermuteDims as PermuteDims, ZeroArray as ZeroArray, get_rank as get_rank, get_shape as get_shape

def _(expr: ZeroArray): ...
def convert_array_to_matrix(expr): ...
def identify_hadamard_products(expr: ArrayContraction | ArrayDiagonal): ...
def identify_removable_identity_matrices(expr): ...
def remove_identity_matrices(expr: ArrayContraction): ...
