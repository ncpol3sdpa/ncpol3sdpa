from _typeshed import Incomplete
from sympy.core import S as S
from sympy.plotting.pygletplot.color_scheme import ColorScheme as ColorScheme
from sympy.plotting.pygletplot.plot_mode import PlotMode as PlotMode
from sympy.utilities.iterables import is_sequence as is_sequence

class PlotModeBase(PlotMode):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool
    styles: Incomplete
    style_override: str
    default_wireframe_color: Incomplete
    default_solid_color: Incomplete
    default_rot_preset: str
    verts: Incomplete
    cverts: Incomplete
    bounds: Incomplete
    cbounds: Incomplete
    predraw: Incomplete
    postdraw: Incomplete
    use_lambda_eval: Incomplete
    style: Incomplete
    color: Incomplete
    bounds_callback: Incomplete
    def __init__(self, *args, bounds_callback: Incomplete | None = None, **kwargs) -> None: ...
    def synchronized(f): ...
    def push_wireframe(self, function) -> None: ...
    def push_solid(self, function) -> None: ...
    def draw(self) -> None: ...
    calculating_verts: Incomplete
    calculating_verts_pos: Incomplete
    calculating_verts_len: Incomplete
    calculating_cverts: Incomplete
    calculating_cverts_pos: Incomplete
    calculating_cverts_len: Incomplete
