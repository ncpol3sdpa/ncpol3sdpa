import abc
from _typeshed import Incomplete
from cvxpy.constraints import NonNeg as NonNeg, Zero as Zero
from cvxpy.reductions.cvx_attr2constr import convex_attributes as convex_attributes
from cvxpy.reductions.qp2quad_form.qp_matrix_stuffing import ConeDims as ConeDims, ParamQuadProg as ParamQuadProg
from cvxpy.reductions.solvers.solver import Solver as Solver
from cvxpy.reductions.utilities import group_constraints as group_constraints

class QpSolver(Solver, metaclass=abc.ABCMeta):
    SUPPORTED_CONSTRAINTS: Incomplete
    REQUIRES_CONSTR: bool
    IS_MIP: str
    def accepts(self, problem): ...
    def apply(self, problem): ...
