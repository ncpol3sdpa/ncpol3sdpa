# import numpy as np
# from typing import Dict, Tuple, List
from ncpol3sdpa import Problem, Constraint
from sympy.physics.quantum import HermitianOperator
from ncpol3sdpa import AvailableSolvers


class Bell_inequality:
    @classmethod
    def create_hermitian_matrix(
        cls,
        A1: HermitianOperator,
        A2: HermitianOperator,
        B1: HermitianOperator,
        B2: HermitianOperator,
    ) -> HermitianOperator:
        return A1 * B1 + A1 * B2 + A2 * B1 - A2 * B2  # type: ignore

    @classmethod
    def solve_bell_inequality(cls) -> float:
        A1 = HermitianOperator("A1")  # type: ignore
        A2 = HermitianOperator("A2")  # type: ignore
        B1 = HermitianOperator("B1")  # type: ignore
        B2 = HermitianOperator("B2")  # type: ignore

        obj = Bell_inequality.create_hermitian_matrix(A1, A2, B1, B2)
        p = Problem(obj, is_commutative=False, is_real=False)

        c = Constraint.EqualityConstraint(A1**2 - 1)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(A2**2 - 1)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(B1**2 - 1)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(B2**2 - 1)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(A1 * B1 - B1 * A1)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(A2 * B1 - B1 * A2)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(A1 * B2 - B2 * A1)
        p.add_constraint(c)

        c = Constraint.EqualityConstraint(A2 * B2 - B2 * A2)
        p.add_constraint(c)

        """"
        p.add_rule ( A1 ** 2 , 1)
        p.add_rule ( A2 ** 2 , 1)
        p.add_rule ( B1 ** 2 , 1)
        p.add_rule ( B2 ** 2 , 1)

        p.add_rule(A1 * B1, B1*A1)
        p.add_rule(A2 * B1, B1*A2)
        p.add_rule(A1 * B2, B2*A1)
        p.add_rule(A2 * B2, B2*A2)
        """

        solution = p.solve(2, solver=AvailableSolvers.MOSEK)

        if solution is None:
            raise ValueError("No solution found for the Bell inequality problem.")
        return solution