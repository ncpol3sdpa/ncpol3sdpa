import sympy as sp
import numpy as np
from ncpol3sdpa import Problem
from ncpol3sdpa.resolution import utils
from numpy.typing import NDArray
from typing import Any


def find_middle_degree(obj: sp.Expr) -> int:
    deg = utils.degree_of_polynomial(obj)
    if deg % 2 == 0:
        return deg // 2
    else:
        return (deg // 2) + 1


def find_rX(p: Problem) -> int:
    """Return the maximum of all the middle degrees of the polynoms of the problem"""
    maxi: int = find_middle_degree(p.objective)

    for cons in p.constraints:
        middle_degree = find_middle_degree(cons.polynomial)

        if middle_degree > maxi:
            maxi = middle_degree
    return maxi


def stable_rank(matrix: NDArray[Any], tol: float = 1e-6) -> int:
    """Compute matrix rank robustly given numerical noise."""
    s = np.linalg.svd(matrix, compute_uv=False)
    res = np.sum(s > tol)
    assert isinstance(res, int)
    return res


def rank_loop(p: Problem) -> int:
    """Return the first indexation rank r such that max SDP(r)= max f(X), where max f(X) is our original problem"""

    rX: int = find_rX(p)
    r = rX + 1

    print(rX)
    p.solve_unchecked(r)
    assert p.solution is not None
    matrix_order_r = p.solution.primal_PSD_variables[0]

    rangR = stable_rank(matrix_order_r)

    p.solve_unchecked(r - rX)
    assert p.solution is not None
    matrix_order_rX = p.solution.primal_PSD_variables[0]

    rangRX = stable_rank(matrix_order_rX)

    while rangR != rangRX:
        r += 1

        p.solve_unchecked(r)
        assert p.solution is not None
        matrix_order_r = p.solution.primal_PSD_variables[0]
        rangR = stable_rank(matrix_order_r)

        p.solve_unchecked(r - rX)
        assert p.solution is not None
        matrix_order_rX = p.solution.primal_PSD_variables[0]
        rangRX = stable_rank(matrix_order_rX)

        if r == 7:  ## to limit the length of the tests
            return 0

    return r


def is_stable_order(r: int, p: Problem) -> bool:
    """To test if the parameter is a stable order or not"""
    if r < rank_loop(p):
        return False
    return True
