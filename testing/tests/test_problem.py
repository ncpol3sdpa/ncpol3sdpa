# from numpy import format_float_scientific
from sympy.abc import x, y
from sympy import Expr, symbols, I
from sympy.physics.quantum import HermitianOperator

from ncpol3sdpa import Constraint, Problem, AvailableSolvers


def test_1() -> None:
    obj = 2 * x * y
    p = Problem(obj, is_real=True)
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
    c1 = Constraint.EqualityConstraint(x - x**2)
    c2 = Constraint.EqualityConstraint(y - y**2)
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
    p = Problem(obj, is_commutative=False)
    c1 = Constraint.InequalityConstraint(a - a**2)
    c2 = Constraint.InequalityConstraint(b - b**2)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve(2) - 1 / 8) <= 0.1


def test_2_nc() -> None:
    a: HermitianOperator = HermitianOperator("a")  # type: ignore
    b: HermitianOperator = HermitianOperator("b")  # type: ignore

    obj = a * b + b * a
    p = Problem(obj, is_commutative=False)
    c1 = Constraint.InequalityConstraint(1 - a**2 - b**2)
    p.add_constraint(c1)
    assert abs(p.solve(2) - 1) <= 0.1


def test_3_nc() -> None:
    a: HermitianOperator = HermitianOperator("a")  # type: ignore
    b: HermitianOperator = HermitianOperator("b")  # type: ignore

    obj = a**2 - 0.5 * a * b - 0.5 * b * a - a
    p = Problem(obj, is_commutative=False)
    c1 = Constraint.InequalityConstraint(a - a**2)
    c2 = Constraint.InequalityConstraint(b - b**2)
    c3 = Constraint.EqualityConstraint(a * b - b * a)
    p.add_constraint(c1)
    p.add_constraint(c2)
    p.add_constraint(c3)
    assert abs(p.solve(3)) <= 0.1


def test_complex_1() -> None:
    z = symbols("z", is_real=False)
    obj = z + z.conjugate()
    p = Problem(obj, is_real=False)
    c1 = Constraint.InequalityConstraint(-z * z.conjugate() + 1)
    c2 = Constraint.EqualityConstraint(z - z.conjugate())
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve(2) - 2) <= 0.1
    assert abs(p.solve(3) - 2) <= 0.1


def test_complex_2() -> None:
    z1, z2 = symbols("z1 z2", is_real=False)
    obj = (z1 + z1.conjugate()) / 2
    p = Problem(obj, is_real=False)
    c1 = Constraint.InequalityConstraint(-z1 * z1.conjugate() + 4)
    c2 = Constraint.InequalityConstraint(-z2 * z2.conjugate() + 1)
    c3 = Constraint.EqualityConstraint(
        (z2 + z2.conjugate()) / 2 - (z2 - z2.conjugate()) / (2 * I)
    )
    c4 = Constraint.EqualityConstraint(
        (z1 + z1.conjugate()) / 2 - (z2 + z2.conjugate()) / 2
    )
    p.add_constraint(c1)
    p.add_constraint(c2)
    p.add_constraint(c3)
    p.add_constraint(c4)
    assert abs(p.solve(3) - 0.7071) <= 0.1
