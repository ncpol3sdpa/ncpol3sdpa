from scipy.sparse import lil_matrix
import numpy as np
# from typing import List

from ncpol3sdpa import AvailableSolvers, SolverRegistry
from ncpol3sdpa.sdp_repr import MomentMatrixSDP, ProblemSDP


def test_1x1() -> None:
    # essentially, maximize -x with x >= 0 and x == 1 and x in R^1
    moment_matrix = MomentMatrixSDP(1, [[(0, 0)]])
    p = ProblemSDP(moment_matrix, lil_matrix([[-1]]))

    solution = SolverRegistry.solve(p, AvailableSolvers.CVXPY)
    assert solution is not None
    result = solution.primal_objective_value
    assert np.abs(-1 - result) <= 0.001  # result should be -1


def test_2x2() -> None:
    # Arithmetic - Geometric inequality
    moment_matrix = MomentMatrixSDP(2, [[(0, 0), (1, 1)], [(1, 0)]])
    # [ 1 a ]
    # [ a 1 ]
    p = ProblemSDP(moment_matrix, lil_matrix([[0, -1], [-1, 0]]))
    # maximize -2a, optimal for a = -1, and objective = 2
    # x2 -2axy + y2 >= 0, because SDP

    solution = SolverRegistry.solve(p, AvailableSolvers.CVXPY)
    assert solution is not None
    result = solution.primal_objective_value
    assert np.abs(2 - result) <= 0.001  # result should be 2


def test_2x2_mosek() -> None:
    # Arithmetic - Geometric inequality
    moment_matrix = MomentMatrixSDP(2, [[(0, 0), (1, 1)], [(1, 0)]])
    # [ 1 a ]
    # [ a 1 ]
    p = ProblemSDP(moment_matrix, lil_matrix([[0, -1], [-1, 0]]))
    # maximize -2a, optimal for a = -1, and objective = 2
    # x2 -2axy + y2 >= 0, because SDP

    solution = SolverRegistry.solve(p, AvailableSolvers.CVXPY)
    assert solution is not None
    result = solution.primal_objective_value
    assert np.abs(2 - result) <= 0.001  # result should be 2

    expected = np.array([[1, -1], [-1, 1]])
    h = expected - solution.primal_PSD_variables[0]
    assert np.trace(h.T @ h) <= 0.001  # result should be 2
