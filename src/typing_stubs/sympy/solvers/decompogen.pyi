from sympy.core import Expr as Expr, Function as Function, Pow as Pow, sympify as sympify
from sympy.core.relational import Relational as Relational
from sympy.core.singleton import S as S
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.polys import Poly as Poly, decompose as decompose
from sympy.utilities.misc import func_name as func_name

def decompogen(f, symbol): ...
def compogen(g_s, symbol): ...
