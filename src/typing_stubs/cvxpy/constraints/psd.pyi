from _typeshed import Incomplete
from cvxpy.constraints.cones import Cone as Cone
from cvxpy.expressions import cvxtypes as cvxtypes
from cvxpy.utilities import scopes as scopes

class PSD(Cone):
    def __init__(self, expr, constr_id: Incomplete | None = None) -> None: ...
    def name(self) -> str: ...
    def is_dcp(self, dpp: bool = False) -> bool: ...
    def is_dgp(self, dpp: bool = False) -> bool: ...
    def is_dqcp(self) -> bool: ...
    @property
    def residual(self): ...
