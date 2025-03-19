from __future__ import annotations
from typing import List, Dict, Any
import sympy as sp
from sympy import Expr, S

# from sympy.ntheory import generate

from ncpol3sdpa.rules import Rule, apply_rule_to_polynom
from ncpol3sdpa.momentmatrix import create_moment_matrix_cvxpy, create_constraints_matrix_cvxpy
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.solver import Solver
from ncpol3sdpa.constraints import Constraint


def polynom_linearized(
        variable_of_monomial : Dict[Any,Any],
        polynom : Expr,
        rules : Dict[Expr,Expr]
    ) -> Expr:
    """Return the linearized polynom"""
    # 2*X*Y -> 2 Y_(i,j)

    polynom = apply_rule_to_polynom(polynom, rules)
    dict_monoms : Dict[Any,Any]
    dict_monoms = polynom.expand().as_coefficients_dict()
    combination : Expr = S.Zero
    for key, value in dict_monoms.items():
        combination += value * variable_of_monomial[key]
    return combination


class Problem:
    def __init__(self, obj : Expr) -> None:
        self.constraints : List[Constraint] = []
        self.objective : Expr = obj

    def add_constraint(self, constraint : Constraint) -> None:
        self.constraints.append(constraint)

    def solve(self, relaxation_order: int = 1) -> float:
        """Solve the polynomial optimization problem using SDP relaxation.

        This function implements the Lasserre hierarchy to solve polynomial optimization
        problems through the following steps:
        1. Generate substitution rules from equality constraints
        2. Generate monomials for the moment matrix
        3. Build the moment matrix
        4. Construct constraint matrices for both equality and inequality constraints
        5. Linearize objective function
        6. Solve the resulting SDP problem

        Args:
            relaxation_order (int): The order of relaxation in Lasserre hierarchy.
                Higher orders give better approximations but increase complexity.
                Defaults to 1.

        Returns:
            float: The optimal value of the objective function

        Example:
            >>> problem = Problem(x**2 + y**2)  # minimize x^2 + y^2
            >>> problem.add_constraint(Constraint(x**2 + y**2 - 1))  # subject to x^2 + y^2 >= 1
            >>> result = problem.solve(relaxation_order=2)
        """
        # Step 1: Handle substitution rules
        rules = Rule.of_constraints([
            constraint 
            for constraint in self.constraints 
            if constraint.substitution
        ])

        # Step 2: Generate monomials
        all_symbols = list(self.objective.free_symbols)
        all_monomials : List[Expr] = [
            monom
            for monom in generate_monomials_commutative(
                all_symbols, relaxation_order
            )
            if monom not in rules
        ]

        # Step 3: Build moment matrix
        moment_matrix, variable_of_monomial = create_moment_matrix_cvxpy(
            all_monomials, rules
        )

        # Step 4: Build constraint matrices
        # 4a. Equality constraints
        constraint_maricies_equal = [
            create_constraints_matrix_cvxpy(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(relaxation_order - (sp.total_degree(constraint.polynom) / 2)),
                ),
                constraint.polynom,
                rules,
            )
            for constraint in self.constraints
            if constraint.is_equality_constraint and not constraint.substitution
        ]

        # 4b. Inequality (positivity) constraints
        constraint_maricies_positiv = [
            create_constraints_matrix_cvxpy(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(relaxation_order - (sp.total_degree(self.constraints[i].polynom) / 2)),
                ),
                self.constraints[i].polynom,
                rules,
            )
            for i in range(len(self.constraints))
            if not self.constraints[i].is_equality_constraint
        ]

        # Step 5: Linearize objective function
        poly_obj = polynom_linearized(
            variable_of_monomial, 
            self.objective, 
            rules
        )

        # Step 6: Solve SDP
        return Solver.solve_cvxpy(
            poly_obj,
            len(moment_matrix),
            moment_matrix,
            constraint_maricies_positiv,
            constraint_maricies_equal,
        )
