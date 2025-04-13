from _typeshed import Incomplete

INF_OR_UNB_MESSAGE: str

def failure_solution(status, attr: Incomplete | None = None) -> Solution: ...

class Solution:
    status: Incomplete
    opt_val: Incomplete
    primal_vars: Incomplete
    dual_vars: Incomplete
    attr: Incomplete
    def __init__(self, status, opt_val, primal_vars, dual_vars, attr) -> None: ...
    def copy(self) -> Solution: ...
