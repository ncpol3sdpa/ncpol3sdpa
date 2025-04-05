from _typeshed import Incomplete
from sympy.core.function import Derivative as Derivative, Subs as Subs
from sympy.core.singleton import S as S
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import iterable as iterable

def finite_diff_weights(order, x_list, x0=...): ...
def apply_finite_diff(order, x_list, y_list, x0=...): ...
def differentiate_finite(expr, *symbols, points: int = 1, x0: Incomplete | None = None, wrt: Incomplete | None = None, evaluate: bool = False): ...
