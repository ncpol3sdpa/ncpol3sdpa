from cvxpy.atoms.atom import Atom as Atom
from cvxpy.constraints.constraint import Constraint as Constraint

class log_det(Atom):
    def __init__(self, A) -> None: ...
    def numeric(self, values): ...
    def validate_arguments(self) -> None: ...
    def shape_from_args(self) -> tuple[int, ...]: ...
    def sign_from_args(self) -> tuple[bool, bool]: ...
    def is_atom_convex(self) -> bool: ...
    def is_atom_concave(self) -> bool: ...
    def is_incr(self, idx) -> bool: ...
    def is_decr(self, idx) -> bool: ...
    @property
    def value(self) -> float: ...
