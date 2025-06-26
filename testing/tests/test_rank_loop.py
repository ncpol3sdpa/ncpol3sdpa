from sympy.abc import x, y
from ncpol3sdpa import rank_loop
from ncpol3sdpa import Constraint, Problem


def test_1() -> None:
    obj = -y
    p = Problem(obj, is_real=True)
    c1 = Constraint.InequalityConstraint(3 - 2 * y - x * x - y * y)
    c2 = Constraint.EqualityConstraint(-x - y - x * y)
    c3 = Constraint.InequalityConstraint(1 + x * y)
    p.add_constraint(c1)
    p.add_constraint(c2)
    p.add_constraint(c3)

    r = rank_loop.rank_loop(p)

    assert (4 - r) >= 0 and abs(p.solve_unchecked(3) - 0.618) <= 0.01


def test_2() -> None:
    obj = 2 * x * y
    p = Problem(obj, is_real=True)
    c1 = Constraint.EqualityConstraint(x * x - x)
    c2 = Constraint.InequalityConstraint(-y * y + y + 0.25)
    p.add_constraint(c1)
    p.add_constraint(c2)

    r = rank_loop.rank_loop(p)

    assert (4 - r) >= 0 and abs(p.solve_unchecked(3) - 2.414) <= 0.01
