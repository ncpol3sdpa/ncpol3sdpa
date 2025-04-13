import abc
from _typeshed import Incomplete
from cvxpy.constraints.constraint import Constraint as Constraint

class Cone(Constraint, metaclass=abc.ABCMeta):
    def __init__(self, args, constr_id: Incomplete | None = None) -> None: ...
    @property
    def dual_residual(self) -> float: ...
