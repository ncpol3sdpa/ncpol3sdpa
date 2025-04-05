from _typeshed import Incomplete
from sympy.core.numbers import I as I, NumberSymbol as NumberSymbol, oo as oo, zoo as zoo
from sympy.core.symbol import Symbol as Symbol
from sympy.external import import_module as import_module
from sympy.utilities.iterables import numbered_symbols as numbered_symbols

class vectorized_lambdify:
    args: Incomplete
    expr: Incomplete
    np: Incomplete
    lambda_func_1: Incomplete
    vector_func_1: Incomplete
    lambda_func_2: Incomplete
    vector_func_2: Incomplete
    vector_func: Incomplete
    failure: bool
    def __init__(self, args, expr) -> None: ...
    def __call__(self, *args): ...

class lambdify:
    args: Incomplete
    expr: Incomplete
    lambda_func_1: Incomplete
    lambda_func_2: Incomplete
    lambda_func_3: Incomplete
    lambda_func: Incomplete
    failure: bool
    def __init__(self, args, expr) -> None: ...
    def __call__(self, args): ...

def experimental_lambdify(*args, **kwargs): ...

class Lambdifier:
    print_lambda: Incomplete
    use_evalf: Incomplete
    float_wrap_evalf: Incomplete
    complex_wrap_evalf: Incomplete
    use_np: Incomplete
    use_python_math: Incomplete
    use_python_cmath: Incomplete
    use_interval: Incomplete
    dict_str: Incomplete
    dict_fun: Incomplete
    eval_str: Incomplete
    lambda_func: Incomplete
    def __init__(self, args, expr, print_lambda: bool = False, use_evalf: bool = False, float_wrap_evalf: bool = False, complex_wrap_evalf: bool = False, use_np: bool = False, use_python_math: bool = False, use_python_cmath: bool = False, use_interval: bool = False) -> None: ...
    def __call__(self, *args, **kwargs): ...
    builtin_functions_different: Incomplete
    builtin_not_functions: Incomplete
    numpy_functions_same: Incomplete
    numpy_functions_different: Incomplete
    numpy_not_functions: Incomplete
    math_functions_same: Incomplete
    math_functions_different: Incomplete
    math_not_functions: Incomplete
    cmath_functions_same: Incomplete
    cmath_functions_different: Incomplete
    cmath_not_functions: Incomplete
    interval_not_functions: Incomplete
    interval_functions_same: Incomplete
    interval_functions_different: Incomplete
    def get_dict_str(self): ...
    def get_dict_fun(self): ...
    def str2tree(self, exprstr): ...
    @classmethod
    def tree2str(cls, tree): ...
    def tree2str_translate(self, tree): ...
    def translate_str(self, estr): ...
    def translate_func(self, func_name, argtree): ...
    @classmethod
    def sympy_expression_namespace(cls, expr): ...
    @staticmethod
    def sympy_atoms_namespace(expr): ...
