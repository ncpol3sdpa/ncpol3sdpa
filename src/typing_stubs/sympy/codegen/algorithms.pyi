from _typeshed import Incomplete
from sympy.codegen.ast import AddAugmentedAssignment as AddAugmentedAssignment, Assignment as Assignment, CodeBlock as CodeBlock, Declaration as Declaration, FunctionDefinition as FunctionDefinition, Pointer as Pointer, Print as Print, Return as Return, Scope as Scope, Variable as Variable, While as While, break_ as break_, real as real
from sympy.codegen.cfunctions import isnan as isnan
from sympy.core.containers import Tuple as Tuple
from sympy.core.numbers import oo as oo
from sympy.core.relational import Gt as Gt, Lt as Lt
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.logic.boolalg import And as And

def newtons_method(expr, wrt, atol: float = 1e-12, delta: Incomplete | None = None, *, rtol: float = 4e-16, debug: bool = False, itermax: Incomplete | None = None, counter: Incomplete | None = None, delta_fn=..., cse: bool = False, handle_nan: Incomplete | None = None, bounds: Incomplete | None = None): ...
def newtons_method_function(expr, wrt, params: Incomplete | None = None, func_name: str = 'newton', attrs=..., *, delta: Incomplete | None = None, **kwargs): ...
