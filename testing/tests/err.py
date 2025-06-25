from ncpol3sdpa import Problem, Constraint, AvailableSolvers
from sympy.abc import x, y

def test_mosek() -> None:
    pb = Problem(-x*x-y)
    pb.add_constraint(Constraint.EqualityConstraint(y-1))
    pb.solve(solver=AvailableSolvers.MOSEK)

def test_cvxpy() -> None:
    pb = Problem(-x*x-y)
    pb.add_constraint(Constraint.EqualityConstraint(y-1))
    pb.solve(solver=AvailableSolvers.CVXPY)

if __name__ == "__main__":
    
    test_mosek()
    test_cvxpy()

    print("All tests passed.")