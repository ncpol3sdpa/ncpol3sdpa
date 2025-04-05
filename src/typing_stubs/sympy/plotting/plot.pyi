from _typeshed import Incomplete
from sympy.concrete.summations import Sum as Sum
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import AppliedUndef as AppliedUndef, Function as Function
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.external import import_module as import_module
from sympy.functions import sign as sign
from sympy.plotting.backends.base_backend import Plot as Plot, unset_show as unset_show
from sympy.plotting.backends.matplotlibbackend import MatplotlibBackend as MatplotlibBackend
from sympy.plotting.backends.textbackend import TextBackend as TextBackend
from sympy.plotting.plotgrid import PlotGrid as PlotGrid
from sympy.plotting.series import BaseSeries as BaseSeries, ContourSeries as ContourSeries, GenericDataSeries as GenericDataSeries, Line2DBaseSeries as Line2DBaseSeries, Line3DBaseSeries as Line3DBaseSeries, LineOver1DRangeSeries as LineOver1DRangeSeries, List2DSeries as List2DSeries, Parametric2DLineSeries as Parametric2DLineSeries, Parametric3DLineSeries as Parametric3DLineSeries, ParametricSurfaceSeries as ParametricSurfaceSeries, SurfaceBaseSeries as SurfaceBaseSeries, SurfaceOver2DRangeSeries as SurfaceOver2DRangeSeries, centers_of_faces as centers_of_faces, centers_of_segments as centers_of_segments, flat as flat
from sympy.plotting.textplot import textplot as textplot
from sympy.tensor.indexed import Indexed as Indexed

__doctest_requires__: Incomplete

def plot_factory(*args, **kwargs): ...

plot_backends: Incomplete

def plot(*args, show: bool = True, **kwargs): ...
def plot_parametric(*args, show: bool = True, **kwargs): ...
def plot3d_parametric_line(*args, show: bool = True, **kwargs): ...
def plot3d(*args, show: bool = True, **kwargs): ...
def plot3d_parametric_surface(*args, show: bool = True, **kwargs): ...
def plot_contour(*args, show: bool = True, **kwargs): ...
def check_arguments(args, expr_len, nb_of_free_symbols): ...
