from typing import List, Dict, Any
# from numbers import Number
import cvxpy
import sympy
from sympy import Symbol
import ncpol3sdpa.semidefinite_program_repr as sdp_repr

def cvxpy_dot_prod(c : Any, x : Any) -> Any:
    return cvxpy.trace(c @ x)
    # return cvxpy.sum(cvxpy.multiply(c, x))

class Solver:

    @classmethod
    def solve_cvxpy(self, problem : sdp_repr.ProblemSDP) -> Any:
        """Solve the SDP problem with cvxpy"""
        # Variables
        sdp_vars = [cvxpy.Variable((size, size), PSD=True) \
                          for size in problem.variable_sizes]

        # Moment matrix structure
        G = sdp_vars[problem.MOMENT_MATRIX_VAR_NUM]
        constraints = [G[0,0] == 1]
        for eq_class in problem.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            (i,j) = eq_class.pop() 
            for (x,y) in eq_class:
                constraints.append(G[i,j] == G[x,y])

        # Constraints
        for constraint in problem.constraints:
            expression = 0
            for var_num, matrix in constraint.constraints:
                expression += cvxpy_dot_prod(matrix, sdp_vars[var_num])
            constraints.append(0 == expression)

        print("SOLVER constraints:")
        print(constraints)
        
        # tr(A.T x G)
        objective = cvxpy.Maximize(cvxpy_dot_prod(problem.objective, G))
        

        prob = cvxpy.Problem(objective, constraints)
        prob.solve()  # Returns the optimal value.
        print("status:", prob.status)
        print("optimal value", prob.value)
        print("optimal var", G.value)
        return prob.value
 
    @classmethod
    def solve(cls, 
            polynome_obj : sympy.Poly,
            k : int,
            moment_matrix : List[List[Symbol]],
            list_matrix_positive : List[List[List[Symbol]]],
            list_matrix_zero : List[List[List[Symbol]]]
        ) -> float:
        """Solve the SDP problem with cvxpy"""

        moment_matrix_cvxpy = [[0 for _ in range(k)] for _ in range(k)]
        
        sympy_to_cvxpy : Dict[sympy.Poly, sympy.Poly] = {}
        for i in range(k):
            for j in range(k):
                if moment_matrix[i][j] not in sympy_to_cvxpy.keys():                
                    temp = cvxpy.Variable(name=moment_matrix[i][j].name)
                    sympy_to_cvxpy[moment_matrix[i][j]] = temp
                
                moment_matrix_cvxpy[i][j] = sympy_to_cvxpy[moment_matrix[i][j]]
        
        moment_matrix_cvxpy2 = cvxpy.vstack([cvxpy.hstack(row) for row in moment_matrix_cvxpy])

        constraints = [
            moment_matrix_cvxpy2 == moment_matrix_cvxpy2.T,
            moment_matrix_cvxpy2>>0,
            moment_matrix_cvxpy2[0,0]== 1
        ]

        for matrix_constraint in list_matrix_positive :
            ki = len(matrix_constraint)
            matrix_constraint_cvxpy = [[0 for _ in range(ki)] for _ in range(ki)]
            for i in range(len(matrix_constraint)):
                for j in range(len(matrix_constraint)):
                    d = matrix_constraint[i][j].as_coefficients_dict()
                    for key,value in d.items():
                        matrix_constraint_cvxpy[i][j] += value * sympy_to_cvxpy[key] 
            
            matrix_constraint_cvxpy2 = cvxpy.vstack([cvxpy.hstack(row) for row in matrix_constraint_cvxpy])
            constraints.append(matrix_constraint_cvxpy2 == matrix_constraint_cvxpy2.T)
            constraints.append(matrix_constraint_cvxpy2>>0)

        for matrix_constraint in list_matrix_zero :
            ki = len(matrix_constraint)
            for i in range(len(matrix_constraint)):
                for j in range (len(matrix_constraint)):
                    d = matrix_constraint[i][j].as_coefficients_dict()
                    combination = 0
                    for key,value in d.items():
                        combination += value * sympy_to_cvxpy[key] 
                    constraints.append(combination == 0)

                                                                                    
        d = polynome_obj.as_coefficients_dict()
        combination = 0
        for key,value in d.items():
            combination += value * sympy_to_cvxpy[key] 

        obj = cvxpy.Maximize(combination)
        prob = cvxpy.Problem(obj, constraints)
        prob.solve()

        return prob.value
        # return 0