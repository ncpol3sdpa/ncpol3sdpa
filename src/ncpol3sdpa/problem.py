from __future__ import annotations
import sympy
import numpy as np
from typing import List, Dict, Tuple, Any
# from sympy.ntheory import generate

from ncpol3sdpa.rules import Rule
from ncpol3sdpa.momentmatrix import create_moment_matrix_cvxpy, create_constraints_matrix_cvxpy
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.solver import Solver
from ncpol3sdpa.constraints import Constraint
import ncpol3sdpa.semidefinite_program_repr as sdp_repr
import ncpol3sdpa.momentmatrix as momentmatrix
from ncpol3sdpa.semidefinite_program_repr import ProblemSDP, MomentMatrixSDP

def algebra_to_SDP_inequality_constraint(
    problem: ProblemSDP, 
    algebra : momentmatrix.AlgebraSDP,
    constraint_moment_matrix : List[List[sympy.Poly]]
) -> sdp_repr.EqConstraint :
    """Adds the translation of an inequality constraint"""
    constraint_matrix_size = len(constraint_moment_matrix)
    moment_matrix_size = problem.variable_sizes[problem.MOMENT_MATRIX_VAR_NUM]

    new_var = len(problem.variable_sizes)
    problem.variable_sizes.append(constraint_matrix_size)

    for i, row in enumerate(constraint_moment_matrix):
        for j, poly in enumerate(row):
            a_k = np.zeros(shape = (constraint_matrix_size, constraint_matrix_size))
            a_k[i][j] -= 0.5
            a_k[j][i] -= 0.5

            a_0 = np.zeros(shape = (moment_matrix_size,moment_matrix_size))
            for monomial, coef in poly.as_coefficients_dict().items():
                assert monomial in algebra.monomial_to_positions
                assert 0 < len(algebra.monomial_to_positions[monomial])
                x,y = algebra.monomial_to_positions[monomial][0]
                a_0[x][y] += 0.5*coef
                a_0[y][x] += 0.5*coef
    
    return sdp_repr.EqConstraint([(problem.MOMENT_MATRIX_VAR_NUM, a_0), (new_var, a_k)])


def algebra_to_SDP(algebra : momentmatrix.AlgebraSDP) -> ProblemSDP:
    """Convert the algebraic representation to the numeric SDP representation"""
    
    moment_matrix_size = len(algebra.moment_matrix)

    # Convert objective
    objective = np.zeros(shape = (moment_matrix_size, moment_matrix_size))
    for monomial, coef in algebra.objective.as_coefficients_dict().items():
        assert monomial in algebra.monomial_to_positions
        assert 0 < len(algebra.monomial_to_positions[monomial])
        #       v List of all the positions of this monomial in the matrix.
        (i,j) = algebra.monomial_to_positions[monomial][0]
        # The 0 is arbitrary (?) could be any other element of the list. 
        # TODO/Idea What happens if we chose other than 0? at random?
        
        # The objective must be symmetric
        objective[i][j] += 0.5 * coef
        objective[j][i] += 0.5 * coef
    
    # Moment matrix
    equiv_classes : List[List[Tuple[int, int]]] = \
        list(algebra.monomial_to_positions.values())
    
    moment_matrix_repr = MomentMatrixSDP(moment_matrix_size, equiv_classes)
     
    result_SDP = ProblemSDP(moment_matrix_repr, objective)

    # Translate Equality constraints
    #TODO

    # Translate Inequality constrains

    for constraint_matrix in algebra.constraint_moment_matrices:
        algebra.add_constraint(algebra_to_SDP_inequality_constraint(\
            result_SDP, algebra, constraint_matrix))

    return result_SDP 


def polynom_linearized(
        variable_of_monomial : Dict[Any,Any],
        polynom : sympy.Poly
    ) -> sympy.Expr:
    dict_monoms : Dict[Any,Any]
    dict_monoms = polynom.expand().as_coefficients_dict()
    combination = 0
    for key, value in dict_monoms.items():
        combination += value * variable_of_monomial[key]
    return combination


class Problem:
    def __init__(self, obj : sympy.Symbol) -> None:
        self.constraints : List[Constraint] = []
        self.objective = obj

    def add_constraint(self, constraint : Constraint) -> None:
        self.constraints.append(constraint)
    

    def solve(self, relaxation_order: int = 1) -> float:
        # 0. Separate constraint types 
        rules = Rule.of_constraints([
            constraint 
            for constraint in self.constraints 
            if constraint.substitution
        ])

        normal_constraints = [
            constraint 
            for constraint in self.constraints 
            if not constraint.substitution
        ]

        # 1. Build algebraic formulation
        algebra = momentmatrix.AlgebraSDP(self.objective, relaxation_order, rules)
        algebra.add_constraints(normal_constraints)

        # 2. Translate to SDP
        problemSDP = algebra_to_SDP(algebra)

        # 3. 

        return Solver.solve_cvxpy(problemSDP)


    def solve0(self, relaxation_order: int = 1) -> float:
        """Return the solution of the problem"""

        # 1. Generates all monomials
        # Assumes that no extra symbols in the objectives, for now

        all_symbols = self.objective.free_symbols

        all_monomials = generate_monomials_commutative(
            all_symbols, relaxation_order
        )

        # 2. Substitute the equality constraints
        #        - rules.py ?
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
                        - (sympy.total_degree(self.constraints[i].polynom) / 2)
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
                        - (sympy.total_degree(self.constraints[i].polynom) / 2)
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
