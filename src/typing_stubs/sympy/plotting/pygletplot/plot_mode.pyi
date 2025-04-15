from .plot_interval import PlotInterval as PlotInterval
from .plot_object import PlotObject as PlotObject
from .util import parse_option_string as parse_option_string
from _typeshed import Incomplete
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.geometry.entity import GeometryEntity as GeometryEntity
from sympy.utilities.iterables import is_sequence as is_sequence

class PlotMode(PlotObject):
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool
    def draw(self) -> None: ...
    def __new__(cls, *args, **kwargs): ...

def var_count_error(is_independent, is_plotting): ...
