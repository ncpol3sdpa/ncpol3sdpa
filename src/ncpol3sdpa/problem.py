from __future__ import annotations
from typing import List, Dict, Any
import sympy as sp
# from sympy.ntheory import generate

from ncpol3sdpa.rules import Rule
from ncpol3sdpa.momentmatrix import create_moment_matrix_cvxpy, create_constraints_matrix_cvxpy
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.solver import Solver
from ncpol3sdpa.constraints import Constraint
from semidefinite_program_repr import ProblemSDP


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

    def relax_to_sdp(self, relaxation_order : int) -> ProblemSDP:
        # # 1. Generates all monomials
        # # Assumes that no extra symbols in the objectives, for now
        # all_symbols = self.objective.free_symbols

        # all_monomials = generate_monomials_commutative(
        #     all_symbols, relaxation_order
        # )

        # # 2. Substitute the equality constraints
        # #        - rules.py ?
        # # skip for now, we create constraint matrix = 0 for now
        # rules = Rule.of_constraints([
        #     constraint 
        #     for constraint in self.constraints 
        #     if constraint.substitution
        # ])

        # for monom in rules:
        #     if monom in all_monomials:
        #         all_monomials.remove(monom)

        # # 3. Start to build the  SDP relaxation

        # n : int = len(all_monomials)
        # index_var : int = 0
        # variable_of_monomial : Dict[sp.Poly, Any] = {}
        # moment_matrix : List[List[sp.Poly]] = [[0 for _ in range(n)] for _ in range(n)]

        # for i, monom1 in enumerate(all_monomials):
        #     for j, monom2 in enumerate(all_monomials):
        #         monom : sp.Poly = apply_rule(monom1 * monom2, rules)
        #         if monom not in variable_of_monomial:
        #             variable_of_monomial[monom] = sp.symbols(f"y{index_var}")
        #             index_var += 1
        #         moment_matrix[i][j] = variable_of_monomial[monom]

        # return moment_matrix, variable_of_monomial
        

    def solve(self, relaxation_order: int = 1) -> float:
        """Return the solution of the problem"""

        # 1. Generates all monomials
        # Assumes that no extra symbols in the objectives, for now

        all_symbols = self.objective.free_symbols

        all_monomials = generate_monomials_commutative(
            all_symbols, relaxation_order
        )

        # 2. Substitute the equality constraints
        #        - rules.py ?
        # skip for now, we create constraint matrix = 0 for now
        rules = Rule.of_constraints([
            constraint 
            for constraint in self.constraints 
            if constraint.substitution
        ])

        for monom in rules:
            if monom in all_monomials:
                all_monomials.remove(monom)

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

        constraint_matrices_positive = [
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
            constraint_matrices_positive,
            constraint_maricies_equal,
        )
