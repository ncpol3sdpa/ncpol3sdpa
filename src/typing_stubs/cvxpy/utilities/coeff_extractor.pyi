import numpy as np
import scipy.sparse as sp
from _typeshed import Incomplete
from cvxpy.cvxcore.python import canonInterface as canonInterface
from cvxpy.lin_ops.canon_backend import TensorRepresentation as TensorRepresentation
from cvxpy.lin_ops.lin_op import LinOp as LinOp, NO_OP as NO_OP
from cvxpy.reductions.inverse_data import InverseData as InverseData
from cvxpy.utilities.replace_quad_forms import replace_quad_forms as replace_quad_forms, restore_quad_forms as restore_quad_forms

class CoeffExtractor:
    id_map: Incomplete
    x_length: Incomplete
    var_shapes: Incomplete
    param_shapes: Incomplete
    param_to_size: Incomplete
    param_id_map: Incomplete
    canon_backend: Incomplete
    def __init__(self, inverse_data, canon_backend: str | None) -> None: ...
    def affine(self, expr): ...
    def extract_quadratic_coeffs(self, affine_expr, quad_forms): ...
    def quad_form(self, expr): ...
    def merge_P_list(self, P_list: list[TensorRepresentation], P_height: int, num_params: int) -> sp.csc_matrix: ...
    def merge_q_list(self, q_list: list[sp.spmatrix | np.ndarray], constant: sp.csc_matrix, num_params: int) -> sp.csr_matrix: ...
