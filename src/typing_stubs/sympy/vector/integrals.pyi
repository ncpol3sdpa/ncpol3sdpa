from sympy.core import Basic as Basic, diff as diff
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.geometry.entity import GeometryEntity as GeometryEntity
from sympy.integrals import Integral as Integral, integrate as integrate
from sympy.matrices import Matrix as Matrix
from sympy.simplify.simplify import simplify as simplify
from sympy.utilities.iterables import topological_sort as topological_sort
from sympy.vector import CoordSys3D as CoordSys3D, ImplicitRegion as ImplicitRegion, ParametricRegion as ParametricRegion, Vector as Vector, parametric_region_list as parametric_region_list

class ParametricIntegral(Basic):
    def __new__(cls, field, parametricregion): ...
    @property
    def field(self): ...
    @property
    def parametricregion(self): ...

def vector_integrate(field, *region): ...
