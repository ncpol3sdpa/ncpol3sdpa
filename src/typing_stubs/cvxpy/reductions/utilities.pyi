import numpy as np
from _typeshed import Incomplete
from cvxpy.atoms.affine.reshape import reshape as reshape
from cvxpy.atoms.affine.vec import vec as vec
from cvxpy.constraints.nonpos import NonNeg as NonNeg, NonPos as NonPos
from cvxpy.constraints.zero import Zero as Zero
from cvxpy.cvxcore.python import canonInterface as canonInterface

def lower_ineq_to_nonpos(inequality): ...
def lower_ineq_to_nonneg(inequality): ...
def lower_equality(equality): ...
def nonpos2nonneg(nonpos): ...
def special_index_canon(expr, args): ...
def are_args_affine(constraints) -> bool: ...
def group_constraints(constraints): ...

class ReducedMat:
    matrix_data: Incomplete
    var_len: Incomplete
    quad_form: Incomplete
    reduced_mat: Incomplete
    problem_data_index: Incomplete
    mapping_nonzero: Incomplete
    def __init__(self, matrix_data, var_len: int, quad_form: bool = False) -> None: ...
    def cache(self, keep_zeros: bool = False) -> None: ...
    def get_matrix_from_tensor(self, param_vec: np.ndarray, with_offset: bool = True) -> tuple: ...
