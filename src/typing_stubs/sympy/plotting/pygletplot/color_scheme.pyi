from .util import create_bounds as create_bounds, interpolate as interpolate, rinterpolate as rinterpolate, update_bounds as update_bounds
from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.symbol import Symbol as Symbol, symbols as symbols
from sympy.utilities.iterables import sift as sift
from sympy.utilities.lambdify import lambdify as lambdify

class ColorGradient:
    colors: Incomplete
    intervals: Incomplete
    def __init__(self, *args) -> None: ...
    def copy(self): ...
    def __call__(self, r, g, b): ...

default_color_schemes: Incomplete

class ColorScheme:
    args: Incomplete
    f: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, x, y, z, u, v): ...
    def apply_to_curve(self, verts, u_set, set_len: Incomplete | None = None, inc_pos: Incomplete | None = None): ...
    def apply_to_surface(self, verts, u_set, v_set, set_len: Incomplete | None = None, inc_pos: Incomplete | None = None): ...
    def str_base(self): ...

x: Incomplete
y: Incomplete
z: Incomplete
t: Incomplete
u: Incomplete
v: Incomplete
