from .cartan_type import Standard_Cartan as Standard_Cartan
from sympy.core.backend import eye as eye

class TypeB(Standard_Cartan):
    def __new__(cls, n): ...
    def dimension(self): ...
    def basic_root(self, i, j): ...
    def simple_root(self, i): ...
    def positive_roots(self): ...
    def roots(self): ...
    def cartan_matrix(self): ...
    def basis(self): ...
    def lie_algebra(self): ...
    def dynkin_diagram(self): ...
