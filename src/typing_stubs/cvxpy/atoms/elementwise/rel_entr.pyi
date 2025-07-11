from cvxpy.atoms.elementwise.elementwise import Elementwise as Elementwise
from scipy.sparse import csc_matrix as csc_matrix

class rel_entr(Elementwise):
    def __init__(self, x, y) -> None: ...
    def numeric(self, values): ...
    def sign_from_args(self) -> tuple[bool, bool]: ...
    def is_atom_convex(self) -> bool: ...
    def is_atom_concave(self) -> bool: ...
    def is_incr(self, idx) -> bool: ...
    def is_decr(self, idx) -> bool: ...
