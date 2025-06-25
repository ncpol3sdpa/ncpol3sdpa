from copy import deepcopy

import numpy as np
from sympy.abc import x, y
import sympy as sp

# from typing import List
from ncpol3sdpa import AvailableSolvers
from ncpol3sdpa import Problem
from ncpol3sdpa import Constraint

from testing.draw_strategies.float_strategies import order_of_magnitude_floats
from testing.draw_strategies.polynomials import (
    sos_polynomials,
    three_symbols,
    two_symbols,
    one_symbol,
)
from hypothesis import given, settings
from hypothesis.strategies import sampled_from, integers

solvers = [
    # AvailableSolvers.MOSEK,
    AvailableSolvers.CVXPY,
]


def verify_test(problem: Problem, k: int = 1) -> None:
    for solver in solvers:
        # The problem should be solved only once
        prob_copy = deepcopy(problem)

        print("solver: ", solver)
        prob_copy.solve(relaxation_order=k, solver=solver)
        assert prob_copy.solution is not None

        sosDecomposition = prob_copy.compute_sos_decomposition()
        assert sosDecomposition is not None
        assert np.abs(sosDecomposition.objective_error(prob_copy.algebraSDP)) < 0.01


# --------- Manual tests ---------


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


def test_mosek_ilposed() -> None:
    problem = Problem(-sp.expand(1.0 + (0.005 * x + 1) ** 2))
    verify_test(problem, k=3)


# --------- Automatic property tests ---------


@settings(deadline=1000)
@given(
    sos_polynomials(
        three_symbols, expand=False, coefs=order_of_magnitude_floats, max_degree=1
    )
    | sos_polynomials(
        two_symbols, expand=False, coefs=order_of_magnitude_floats, max_degree=2
    )
    | sos_polynomials(
        one_symbol, expand=False, coefs=order_of_magnitude_floats, max_degree=2
    ),
    sampled_from(solvers),
    integers(min_value=3, max_value=4),
)
def test_bounded_no_constraints(
    sos_poly: sp.Expr, solver: AvailableSolvers, k: int
) -> None:
    sos_margin = 1.0
    sos_poly = sp.expand(sos_margin + sos_poly)
    problem = Problem(-sos_poly)

    problem.solve(relaxation_order=3, solver=solver)
    assert problem.solution is not None

    assert problem.solution.primal_objective_value <= -sos_margin + 0.001
    assert problem.solution.dual_objective_value <= -sos_margin + 0.001

    sosDecomposition = problem.compute_sos_decomposition()
    assert sosDecomposition is not None
    assert np.abs(sosDecomposition.objective_error(problem.algebraSDP)) < 0.01
