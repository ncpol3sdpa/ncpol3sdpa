from copy import deepcopy

import numpy as np
from sympy.abc import x, y
import sympy as sp

# from typing import List
from ncpol3sdpa import AvailableSolvers
from ncpol3sdpa import Problem
from ncpol3sdpa import Constraint


solvers = [AvailableSolvers.CVXPY, AvailableSolvers.MOSEK]


def verify_test(problem: Problem, k: int = 1) -> None:
    for solver in solvers:
        # The problem should be solved only once
        prob_copy = deepcopy(problem)

        print("solver: ", solver)
        prob_copy.solve(relaxation_order=k, solver=solver)

        sosDecomposition = prob_copy.compute_sos_decomposition()
        assert sosDecomposition is not None
        assert np.abs(sosDecomposition.objective_error(prob_copy.algebraSDP)) < 0.01


def test1() -> None:
    problem = Problem(-(y**2) - y)
    verify_test(problem)


def test2() -> None:
    problem = Problem(sp.expand(-(x**2) - (3 * x - 6 * y) ** 2 + 7 * x - 4 * y + 12))
    verify_test(problem)


def test3() -> None:
    problem = Problem(sp.expand(-(x**2) - (3 * x - 6 * y) ** 2 + 12))
    verify_test(problem)


def test_eq_constraint() -> None:
    problem = Problem(sp.expand(-(x**2) - (3 * x - 6 * y) ** 2 + 12))
    problem.add_constraint(Constraint.EqualityConstraint(x * y + 6 - x**2))
    verify_test(problem, k=3)


def test_ineq_constraint() -> None:
    problem = Problem(sp.expand(-(x**2) - (3 * x - 6 * y) ** 2 + 12))
    problem.add_constraint(Constraint.InequalityConstraint(x * y + 6 - x**2))
    verify_test(problem, k=3)
