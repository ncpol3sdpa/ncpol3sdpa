# TODO

import numpy as np
# from typing import List
from ncpol3sdpa import AvailableSolvers, SolverRegistry
from ncpol3sdpa.sdp_repr import MomentMatrixSDP, ProblemSDP
import ncpol3sdpa.sdp_repr as sdp_repr
from ncpol3sdpa import sdp_solution
import cvxpy as cp

from ncpol3sdpa import Constraint, Problem, AvailableSolvers

from sympy.abc import x, y
import sympy as sp



def test_1x1() -> None:
    # essentially, maximize -x with x >= 0 and x == 1 and x in R^1
    moment_matrix = MomentMatrixSDP(1, [[(0, 0)]])
    p = ProblemSDP(moment_matrix, np.array([[-1]]))

    solution = SolverRegistry.solve(p, AvailableSolvers.CVXPY)
    assert solution is not None
    dual_objective_value = solution.dual_objective_value
    dual_variable = solution.dual_variables
    print (len(dual_variable))

    # dual problem resolved by cvxpy 
    x = cp.Variable()
    constraints = [ x == 1]
    obj = cp.Maximize(-x)
    prob = cp.Problem(obj, constraints)
    prob.solve()

    dual_variable_theo = []
    for i in range (len(constraints)):
        dual_variable_theo.append(constraints[i].dual_value)

    assert np.abs( - 1 - dual_objective_value) <= 0.001 and  \
    [np.abs(dual_variable_theo[i] - dual_variable[i]) <= 0.001 for i in range (len (constraints))]


def test() -> None:
    
    obj = -y**2  - y

    pol1 = x - x**2
    #pol2 = - x * x + x
    pol3 = y - y**2

    #c1 = Constraint.InequalityConstraint(pol1)
    #c2 = Constraint.InequalityConstraint(pol2)
    #c3 = Constraint.InequalityConstraint(pol3)

    problem = Problem(obj)
   # problem.add_constraint(c1)
   # problem.add_constraint(c2)
   # problem.add_constraint(c3)

    problem.solve(relaxation_order= 1, solver= AvailableSolvers.CVXPY)

    sosDecomposition = problem.compute_sos_decomposition()
    assert sosDecomposition is not None
    print(sp.expand(sosDecomposition.reconstructed_objective()))
    assert np.abs(sosDecomposition.objective_error(problem)) < 0.5
   
