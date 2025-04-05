from _typeshed import Incomplete
from sympy.combinatorics.perm_groups import PermutationGroup as PermutationGroup
from sympy.core import Basic as Basic, Tuple as Tuple, default_sort_key as default_sort_key
from sympy.sets import FiniteSet as FiniteSet
from sympy.utilities.iterables import flatten as flatten, minlex as minlex, unflatten as unflatten
from sympy.utilities.misc import as_int as as_int

rmul: Incomplete

class Polyhedron(Basic):
    def __new__(cls, corners, faces=(), pgroup=()): ...
    @property
    def corners(self): ...
    vertices = corners
    @property
    def array_form(self): ...
    @property
    def cyclic_form(self): ...
    @property
    def size(self): ...
    @property
    def faces(self): ...
    @property
    def pgroup(self): ...
    @property
    def edges(self): ...
    def rotate(self, perm) -> None: ...
    def reset(self) -> None: ...

tetrahedron: Incomplete
cube: Incomplete
octahedron: Incomplete
dodecahedron: Incomplete
icosahedron: Incomplete
tetrahedron_faces: Incomplete
cube_faces: Incomplete
octahedron_faces: Incomplete
dodecahedron_faces: Incomplete
icosahedron_faces: Incomplete
