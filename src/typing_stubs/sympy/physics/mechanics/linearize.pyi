from _typeshed import Incomplete

__all__ = ['Linearizer']

class Linearizer:
    linear_solver: Incomplete
    f_0: Incomplete
    f_1: Incomplete
    f_2: Incomplete
    f_3: Incomplete
    f_4: Incomplete
    f_c: Incomplete
    f_v: Incomplete
    f_a: Incomplete
    q: Incomplete
    u: Incomplete
    q_i: Incomplete
    q_d: Incomplete
    u_i: Incomplete
    u_d: Incomplete
    r: Incomplete
    lams: Incomplete
    perm_mat: Incomplete
    def __init__(self, f_0, f_1, f_2, f_3, f_4, f_c, f_v, f_a, q, u, q_i: Incomplete | None = None, q_d: Incomplete | None = None, u_i: Incomplete | None = None, u_d: Incomplete | None = None, r: Incomplete | None = None, lams: Incomplete | None = None, linear_solver: str = 'LU') -> None: ...
    def linearize(self, op_point: Incomplete | None = None, A_and_B: bool = False, simplify: bool = False): ...
