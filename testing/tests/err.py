from ncpol3sdpa import Problem, Constraint, SolverList
from sympy.abc import x, y


def test_mosek() -> None:
    pb = Problem(-x * x - y)
    pb.add_constraint(Constraint.EqualityConstraint(y - 1))
    pb.solve(solver=SolverList.MOSEK)


def test_cvxpy() -> None:
    pb = Problem(-x * x - y)
    pb.add_constraint(Constraint.EqualityConstraint(y - 1))
    pb.solve(solver=SolverList.CVXPY)


if __name__ == "__main__":
    test_cvxpy()
    test_mosek()

    print("All tests passed.")
