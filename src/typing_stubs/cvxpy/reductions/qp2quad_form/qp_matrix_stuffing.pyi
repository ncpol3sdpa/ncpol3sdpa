import numpy as np
from _typeshed import Incomplete
from cvxpy.constraints import Equality as Equality, ExpCone as ExpCone, Inequality as Inequality, NonNeg as NonNeg, NonPos as NonPos, PSD as PSD, SOC as SOC, Zero as Zero
from cvxpy.cvxcore.python import canonInterface as canonInterface
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.problems.objective import Minimize as Minimize
from cvxpy.problems.param_prob import ParamProb as ParamProb
from cvxpy.reductions import InverseData as InverseData, Solution as Solution
from cvxpy.reductions.cvx_attr2constr import convex_attributes as convex_attributes
from cvxpy.reductions.dcp2cone.cone_matrix_stuffing import nonpos2nonneg as nonpos2nonneg
from cvxpy.reductions.matrix_stuffing import MatrixStuffing as MatrixStuffing, extract_lower_bounds as extract_lower_bounds, extract_mip_idx as extract_mip_idx, extract_upper_bounds as extract_upper_bounds
from cvxpy.reductions.utilities import ReducedMat as ReducedMat, are_args_affine as are_args_affine, group_constraints as group_constraints, lower_equality as lower_equality, lower_ineq_to_nonneg as lower_ineq_to_nonneg
from cvxpy.utilities.coeff_extractor import CoeffExtractor as CoeffExtractor

class ConeDims:
    zero: Incomplete
    nonneg: Incomplete
    exp: Incomplete
    soc: Incomplete
    psd: Incomplete
    def __init__(self, constr_map) -> None: ...
    def __getitem__(self, key): ...

class ParamQuadProg(ParamProb):
    P: Incomplete
    q: Incomplete
    x: Incomplete
    A: Incomplete
    lower_bounds: Incomplete
    upper_bounds: Incomplete
    reduced_A: Incomplete
    reduced_P: Incomplete
    constraints: Incomplete
    constr_size: Incomplete
    parameters: Incomplete
    param_id_to_col: Incomplete
    id_to_param: Incomplete
    param_id_to_size: Incomplete
    total_param_size: Incomplete
    variables: Incomplete
    var_id_to_col: Incomplete
    id_to_var: Incomplete
    formatted: Incomplete
    def __init__(self, P, q, x, A, variables, var_id_to_col, constraints, parameters, param_id_to_col, formatted: bool = False, lower_bounds: np.ndarray | None = None, upper_bounds: np.ndarray | None = None) -> None: ...
    def is_mixed_integer(self) -> bool: ...
    def apply_parameters(self, id_to_param_value: Incomplete | None = None, zero_offset: bool = False, keep_zeros: bool = False): ...
    def apply_param_jac(self, delP, delq, delA, delb, active_params: Incomplete | None = None) -> None: ...
    def split_solution(self, sltn, active_vars: Incomplete | None = None) -> None: ...
    def split_adjoint(self, del_vars: Incomplete | None = None) -> None: ...

class QpMatrixStuffing(MatrixStuffing):
    canon_backend: Incomplete
    def __init__(self, canon_backend: str | None = None) -> None: ...
    @staticmethod
    def accepts(problem): ...
    def stuffed_objective(self, problem, extractor): ...
    def apply(self, problem): ...
    def invert(self, solution, inverse_data): ...
