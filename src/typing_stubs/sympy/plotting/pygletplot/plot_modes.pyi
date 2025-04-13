from _typeshed import Incomplete
from sympy.core.numbers import pi as pi
from sympy.functions import cos as cos, sin as sin
from sympy.plotting.pygletplot.plot_curve import PlotCurve as PlotCurve
from sympy.plotting.pygletplot.plot_surface import PlotSurface as PlotSurface
from sympy.utilities.lambdify import lambdify as lambdify

def float_vec3(f): ...

class Cartesian2D(PlotCurve):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class Cartesian3D(PlotSurface):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class ParametricCurve2D(PlotCurve):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class ParametricCurve3D(PlotCurve):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class ParametricSurface(PlotSurface):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class Polar(PlotCurve):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class Cylindrical(PlotSurface):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool

class Spherical(PlotSurface):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool
