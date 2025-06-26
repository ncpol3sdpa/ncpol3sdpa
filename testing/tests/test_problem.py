# from numpy import format_float_scientific
from sympy.abc import x, y
from sympy import S
from sympy import Expr, symbols, I
from sympy.physics.quantum import HermitianOperator, Operator

from ncpol3sdpa import Constraint, Problem, SolverList


def test_1() -> None:
    obj = 2 * x * y
    p = Problem(obj, is_real=True)
    c1 = Constraint.EqualityConstraint(x * x - x)
    c2 = Constraint.InequalityConstraint(-y * y + y + 0.25)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve_unchecked(1) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(2) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(3) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(1, SolverList.MOSEK) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(2, SolverList.MOSEK) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(3, SolverList.MOSEK) - 2.4142) <= 0.01


def test_2() -> None:
    obj = y**2 - x * y - y
    c1 = Constraint.EqualityConstraint(x - x**2)
    c2 = Constraint.EqualityConstraint(y - y**2)
    p = Problem(obj)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve_unchecked(1)) <= 1
    assert abs(p.solve_unchecked(2)) <= 0.1
    assert abs(p.solve_unchecked(3)) <= 0.001
    assert abs(p.solve_unchecked(1, SolverList.MOSEK)) <= 1
    assert abs(p.solve_unchecked(2, SolverList.MOSEK)) <= 0.1
    assert abs(p.solve_unchecked(3, SolverList.MOSEK)) <= 0.001


def test_3() -> None:
    obj: Expr = -(x**2) + 10
    p = Problem(obj)
    assert abs(p.solve_unchecked(1) - 10) <= 1
    assert abs(p.solve_unchecked(2) - 10) <= 0.1
    assert abs(p.solve_unchecked(3) - 10) <= 0.001
    assert abs(p.solve_unchecked(1, SolverList.MOSEK) - 10) <= 1
    assert abs(p.solve_unchecked(2, SolverList.MOSEK) - 10) <= 0.1
    assert abs(p.solve_unchecked(3, SolverList.MOSEK) - 10) <= 0.001


def test_4() -> None:
    obj = y * (-(x**2) + 2)
    p = Problem(obj)
    p.add_rule(y, 10 * S.One)
    assert abs(p.solve_unchecked(2) - 20) <= 0.1
    assert abs(p.solve_unchecked(3) - 20) <= 0.001
    assert abs(p.solve_unchecked(2, SolverList.MOSEK) - 20) <= 0.1
    assert abs(p.solve_unchecked(3, SolverList.MOSEK) - 20) <= 0.001


def test_1_sub() -> None:
    obj = 2 * x * y
    p = Problem(obj)
    constraint = Constraint.EqualityConstraint(-y * y + y + 0.25)
    p.add_constraint(constraint)
    p.add_rule(x * x, x)
    assert abs(p.solve_unchecked(1) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(2) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(3) - 2.4142) <= 0.01
    assert abs(p.solve_unchecked(1, SolverList.MOSEK)) - 2.4142 <= 0.01
    assert abs(p.solve_unchecked(2, SolverList.MOSEK)) - 2.4142 <= 0.01
    assert abs(p.solve_unchecked(3, SolverList.MOSEK)) - 2.4142 <= 0.01


def test_1_nc() -> None:
    a: HermitianOperator = HermitianOperator("a")  # type: ignore
    b: HermitianOperator = HermitianOperator("b")  # type: ignore

    obj = a**2 - 0.5 * a * b - 0.5 * b * a - a
    p = Problem(obj, is_commutative=False)
    c1 = Constraint.InequalityConstraint(a - a**2)
    c2 = Constraint.InequalityConstraint(b - b**2)
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve_unchecked(2) - 1 / 8) <= 0.1


def test_2_nc() -> None:
    a: HermitianOperator = HermitianOperator("a")  # type: ignore
    b: HermitianOperator = HermitianOperator("b")  # type: ignore

    obj = a * b + b * a
    p = Problem(obj, is_commutative=False)
    c1 = Constraint.InequalityConstraint(1 - a**2 - b**2)
    p.add_constraint(c1)
    assert abs(p.solve_unchecked(2) - 1) <= 0.1


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
    assert abs(p.solve_unchecked(3)) <= 0.1


def test_complex_1() -> None:
    z = symbols("z", is_real=False)
    obj = z + z.conjugate()
    p = Problem(obj, is_real=False)
    c1 = Constraint.InequalityConstraint(-z * z.conjugate() + 1)
    c2 = Constraint.EqualityConstraint(z - z.conjugate())
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve_unchecked(2) - 2) <= 0.1
    assert abs(p.solve_unchecked(3) - 2) <= 0.1


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
    assert abs(p.solve_unchecked(3) - 0.7071) <= 0.1


def test_nc_complex_1() -> None:
    X1 = HermitianOperator("X1")  # type: ignore
    X2 = HermitianOperator("X2")  # type: ignore
    obj = -(X1**2) - X2**2 - I * (X1 * X2 - X2 * X1)
    p = Problem(obj, is_commutative=False, is_real=False)
    c1 = Constraint.InequalityConstraint(1 - X1**2 - X2**2)
    p.add_constraint(c1)
    assert abs(p.solve_unchecked(2)) <= 0.1


def test_nc_complex_2() -> None:
    X1 = Operator("X1")  # type: ignore
    X2 = HermitianOperator("X2")  # type: ignore
    obj = -(X1**2) - X2**2 - I * (X1 * X2 - X2 * X1)
    p = Problem(obj, is_commutative=False, is_real=False)
    c1 = Constraint.InequalityConstraint(1 - X1**2 - X2**2)
    c2 = Constraint.EqualityConstraint(X1 - X1.adjoint())  # type: ignore
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve_unchecked(2)) <= 0.1


def test_trace_inequality() -> None:
    X1 = HermitianOperator("X1")  # type: ignore
    X2 = HermitianOperator("X2")  # type: ignore
    obj = -1 * (X1 * X2 + X2 * X1).adjoint() * (X1 * X2 + X2 * X1)
    p = Problem(obj, is_commutative=False, is_real=False)
    c1 = Constraint.LocalInequalityConstraint(X1 * X2 + X2 * X1)
    p.add_constraint(c1)
    assert abs(p.solve_unchecked(2)) <= 0.1
    assert abs(p.solve_unchecked(3, SolverList.MOSEK)) <= 0.0001


def test_nc_agebra_commute() -> None:
    A0 = HermitianOperator("A0")  # type: ignore
    A1 = HermitianOperator("A1")  # type: ignore
    B0 = HermitianOperator("B0")  # type: ignore
    B1 = HermitianOperator("B1")  # type: ignore
    obj = A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1
    p = Problem(
        obj, is_commutative=False, is_real=False, commute_variables=[[A0, A1], [B0, B1]]
    )
    p.add_constraint(Constraint.EqualityConstraint(A0 * A0 - 1))
    p.add_constraint(Constraint.EqualityConstraint(A1 * A1 - 1))
    p.add_constraint(Constraint.EqualityConstraint(B0 * B0 - 1))
    p.add_constraint(Constraint.EqualityConstraint(B1 * B1 - 1))

    # p.add_constraint(Constraint.EqualityConstraint(A0 * B0 - B0 * A0))
    # p.add_constraint(Constraint.EqualityConstraint(A0 * B1 - B1 * A0))
    # p.add_constraint(Constraint.EqualityConstraint(A1 * B0 - B0 * A1))
    # p.add_constraint(Constraint.EqualityConstraint(A1 * B1 - B1 * A1))

    # val2 = p.solve_unchecked(2)
    val3 = p.solve_unchecked(2, solver=SolverList.MOSEK)

    # assert abs(val2 - 2.82842712475) <= 0.1
    assert abs(val3 - 2.82842712475) <= 0.001


def test_add_variables() -> None:
    obj = -(x**2) + y
    c1 = Constraint.EqualityConstraint(y - 10)
    c2 = Constraint.InequalityConstraint(1 - x**3)
    p = Problem(obj, more_monomials=[x**2])
    p.add_constraint(c1)
    p.add_constraint(c2)
    assert abs(p.solve_unchecked(1) - 10) <= 0.1
