from monomial import Monomial
from monomial import generate_monomials_commutative
from equality_constraints import solve_equality_constraints
from momentmatrix import MomentMatrix
import momentmatrix
from solver import Solver
from constraints import Constraint

class Problem:

    def __init__(self,obj):

        self.constraints = []
        self.objective = obj

    def add_constraint(self, constraint): ...
    
    def solve(self, relaxation_order: int = 1):
        """Return the solution of the problem""" 
        
        # 1. Generates all monomials
        # Assumes that no extra symbols in the objectives, for now
        all_monomials = generate_monomials_commutative(self.objective.free_symbols, relaxation_order)

        # 2. Substitute the equality constraints
        #        - equality_constraints.py ?
        # skip for now, we create constraint matrix = 0 for now

        # 3. Build the moment matrix
        #        - momentmatrix.py
        moment_matrix = momentmatrix.create_matrix(all_monomials)

        # 4. Build constraints matrices
        #        - momentmatrix.py
        constraint_maricies = [momentmatrix.create_matrix_of_constraints(all_monomials, self.constraints[i].polynom, 0) \
                                 for i in range(len(self.constraints))]

        # 5. Solve the SDP (Solver.solve)
        #        - solver.py
        # CF ex3_cvxpy.py
