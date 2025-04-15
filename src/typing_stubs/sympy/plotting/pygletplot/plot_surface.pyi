from sympy.core import S as S
from sympy.plotting.pygletplot.plot_mode_base import PlotModeBase as PlotModeBase

class PlotSurface(PlotModeBase):
    default_rot_preset: str
    def calculate_one_cvert(self, u, v): ...
    def draw_verts(self, use_cverts, use_solid_color): ...
