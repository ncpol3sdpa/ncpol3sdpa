from ncpol3sdpa import Problem, Constraint, SolverFactory
from sympy.abc import x, y

def test_mosek() -> None:
    pb = Problem(-x*x-y)
    pb.add_constraint(Constraint.EqualityConstraint(y-1))
    pb.solve(solver=SolverFactory.create_solver("mosek"))

def test_cvxpy() -> None:
    pb = Problem(-x*x-y)
    pb.add_constraint(Constraint.EqualityConstraint(y-1))
    pb.solve(solver=SolverFactory.create_solver("cvxpy"))

if __name__ == "__main__":
    
    test_mosek()
    test_cvxpy()

    print("All tests passed.")