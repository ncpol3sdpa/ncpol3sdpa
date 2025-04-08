from ncpol3sdpa.solver import Solver
from ncpol3sdpa.sos import Sos
from ncpol3sdpa.sdp_repr import MomentMatrixSDP, ProblemSDP
import numpy as np
import cvxpy as cp
# from typing import List


def test_dual_constraints_cvxpy() -> None:
    moment_matrix = MomentMatrixSDP(1, [[(0, 0)]])
    problem = ProblemSDP(moment_matrix, np.array([[-1]]))
    dual_constraints = Sos.dual_constraints_cvxpy(problem)

    x = cp.Variable()
    constraints = [ x <= 1, x>= 1,x>=0 ]
    obj = cp.Maximize (-x)
    prob = cp.Problem(obj,constraints)
    prob.solve()

    cvxpy_dual_constraints = []
    for constraint in constraints:
        cvxpy_dual_constraints.append(constraint.dual_value) 
    
    assert (dual_constraints == cvxpy_dual_constraints)

def test_dual_constraints_cvxpy_2() -> None:
    # Arithmetic - Geometric inequality
    moment_matrix = MomentMatrixSDP(2, [[(0, 0), (1, 1)], [(1, 0)]])
    # [ 1 a ]
    # [ a 1 ]
    p = ProblemSDP(moment_matrix, np.array([[0, -1], [-1, 0]]))
    # maximize -2a, optimal for a = -1, and objective = 2
    # x2 -2axy + y2 >= 0, because SDP

    dual_constraints = Sos.dual_constraints_cvxpy(p)
    
    x = cp.Variable()
    y = cp.Variable()
    constraints = [ x + y == 1,x - y >= 1]
    obj = cp.Minimize ((x-y)**2)
    prob = cp.Problem(obj,constraints)
    prob.solve()

    cvxpy_dual_constraints = []
    for constraint in constraints:
        cvxpy_dual_constraints.append(constraint.dual_value) 
    
    assert (dual_constraints == cvxpy_dual_constraints)



    
