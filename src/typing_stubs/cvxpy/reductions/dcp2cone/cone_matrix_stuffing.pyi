import numpy as np
from _typeshed import Incomplete
from cvxpy.constraints import Equality as Equality, ExpCone as ExpCone, Inequality as Inequality, NonNeg as NonNeg, NonPos as NonPos, PSD as PSD, PowCone3D as PowCone3D, SOC as SOC, Zero as Zero
from cvxpy.cvxcore.python import canonInterface as canonInterface
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.problems.objective import Minimize as Minimize
from cvxpy.problems.param_prob import ParamProb as ParamProb
from cvxpy.reductions import InverseData as InverseData, Solution as Solution, cvx_attr2constr as cvx_attr2constr
from cvxpy.reductions.matrix_stuffing import MatrixStuffing as MatrixStuffing, extract_lower_bounds as extract_lower_bounds, extract_mip_idx as extract_mip_idx, extract_upper_bounds as extract_upper_bounds
from cvxpy.reductions.utilities import ReducedMat as ReducedMat, are_args_affine as are_args_affine, group_constraints as group_constraints, lower_equality as lower_equality, lower_ineq_to_nonneg as lower_ineq_to_nonneg, nonpos2nonneg as nonpos2nonneg
from cvxpy.utilities.coeff_extractor import CoeffExtractor as CoeffExtractor

class ConeDims:
    EQ_DIM: Incomplete
    LEQ_DIM: Incomplete
    EXP_DIM: Incomplete
    SOC_DIM: Incomplete
    PSD_DIM: Incomplete
    P3D_DIM: str
    zero: Incomplete
    nonneg: Incomplete
    exp: Incomplete
    soc: Incomplete
    psd: Incomplete
    p3d: Incomplete
    def __init__(self, constr_map) -> None: ...
    def __getitem__(self, key): ...

class ParamConeProg(ParamProb):
    c: Incomplete
    A: Incomplete
    P: Incomplete
    x: Incomplete
    lower_bounds: Incomplete
    upper_bounds: Incomplete
    reduced_A: Incomplete
    reduced_P: Incomplete
    constraints: Incomplete
    constr_size: Incomplete
    constr_map: Incomplete
    cone_dims: Incomplete
    parameters: Incomplete
    param_id_to_col: Incomplete
    id_to_param: Incomplete
    param_id_to_size: Incomplete
    total_param_size: Incomplete
    variables: Incomplete
    var_id_to_col: Incomplete
    id_to_var: Incomplete
    formatted: Incomplete
    def __init__(self, c, x, A, variables, var_id_to_col, constraints, parameters, param_id_to_col, P: Incomplete | None = None, formatted: bool = False, lower_bounds: np.ndarray | None = None, upper_bounds: np.ndarray | None = None) -> None: ...
    def is_mixed_integer(self) -> bool: ...
    def apply_parameters(self, id_to_param_value: Incomplete | None = None, zero_offset: bool = False, keep_zeros: bool = False, quad_obj: bool = False): ...
    def apply_param_jac(self, delc, delA, delb, active_params: Incomplete | None = None): ...
    def split_solution(self, sltn, active_vars: Incomplete | None = None): ...
    def split_adjoint(self, del_vars: Incomplete | None = None): ...

class ConeMatrixStuffing(MatrixStuffing):
    CONSTRAINTS: str
    quad_obj: Incomplete
    canon_backend: Incomplete
    def __init__(self, quad_obj: bool = False, canon_backend: str | None = None) -> None: ...
    def accepts(self, problem): ...
    def stuffed_objective(self, problem, extractor): ...
    def apply(self, problem): ...
    def invert(self, solution, inverse_data): ...
