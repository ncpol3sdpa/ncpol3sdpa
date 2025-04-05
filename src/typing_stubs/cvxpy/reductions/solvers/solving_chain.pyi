from _typeshed import Incomplete
from cvxpy.atoms import EXP_ATOMS as EXP_ATOMS, NONPOS_ATOMS as NONPOS_ATOMS, PSD_ATOMS as PSD_ATOMS, SOC_ATOMS as SOC_ATOMS
from cvxpy.constraints import Equality as Equality, ExpCone as ExpCone, FiniteSet as FiniteSet, Inequality as Inequality, NonNeg as NonNeg, NonPos as NonPos, PSD as PSD, PowCone3D as PowCone3D, SOC as SOC, Zero as Zero
from cvxpy.constraints.exponential import OpRelEntrConeQuad as OpRelEntrConeQuad, RelEntrConeQuad as RelEntrConeQuad
from cvxpy.error import DCPError as DCPError, DGPError as DGPError, DPPError as DPPError, SolverError as SolverError
from cvxpy.problems.objective import Maximize as Maximize
from cvxpy.reductions.chain import Chain as Chain
from cvxpy.reductions.complex2real import complex2real as complex2real
from cvxpy.reductions.cone2cone.approximations import APPROX_CONES as APPROX_CONES, QuadApprox as QuadApprox
from cvxpy.reductions.cone2cone.exotic2common import EXOTIC_CONES as EXOTIC_CONES, Exotic2Common as Exotic2Common
from cvxpy.reductions.cone2cone.soc2psd import SOC2PSD as SOC2PSD
from cvxpy.reductions.cvx_attr2constr import CvxAttr2Constr as CvxAttr2Constr
from cvxpy.reductions.dcp2cone.cone_matrix_stuffing import ConeMatrixStuffing as ConeMatrixStuffing
from cvxpy.reductions.dcp2cone.dcp2cone import Dcp2Cone as Dcp2Cone
from cvxpy.reductions.dgp2dcp.dgp2dcp import Dgp2Dcp as Dgp2Dcp
from cvxpy.reductions.discrete2mixedint.valinvec2mixedint import Valinvec2mixedint as Valinvec2mixedint
from cvxpy.reductions.eval_params import EvalParams as EvalParams
from cvxpy.reductions.flip_objective import FlipObjective as FlipObjective
from cvxpy.reductions.qp2quad_form import qp2symbolic_qp as qp2symbolic_qp
from cvxpy.reductions.qp2quad_form.qp_matrix_stuffing import QpMatrixStuffing as QpMatrixStuffing
from cvxpy.reductions.reduction import Reduction as Reduction
from cvxpy.reductions.solvers.constant_solver import ConstantSolver as ConstantSolver
from cvxpy.reductions.solvers.solver import Solver as Solver
from cvxpy.settings import CLARABEL as CLARABEL, CPP_CANON_BACKEND as CPP_CANON_BACKEND, NUMPY_CANON_BACKEND as NUMPY_CANON_BACKEND, PARAM_THRESHOLD as PARAM_THRESHOLD, SCIPY_CANON_BACKEND as SCIPY_CANON_BACKEND
from cvxpy.utilities.debug_tools import build_non_disciplined_error_msg as build_non_disciplined_error_msg

DPP_ERROR_MSG: str
ECOS_DEP_DEPRECATION_MSG: str
ECOS_DEPRECATION_MSG: str

def construct_solving_chain(problem, candidates, gp: bool = False, enforce_dpp: bool = False, ignore_dpp: bool = False, canon_backend: str | None = None, solver_opts: dict | None = None, specified_solver: str | None = None) -> SolvingChain: ...

class SolvingChain(Chain):
    solver: Incomplete
    def __init__(self, problem: Incomplete | None = None, reductions: Incomplete | None = None) -> None: ...
    def prepend(self, chain) -> SolvingChain: ...
    def solve(self, problem, warm_start: bool, verbose: bool, solver_opts): ...
    def solve_via_data(self, problem, data, warm_start: bool = False, verbose: bool = False, solver_opts={}): ...
