from sympy import KroneckerProduct as KroneckerProduct
from sympy.core.basic import Basic as Basic
from sympy.core.function import Lambda as Lambda
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Integer as Integer
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, symbols as symbols
from sympy.matrices.expressions.hadamard import HadamardPower as HadamardPower, HadamardProduct as HadamardProduct
from sympy.matrices.expressions.matadd import MatAdd as MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr
from sympy.matrices.expressions.matmul import MatMul as MatMul
from sympy.matrices.expressions.matpow import MatPow as MatPow
from sympy.matrices.expressions.trace import Trace as Trace
from sympy.matrices.expressions.transpose import Transpose as Transpose
from sympy.tensor.array.expressions.array_expressions import ArrayElementwiseApplyFunc as ArrayElementwiseApplyFunc, Reshape as Reshape

def convert_matrix_to_array(expr: Basic) -> Basic: ...
