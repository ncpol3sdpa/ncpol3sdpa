from _typeshed import Incomplete
from sympy.core.containers import Tuple as Tuple
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.plotting.plot import plot_factory as plot_factory
from sympy.plotting.series import ImplicitSeries as ImplicitSeries
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.iterables import flatten as flatten

__doctest_requires__: Incomplete

def plot_implicit(expr, x_var: Incomplete | None = None, y_var: Incomplete | None = None, adaptive: bool = True, depth: int = 0, n: int = 300, line_color: str = 'blue', show: bool = True, **kwargs): ...
