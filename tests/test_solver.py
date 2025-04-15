from ncpol3sdpa.solver import Solver
from ncpol3sdpa.sdp_repr import MomentMatrixSDP, ProblemSDP
import numpy as np
# from typing import List


def test_1x1() -> None:
    # essentially, maximize -x with x >= 0 and x == 1 and x in R^1
    moment_matrix = MomentMatrixSDP(1, [[(0, 0)]])
    p = ProblemSDP(moment_matrix, np.array([[-1]]))

    result = Solver.solve_cvxpy(p)
    assert np.abs(-1 - result) <= 0.001  # result should be -1


def test_2x2() -> None:
    # Arithmetic - Geometric inequality
    moment_matrix = MomentMatrixSDP(2, [[(0, 0), (1, 1)], [(1, 0)]])
    # [ 1 a ]
    # [ a 1 ]
    p = ProblemSDP(moment_matrix, np.array([[0, -1], [-1, 0]]))
    # maximize -2a, optimal for a = -1, and objective = 2
    # x2 -2axy + y2 >= 0, because SDP

    result = Solver.solve_cvxpy(p)
    assert np.abs(2 - result) <= 0.001  # result should be 2
