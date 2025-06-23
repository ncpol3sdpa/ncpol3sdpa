from copy import deepcopy

import numpy as np
from sympy.abc import x, y, z
import sympy as sp

# from typing import List
from ncpol3sdpa import AvailableSolvers
from ncpol3sdpa import Problem
from ncpol3sdpa import Constraint

from testing.draw_strategies.float_strategies import order_of_magnitude_floats
from testing.draw_strategies.polynomials import (
    polynomials,
    sos_polynomials,
    three_symbols,
    two_symbols,
    one_symbol,
)
from hypothesis import given, settings
from hypothesis.strategies import sampled_from

solvers = [AvailableSolvers.MOSEK]  # , AvailableSolvers.CVXPY]


def verify_test(problem: Problem, k: int = 1) -> None:
    for solver in solvers:
        # The problem should be solved only once
        prob_copy = deepcopy(problem)

        print("solver: ", solver)
        prob_copy.solve(relaxation_order=k, solver=solver)
        assert prob_copy.solution is not None

        print(prob_copy.solution.primal_objective_value)
        print(prob_copy.solution.dual_objective_value)

        sosDecomposition = prob_copy.compute_sos_decomposition()
        assert sosDecomposition is not None
        print(sp.expand(sosDecomposition.reconstructed_objective()))
        print((sosDecomposition.reconstructed_objective()))
        assert np.abs(sosDecomposition.objective_error(prob_copy.algebraSDP)) < 0.05


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
    verify_test(problem, k=5)


def test_failing() -> None:
    # This is sos
    p1 = (
        203.655826479035 * x**2
        - 336.661012226743 * x * z
        - 133.085609676013 * x
        + 1.0 * y**2
        - 20.0 * y * z
        + 294.273570504449 * z**2
        + 287.022169905708 * z
        + 163.816502149217
    )
    problem = Problem(p1)
    verify_test(problem, k=3)


def test_failing2() -> None:
    problem = Problem(10.0 * x**2)
    problem.add_constraint(Constraint.InequalityConstraint(1 - x**2))
    problem.add_constraint(Constraint.InequalityConstraint(1 - y**2))

    verify_test(problem, k=3)


# --------- Automatic property tests ---------


@settings(deadline=1000)
@given(
    sos_polynomials(
        three_symbols, expand=False, coefs=order_of_magnitude_floats(1), max_degree=1
    )
    | sos_polynomials(
        two_symbols, expand=False, coefs=order_of_magnitude_floats(1), max_degree=2
    )
    | sos_polynomials(
        one_symbol, expand=False, coefs=order_of_magnitude_floats(1), max_degree=2
    ),
    sampled_from(solvers),
)
def test_bounded_no_constraints(sos_poly: sp.Expr, solver: AvailableSolvers) -> None:
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


@settings(deadline=2000)
@given(
    polynomials(two_symbols, coefs=order_of_magnitude_floats(1), max_degree=2),
    sampled_from(solvers),
)
def test_bounded_monomials(poly: sp.Expr, solver: AvailableSolvers) -> None:
    problem = Problem(poly)
    problem.add_constraint(Constraint.InequalityConstraint(1 - two_symbols[0] ** 2))
    problem.add_constraint(Constraint.InequalityConstraint(1 - two_symbols[1] ** 2))

    problem.solve(relaxation_order=3, solver=solver)
    assert problem.solution is not None

    sosDecomposition = problem.compute_sos_decomposition()
    assert sosDecomposition is not None
    assert np.abs(sosDecomposition.objective_error(problem.algebraSDP)) < 0.05


@settings(deadline=2000)
@given(
    order_of_magnitude_floats(1, can_be_zero=False, positive_only=True),
    order_of_magnitude_floats(1, can_be_zero=False, positive_only=True),
    polynomials(
        two_symbols,
        coefs=order_of_magnitude_floats(1),
        max_degree=2,
    ).filter(lambda p: p != 0),
    sampled_from(solvers),
)
def test_ellipsis_monomials(
    a: float, b: float, poly: sp.Expr, solver: AvailableSolvers
) -> None:
    problem = Problem(poly)
    problem.add_constraint(
        Constraint.EqualityConstraint(
            -1 + a * two_symbols[0] ** 2 + a * two_symbols[1] ** 2
        )
    )

    problem.solve(relaxation_order=3, solver=solver)
    assert problem.solution is not None

    sosDecomposition = problem.compute_sos_decomposition()
    assert sosDecomposition is not None
    assert np.abs(sosDecomposition.objective_error(problem.algebraSDP)) < 0.05
