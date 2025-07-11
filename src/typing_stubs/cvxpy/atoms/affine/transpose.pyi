import cvxpy.lin_ops.lin_op as lo
from _typeshed import Incomplete
from cvxpy.atoms.affine.affine_atom import AffAtom as AffAtom
from cvxpy.constraints.constraint import Constraint as Constraint

class transpose(AffAtom):
    axes: Incomplete
    def __init__(self, expr, axes: Incomplete | None = None) -> None: ...
    def name(self) -> str: ...
    def numeric(self, values): ...
    def is_atom_log_log_convex(self) -> bool: ...
    def is_atom_log_log_concave(self) -> bool: ...
    def is_symmetric(self) -> bool: ...
    def is_skew_symmetric(self) -> bool: ...
    def is_hermitian(self) -> bool: ...
    def shape_from_args(self) -> tuple[int, ...]: ...
    def get_data(self): ...
    def graph_implementation(self, arg_objs, shape: tuple[int, ...], data: Incomplete | None = None) -> tuple[lo.LinOp, list[Constraint]]: ...
