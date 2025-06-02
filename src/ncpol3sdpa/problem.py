from typing import List

from sympy import Expr
import sympy

from ncpol3sdpa.solvers import AvailableSolvers, Solver, SolverRegistry
from ncpol3sdpa.resolution import (
    Rules,
    RulesCommutative,
    RulesNoncommutative,
    Constraint,
    create_AlgebraSDP,
    generate_needed_symbols,
)
from ncpol3sdpa.algebra_to_SDP import algebra_to_SDP
from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.sos import SosDecomposition, compute_sos_decomposition


class Problem:
    def __init__(
        self, obj: sympy.Expr, is_commutative: bool = True, is_real: bool = True
    ) -> None:
        self.constraints: List[Constraint] = []
        self.objective: Expr = obj
        self.is_commutative = is_commutative
        self.is_real = is_real
        self.solution: Solution_SDP | None = None
        self.rules: Rules = (
            RulesCommutative() if is_commutative else RulesNoncommutative()
        )

    def add_rule(self, old: Expr, new: Expr) -> None:
        """Adds the substitution rule old -> new to the problem. (variation of the constraint old = new)
        old and new MUST BE MONOMIALS"""
        # TODO: assert that old and new are monomials
        self.rules.add_rule(old, new)

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint)

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for c in constraints:
            self.add_constraint(c)

    def solve(
        self,
        relaxation_order: int = 1,
        solver: Solver | AvailableSolvers = AvailableSolvers.CVXPY,
    ) -> float | None:
        """Solve the polynomial optimization problem using SDP relaxation.

        Args:
            relaxation_order (int): The order of relaxation in Lasserre hierarchy.
                Higher orders give better approximations but increase complexity.
                Defaults to 1.

        Returns:
            float: An upper bound on the optimal value of the objective function

        Example:
            >>> problem = Problem(x**2 + y**2)  # minimize x^2 + y^2
            >>> problem.add_constraint(Constraint(x**2 + y**2 - 1))  # subject to x^2 + y^2 >= 1
            >>> result = problem.solve(relaxation_order=2)
        """

        normal_constraints = self.constraints

        # 1. Build algebraic formulation
        all_constraint_polynomials = [c.polynomial for c in self.constraints] + [
            self.objective
        ]
        needed_symbols = generate_needed_symbols(all_constraint_polynomials)
        algebraSDP = create_AlgebraSDP(
            needed_symbols,
            self.objective,
            relaxation_order,
            self.rules,
            self.is_commutative,
            self.is_real,
        )
        self.algebraSDP = algebraSDP
        algebraSDP.add_constraints(normal_constraints)

        # 2. Translate to SDP
        problemSDP = algebra_to_SDP(algebraSDP)
        if not self.is_real:
            problemSDP = problemSDP.complex_to_realSDP()
        # print(problemSDP)

        # 3. Solve the SDP
        if isinstance(solver, AvailableSolvers):
            solver = SolverRegistry.get_solver(solver)
        if isinstance(solver, Solver):
            self.solution = solver.solve(problemSDP)
        else:
            raise TypeError(
                f"Solver must be of type {Solver} or {AvailableSolvers}, not {type(solver)}"
            )

        if self.solution is not None:
            return self.solution.primal_objective_value
        else:
            return None

    def solve_uncheked(
        self,
        relaxation_order: int = 1,
        solver: Solver | AvailableSolvers = AvailableSolvers.CVXPY,
    ) -> float:
        """Same as solve, but will raise an exception if there was no solution"""
        res = self.solve(relaxation_order=relaxation_order, solver=solver)
        assert res is not None, "Could not find solution"
        return res

    def compute_sos_decomposition(self) -> SosDecomposition:
        """Returns a Sum of Squares decomposition of (lambda - objective).
        See sos_duality_derivation.md for more details.
        The `solve` function must be called and must have succeeded before this function can be called.
        """

        assert self.solution is not None, (
            "Solution not found: `solve` was not called or a solution was not found"
        )
        assert self.algebraSDP is not None, "Could not find algebra"

        return compute_sos_decomposition(
            solution=self.solution, problem_algebra=self.algebraSDP
        )
