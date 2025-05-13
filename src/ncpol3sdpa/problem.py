from typing import List

from sympy import Expr
import sympy

from ncpol3sdpa.resolution.algebra import create_AlgebraSDP
from ncpol3sdpa.solvers import AvailableSolvers
from ncpol3sdpa.resolution import (
    Rule,
    Constraint,
    generate_needed_symbols,
)
from ncpol3sdpa.algebra_to_SDP import algebra_to_SDP


class Problem:
    def __init__(
        self, obj: sympy.Expr, is_commutative: bool = True, is_real: bool = True
    ) -> None:
        self.constraints: List[Constraint] = []
        self.objective: Expr = obj
        self.is_commutative = is_commutative
        self.is_real = is_real

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint)

    def add_constraints(self, constraints: List[Constraint]) -> None:
        for c in constraints:
            self.add_constraint(c)

    def solve(
        self,
        relaxation_order: int = 1,
        solver: AvailableSolvers = AvailableSolvers.CVXPY,
    ) -> float:
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

        # 0. Separate constraint types
        rules = Rule(
            [constraint for constraint in self.constraints if constraint.substitution]
        )

        normal_constraints = [
            constraint for constraint in self.constraints if not constraint.substitution
        ]

        # 1. Build algebraic formulation
        all_constraint_polynomials = [c.polynomial for c in self.constraints] + [
            self.objective
        ]
        needed_symbols = generate_needed_symbols(all_constraint_polynomials)
        algebraSDP = create_AlgebraSDP(
            needed_symbols,
            self.objective,
            relaxation_order,
            rules,
            self.is_commutative,
            self.is_real,
        )
        algebraSDP.add_constraints(normal_constraints)

        # 2. Translate to SDP
        problemSDP = algebra_to_SDP(algebraSDP)
        if not self.is_real:
            problemSDP = problemSDP.complex_to_realSDP()

        print(problemSDP)

        # 3. Solve the SDP
        return solver.solve(problemSDP)
