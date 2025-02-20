

class Problem:

    def __init__(self,obj):

        self.constraints = []
        self.objective = obj

    def add_constraint(self, constraint): ...
    
    def solve(self, relaxation_order: int = 1):
        """Return the solution of the problem""" 
        
        # 1. Generates all monomials
        #        - monomial.py
        # 2. Substitute the equality constraints
        #        - equality_constraints.py ?
        # 3. Build the moment matrix
        #        - momentmatrix.py
        # 4. Build constraints matrices
        #        - momentmatrix.py
        # 5. Solve the SDP (Solver.solve)
        #        - solver.py
        # CF ex3_cvxpy.py