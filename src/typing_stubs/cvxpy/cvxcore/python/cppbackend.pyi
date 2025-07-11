import cvxpy.lin_ops.lin_op as lo
import scipy.sparse as sp
from _typeshed import Incomplete

def build_matrix(id_to_col: dict, param_to_size: dict, param_to_col: dict, var_length: int, constr_length: int, linOps: list[lo.LinOp]) -> sp.csc_matrix: ...

TYPE_MAP: Incomplete

def get_type(linPy): ...
def set_linC_data(linC, linPy) -> None: ...
def make_linC_from_linPy(linPy, linPy_to_linC) -> None: ...
def set_slice_data(linC, linPy) -> None: ...
def build_lin_op_tree(root_linPy, linPy_to_linC) -> None: ...
def set_matrix_data(linC, linPy) -> None: ...
def format_matrix(matrix, shape: Incomplete | None = None, format: str = 'dense'): ...
