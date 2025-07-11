from _typeshed import Incomplete
from sympy.core import S as S
from sympy.plotting.pygletplot.plot_object import PlotObject as PlotObject
from sympy.plotting.pygletplot.util import billboard_matrix as billboard_matrix, dot_product as dot_product, get_direction_vectors as get_direction_vectors, strided_range as strided_range, vec_mag as vec_mag, vec_sub as vec_sub
from sympy.utilities.iterables import is_sequence as is_sequence

class PlotAxes(PlotObject):
    visible: Incomplete
    font_face: Incomplete
    font_size: Incomplete
    def __init__(self, *args, style: str = '', none: Incomplete | None = None, frame: Incomplete | None = None, box: Incomplete | None = None, ordinate: Incomplete | None = None, stride: float = 0.25, visible: str = '', overlay: str = '', colored: str = '', label_axes: str = '', label_ticks: str = '', tick_length: float = 0.1, font_face: str = 'Arial', font_size: int = 28, **kwargs) -> None: ...
    label_font: Incomplete
    def reset_resources(self) -> None: ...
    def reset_bounding_box(self) -> None: ...
    def draw(self) -> None: ...
    def adjust_bounds(self, child_bounds) -> None: ...
    def toggle_visible(self) -> None: ...
    def toggle_colors(self) -> None: ...

class PlotAxesBase(PlotObject):
    def __init__(self, parent_axes) -> None: ...
    def draw(self) -> None: ...
    def draw_background(self, color) -> None: ...
    def draw_axis(self, axis, color) -> None: ...
    def draw_text(self, text, position, color, scale: float = 1.0) -> None: ...
    def draw_line(self, v, color) -> None: ...

class PlotAxesOrdinate(PlotAxesBase):
    def __init__(self, parent_axes) -> None: ...
    def draw_axis(self, axis, color) -> None: ...
    def draw_axis_line(self, axis, color, a_min, a_max, labels_visible) -> None: ...
    def draw_axis_line_labels(self, axis, color, axis_line) -> None: ...
    def draw_tick_line(self, axis, color, radius, tick, labels_visible) -> None: ...
    def draw_tick_line_label(self, axis, color, radius, tick) -> None: ...

class PlotAxesFrame(PlotAxesBase):
    def __init__(self, parent_axes) -> None: ...
    def draw_background(self, color) -> None: ...
    def draw_axis(self, axis, color) -> None: ...
