from sympy import Add as Add, Dummy as Dummy, Mul as Mul, Sum as Sum
from sympy.tensor.array.expressions import ArrayAdd as ArrayAdd, ArrayElementwiseApplyFunc as ArrayElementwiseApplyFunc, PermuteDims as PermuteDims, Reshape as Reshape
from sympy.tensor.array.expressions.array_expressions import ArrayContraction as ArrayContraction, ArrayDiagonal as ArrayDiagonal, ArrayTensorProduct as ArrayTensorProduct, get_rank as get_rank, get_shape as get_shape

def convert_array_to_indexed(expr, indices): ...

class _ConvertArrayToIndexed:
    count_dummies: int
    def __init__(self) -> None: ...
    def do_convert(self, expr, indices): ...
