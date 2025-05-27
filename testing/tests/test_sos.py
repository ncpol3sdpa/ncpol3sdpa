# TODO

import numpy as np

# from typing import List
from ncpol3sdpa import AvailableSolvers

from ncpol3sdpa import Problem

from sympy.abc import x, y
import sympy as sp


def objective_only_test(obj: sp.Expr) -> None:
    problem = Problem(obj)

    # TODO Bug in mosek
    for solver in [AvailableSolvers.MOSEK, AvailableSolvers.CVXPY]:
        print("solver: ", solver)
        problem.solve(relaxation_order=1, solver=solver)

        sosDecomposition = problem.compute_sos_decomposition()
        assert sosDecomposition is not None
        assert np.abs(sosDecomposition.objective_error(problem.algebraSDP)) < 0.01


def test1() -> None:
    objective_only_test(-(y**2) - y)


def test2() -> None:
    objective_only_test(sp.expand(-(x**2) - (3 * x - 6 * y) ** 2 + 7 * x - 4 * y + 12))


def test3() -> None:
    objective_only_test(sp.expand(-(x**2) - (3 * x - 6 * y) ** 2 + 12))
