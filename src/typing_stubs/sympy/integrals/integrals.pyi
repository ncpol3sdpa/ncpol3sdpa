from .deltafunctions import deltaintegrate as deltaintegrate
from .meijerint import meijerint_definite as meijerint_definite, meijerint_indefinite as meijerint_indefinite
from .rationaltools import ratint as ratint
from .trigonometry import trigintegrate as trigintegrate
from _typeshed import Incomplete
from sympy.concrete.expr_with_limits import AddWithLimits as AddWithLimits
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import diff as diff
from sympy.core.logic import fuzzy_bool as fuzzy_bool
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import oo as oo, pi as pi
from sympy.core.relational import Ne as Ne
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.core.sympify import sympify as sympify
from sympy.functions import Piecewise as Piecewise, atan as atan, cot as cot, piecewise_fold as piecewise_fold, sqrt as sqrt, tan as tan
from sympy.functions.elementary.complexes import Abs as Abs, sign as sign
from sympy.functions.elementary.exponential import log as log
from sympy.functions.elementary.integers import floor as floor
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.functions.special.singularity_functions import Heaviside as Heaviside
from sympy.matrices import MatrixBase as MatrixBase
from sympy.polys import Poly as Poly, PolynomialError as PolynomialError
from sympy.series.formal import FormalPowerSeries as FormalPowerSeries
from sympy.series.limits import limit as limit
from sympy.series.order import Order as Order
from sympy.tensor.functions import shape as shape
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.misc import filldedent as filldedent

class Integral(AddWithLimits):
    args: tuple[Expr, Tuple]
    def __new__(cls, function, *symbols, **assumptions): ...
    def __getnewargs__(self): ...
    @property
    def free_symbols(self): ...
    def transform(self, x, u): ...
    def doit(self, **hints): ...
    def as_sum(self, n: Incomplete | None = None, method: str = 'midpoint', evaluate: bool = True): ...
    def principal_value(self, **kwargs): ...

def integrate(*args, meijerg: Incomplete | None = None, conds: str = 'piecewise', risch: Incomplete | None = None, heurisch: Incomplete | None = None, manual: Incomplete | None = None, **kwargs): ...
def line_integrate(field, curve, vars): ...
def _(expr): ...
