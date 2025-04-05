from _typeshed import Incomplete
from sympy.core.function import Lambda as Lambda
from sympy.core.numbers import I as I
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, symbols as symbols
from sympy.functions.elementary.exponential import log as log
from sympy.functions.elementary.trigonometric import atan as atan
from sympy.polys import Poly as Poly, ZZ as ZZ, resultant as resultant
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import cancel as cancel
from sympy.polys.rootoftools import RootSum as RootSum

def ratint(f, x, **flags): ...
def ratint_ratpart(f, g, x): ...
def ratint_logpart(f, g, x, t: Incomplete | None = None): ...
def log_to_atan(f, g): ...
def log_to_real(h, q, x, t): ...
