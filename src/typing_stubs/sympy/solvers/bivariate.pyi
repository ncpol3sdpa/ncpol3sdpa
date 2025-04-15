from sympy.core.add import Add as Add
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import expand_log as expand_log
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy
from sympy.functions.elementary.exponential import LambertW as LambertW, exp as exp, log as log
from sympy.functions.elementary.miscellaneous import root as root
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import Poly as Poly, factor as factor
from sympy.simplify.radsimp import collect as collect
from sympy.simplify.simplify import powsimp as powsimp, separatevars as separatevars
from sympy.solvers.solvers import solve as solve
from sympy.utilities.iterables import uniq as uniq

def bivariate_type(f, x, y, *, first: bool = True): ...
