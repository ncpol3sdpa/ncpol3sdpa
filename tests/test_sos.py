from ncpol3sdpa.solver import Solver
from ncpol3sdpa.sos import Sos
from ncpol3sdpa.sdp_repr import MomentMatrixSDP, ProblemSDP
import numpy as np
import cvxpy as cp
# from typing import List


def test_dual_constraints_cvxpy() -> None:
    moment_matrix = MomentMatrixSDP(1, [[(0, 0)]])
    p = ProblemSDP(moment_matrix, np.array([[-1]]))
    dual_constraints = Sos.dual_constraints_cvxpy(p)

    x = cp.Variable()
    constraints = [ x <= 1, x>= 1,x>=0 ]
    obj = cp.Maximize (-x)
    prob = cp.Problem(obj,constraints)
    prob.solve()

    cvxpy_dual_constraints = []
    for constraint in constraints:
        cvxpy_dual_constraints.append(constraint.dual_value) 
    
    assert (dual_constraints == cvxpy_dual_constraints)


