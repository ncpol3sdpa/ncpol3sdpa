from cvxpy.atoms.atom import Atom as Atom
from cvxpy.expressions.constants.parameter import is_param_affine as is_param_affine

class dotsort(Atom):
    def __init__(self, X, W) -> None: ...
    def validate_arguments(self) -> None: ...
    def numeric(self, values): ...
    def shape_from_args(self) -> tuple[int, ...]: ...
    def sign_from_args(self) -> tuple[bool, bool]: ...
    def is_atom_convex(self) -> bool: ...
    def is_atom_concave(self) -> bool: ...
    def is_incr(self, idx) -> bool: ...
    def is_decr(self, idx) -> bool: ...
    def get_data(self) -> None: ...
