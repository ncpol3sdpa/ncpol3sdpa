from sympy.core import S as S
from sympy.plotting.pygletplot.plot_mode_base import PlotModeBase as PlotModeBase

class PlotCurve(PlotModeBase):
    style_override: str
    def calculate_one_cvert(self, t): ...
    def draw_verts(self, use_cverts): ...
