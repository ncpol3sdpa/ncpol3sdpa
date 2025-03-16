from __future__ import annotations
from typing import List, Dict, Any
import sympy as sp
# from sympy.ntheory import generate

from ncpol3sdpa.rules import Rule
from ncpol3sdpa.momentmatrix import create_moment_matrix_cvxpy, create_constraints_matrix_cvxpy
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.solver import Solver
from ncpol3sdpa.constraints import Constraint


def polynom_linearized(
        variable_of_monomial : Dict[Any,Any],
        polynom : sp.Poly
    ) -> sp.Expr:
    dict_monoms : Dict[Any,Any]
    dict_monoms = polynom.expand().as_coefficients_dict()
    combination = 0
    for key, value in dict_monoms.items():
        combination += value * variable_of_monomial[key]
    return combination


class Problem:
    def __init__(self, obj : sp.Symbol) -> None:
        self.constraints : List[Constraint] = []
        self.objective = obj

    def add_constraint(self, constraint : Constraint) -> None:
        self.constraints.append(constraint)

    def solve(self, relaxation_order: int = 1) -> float:
        """Return the solution of the problem"""

        # 1. Generates all monomials
        # Assumes that no extra symbols in the objectives, for now


        all_symbols = self.objective.free_symbols

        all_monomials = generate_monomials_commutative(
            all_symbols, relaxation_order
        )

        rules = Rule.of_constraints([
            constraint 
            for constraint in self.constraints 
            if constraint.substitution
        ])

        for monom in rules:
            if monom in all_monomials:
                all_monomials.remove(monom)

        # 2. Substitute the equality constraints
        #        - rules.py ?
        # skip for now, we create constraint matrix = 0 for now

        # 3. Build the moment matrix
        #        - momentmatrix.py

        moment_matrix, variable_of_monomial = create_moment_matrix_cvxpy(
            all_monomials, rules
        )

        print(rules)
        print(variable_of_monomial)
        print(moment_matrix)

        # 4. Build constraints matrices
        #        - momentmatrix.py

        constraint_maricies_equal = [
            create_constraints_matrix_cvxpy(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(
                        relaxation_order
                        - (sp.total_degree(self.constraints[i].polynom) / 2)
                    ),
                ),
                self.constraints[i].polynom,
                rules,
            )
            for i in range(len(self.constraints))
            if self.constraints[i].is_equality_constraint and (not self.constraints[i].substitution)
        ]

        constraint_maricies_positiv = [
            create_constraints_matrix_cvxpy(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(
                        relaxation_order
                        - (sp.total_degree(self.constraints[i].polynom) / 2)
                    ),
                ),
                self.constraints[i].polynom,
                rules,
            )
            for i in range(len(self.constraints))
            if not self.constraints[i].is_equality_constraint
        ]
        


        poly_obj = polynom_linearized(variable_of_monomial, self.objective)

        # 5. Solve the SDP (Solver.solve)
        #        - solver.py
        # CF ex3_cvxpy.py

        return Solver.solve(
            poly_obj,
            len(moment_matrix),
            moment_matrix,
            constraint_maricies_positiv,
            constraint_maricies_equal,
        )
