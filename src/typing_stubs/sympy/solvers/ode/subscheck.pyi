from _typeshed import Incomplete
from sympy.core import Pow as Pow, S as S
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, diff as diff
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions import exp as exp
from sympy.logic.boolalg import BooleanAtom as BooleanAtom
from sympy.series import Order as Order
from sympy.simplify.simplify import besselsimp as besselsimp, posify as posify, simplify as simplify
from sympy.simplify.sqrtdenest import sqrtdenest as sqrtdenest
from sympy.simplify.trigsimp import trigsimp as trigsimp
from sympy.solvers import solve as solve
from sympy.solvers.deutils import ode_order as ode_order
from sympy.utilities.iterables import is_sequence as is_sequence, iterable as iterable

def sub_func_doit(eq, func, new): ...
def checkodesol(ode, sol, func: Incomplete | None = None, order: str = 'auto', solve_for_func: bool = True): ...
def checksysodesol(eqs, sols, func: Incomplete | None = None): ...
