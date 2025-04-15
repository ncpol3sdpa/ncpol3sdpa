# from numpy import format_float_scientific
from ncpol3sdpa.problem import Problem, AvailableSolvers
from ncpol3sdpa.constraints import Constraint
from sympy.abc import x, y
from sympy import Expr
from sympy.physics.quantum import HermitianOperator


def test_1() -> None:
    obj = 2 * x * y
    p = Problem(obj)
    c1 = Constraint.EqualityConstraint(x * x - x)
    c2 = Constraint.InequalityConstraint(-y * y + y + 0.25)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve(1) - 2.4142) <= 0.01
    assert abs(p.solve(2) - 2.4142) <= 0.01
    assert abs(p.solve(3) - 2.4142) <= 0.01
    assert abs(p.solve(1, AvailableSolvers.MOSEK) - 2.4142) <= 0.01
    assert abs(p.solve(2, AvailableSolvers.MOSEK) - 2.4142) <= 0.01
    assert abs(p.solve(3, AvailableSolvers.MOSEK) - 2.4142) <= 0.01


def test_2() -> None:
    obj = y**2 - x * y - y
    c1 = Constraint(False, x - x**2)
    c2 = Constraint(False, y - y**2)
    p = Problem(obj)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve(1)) <= 1
    assert abs(p.solve(2)) <= 0.1
    assert abs(p.solve(3)) <= 0.001
    assert abs(p.solve(1, AvailableSolvers.MOSEK)) <= 1
    assert abs(p.solve(2, AvailableSolvers.MOSEK)) <= 0.1
    assert abs(p.solve(3, AvailableSolvers.MOSEK)) <= 0.001


def test_3() -> None:
    obj: Expr = -(x**2) + 10
    p = Problem(obj)
    assert abs(p.solve(1) - 10) <= 1
    assert abs(p.solve(2) - 10) <= 0.1
    assert abs(p.solve(3) - 10) <= 0.001
    assert abs(p.solve(1, AvailableSolvers.MOSEK) - 10) <= 1
    assert abs(p.solve(2, AvailableSolvers.MOSEK) - 10) <= 0.1
    assert abs(p.solve(3, AvailableSolvers.MOSEK) - 10) <= 0.001


# Issue with cvxpy ??
def test_4() -> None:
    obj = y * (-(x**2) + 2)
    c1 = Constraint.EqualityConstraint(y - 10, substitution=True)
    p = Problem(obj)
    p.add_constraint(c1)
    assert abs(p.solve(2) - 20) <= 0.1
    assert abs(p.solve(3) - 20) <= 0.001
    assert abs(p.solve(2, AvailableSolvers.MOSEK) - 20) <= 0.1
    assert abs(p.solve(3, AvailableSolvers.MOSEK) - 20) <= 0.001


def test_1_sub() -> None:
    obj = 2 * x * y
    p = Problem(obj)
    c1 = Constraint.EqualityConstraint(x * x - x, substitution=True)
    c2 = Constraint.EqualityConstraint(-y * y + y + 0.25)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve(1) - 2.4142) <= 0.01
    assert abs(p.solve(2) - 2.4142) <= 0.01
    assert abs(p.solve(3) - 2.4142) <= 0.01
    assert abs(p.solve(1, AvailableSolvers.MOSEK) - 2.4142) <= 0.01
    assert abs(p.solve(2, AvailableSolvers.MOSEK) - 2.4142) <= 0.01
    assert abs(p.solve(3, AvailableSolvers.MOSEK) - 2.4142) <= 0.01


def test_1_nc() -> None:
    a: HermitianOperator = HermitianOperator("a")  # type: ignore
    b: HermitianOperator = HermitianOperator("b")  # type: ignore

    obj = a**2 - 0.5 * a * b - 0.5 * b * a - a
    p = Problem(obj, commutative=False)
    c1 = Constraint.InequalityConstraint(a - a**2)
    c2 = Constraint.InequalityConstraint(b - b**2)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve(2) - 1 / 8) <= 0.1


def test_2_nc() -> None:
    a: HermitianOperator = HermitianOperator("a")  # type: ignore
    b: HermitianOperator = HermitianOperator("b")  # type: ignore

    obj = a * b + b * a
    p = Problem(obj, commutative=False)
    c1 = Constraint.InequalityConstraint(1 - a**2 - b**2)
    p.add_constraint(c1)
    assert abs(p.solve(2) - 1) <= 0.1


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_1_sub()
    print("Everything passed")
