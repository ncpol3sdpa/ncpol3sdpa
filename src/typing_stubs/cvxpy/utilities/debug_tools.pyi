from cvxpy.expressions.variable import Variable as Variable

DCP: str
DGP: str
MAX_NODES: int

def node_count(expr) -> int: ...
def build_non_disciplined_error_msg(problem, discipline_type) -> str: ...
