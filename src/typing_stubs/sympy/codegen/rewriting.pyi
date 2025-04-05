from _typeshed import Incomplete
from sympy.assumptions import Q as Q, ask as ask
from sympy.codegen.cfunctions import exp2 as exp2, expm1 as expm1, log1p as log1p, log2 as log2
from sympy.codegen.matrix_nodes import MatrixSolve as MatrixSolve
from sympy.codegen.numpy_nodes import logaddexp as logaddexp, logaddexp2 as logaddexp2
from sympy.codegen.scipy_nodes import cosm1 as cosm1, powm1 as powm1
from sympy.core.expr import UnevaluatedExpr as UnevaluatedExpr
from sympy.core.function import expand_log as expand_log
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.symbol import Wild as Wild
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, sinc as sinc
from sympy.matrices.expressions.matexpr import MatrixSymbol as MatrixSymbol
from sympy.utilities.iterables import sift as sift

class Optimization:
    cost_function: Incomplete
    priority: Incomplete
    def __init__(self, cost_function: Incomplete | None = None, priority: int = 1) -> None: ...
    def cheapest(self, *args): ...

class ReplaceOptim(Optimization):
    query: Incomplete
    value: Incomplete
    def __init__(self, query, value, **kwargs) -> None: ...
    def __call__(self, expr): ...

def optimize(expr, optimizations): ...

exp2_opt: Incomplete
sinc_opt1: Incomplete
sinc_opt2: Incomplete
sinc_opts: Incomplete
log2_opt: Incomplete
log2const_opt: Incomplete
logsumexp_2terms_opt: Incomplete

class FuncMinusOneOptim(ReplaceOptim):
    func: Incomplete
    func_m_1: Incomplete
    opportunistic: Incomplete
    def __init__(self, func, func_m_1, opportunistic: bool = True) -> None: ...
    def replace_in_Add(self, e): ...
    def __call__(self, expr): ...

expm1_opt: Incomplete
cosm1_opt: Incomplete
powm1_opt: Incomplete
log1p_opt: Incomplete

def create_expand_pow_optimization(limit, *, base_req=...): ...

matinv_opt: Incomplete
logaddexp_opt: Incomplete
logaddexp2_opt: Incomplete
optims_c99: Incomplete
optims_numpy: Incomplete
optims_scipy: Incomplete
