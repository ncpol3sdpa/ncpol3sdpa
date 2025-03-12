import sympy as sp
from sympy.ntheory import generate

from ncpol3sdpa import momentmatrix
from ncpol3sdpa.constraints import Constraint
from ncpol3sdpa.equality_constraints import solve_equality_constraints
from ncpol3sdpa.momentmatrix import MomentMatrix
from ncpol3sdpa.monomial import Monomial, generate_monomials_commutative
from ncpol3sdpa.solver import Solver



def polynom_linearized(variable_of_monomial, polynom):
    dict_monoms = polynom.as_coefficients_dict()
    combination = 0 
    for key,value in dict_monoms.items():
        combination += value * variable_of_monomial[key]
    return combination

class Problem:
    def __init__(self, obj):
        self.constraints = []
        self.objective = obj

    def add_constraint(self, constraint): ...

    def solve(self, relaxation_order: int = 1):
        """Return the solution of the problem"""

        # 1. Generates all monomials
        # Assumes that no extra symbols in the objectives, for now
        all_monomials = generate_monomials_commutative(
            self.objective.free_symbols, relaxation_order
        )

        # 2. Substitute the equality constraints
        #        - equality_constraints.py ?
        # skip for now, we create constraint matrix = 0 for now

        # 3. Build the moment matrix
        #        - momentmatrix.py
        moment_matrix, variable_of_monomial = momentmatrix.create_moment_matrix(
            all_monomials
        )

        # 4. Build constraints matrices
        #        - momentmatrix.py
        constraint_maricies_equal = [
            momentmatrix.create_matrix_constraints(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(
                        relaxation_order
                        - (sp.total_degree(self.constraints[i].polynom) / 2)
                    ),
                ),
                self.constraints[i].polynom,
            )
            for i in range(len(self.constraints))
            if self.constraints[i].equal_constraint
        ]

        constraint_maricies_positiv = [
            momentmatrix.create_matrix_constraints(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(
                        relaxation_order
                        - (sp.total_degree(self.constraints[i].polynom) / 2)
                    ),
                ),
                self.constraints[i].polynom,
            )
            for i in range(len(self.constraints))
            if (not self.constraints[i].equal_constraint)
        ]

        poly_obj = polynom_linearized(variable_of_monomial, self.objective)


        # 5. Solve the SDP (Solver.solve)
        #        - solver.py
        # CF ex3_cvxpy.py
        print(moment_matrix)
        return Solver.solve(poly_obj, len(moment_matrix), moment_matrix, constraint_maricies_positiv, constraint_maricies_equal)

