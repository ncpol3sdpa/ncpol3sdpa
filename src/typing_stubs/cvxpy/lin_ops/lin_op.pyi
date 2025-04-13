from _typeshed import Incomplete

class LinOp:
    type: Incomplete
    shape: Incomplete
    args: Incomplete
    data: Incomplete
    def __init__(self, type, shape: tuple[int, ...], args, data) -> None: ...

VARIABLE: str
PROMOTE: str
BROADCAST_TO: str
MUL: str
RMUL: str
MUL_ELEM: str
DIV: str
SUM: str
NEG: str
INDEX: str
TRANSPOSE: str
SUM_ENTRIES: str
TRACE: str
RESHAPE: str
DIAG_VEC: str
DIAG_MAT: str
UPPER_TRI: str
CONV: str
KRON_R: str
KRON_L: str
HSTACK: str
VSTACK: str
CONCATENATE: str
SCALAR_CONST: str
DENSE_CONST: str
SPARSE_CONST: str
PARAM: str
NO_OP: str
CONSTANT_ID: int
