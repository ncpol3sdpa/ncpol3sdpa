from typing import List, Dict
from sympy import Expr, Symbol
from cvxpy import Variable, Maximize, Problem
from cvxpy.atoms.affine.vstack import vstack
from cvxpy.atoms.affine.hstack import hstack
from ncpol3sdpa.funs import coefficients_dict

class Solver:

    @classmethod
    def solve_cvxpy(cls, 
            polynome_obj : Expr,
            k : int,
            moment_matrix : List[List[Symbol]],
            list_matrix_positive : List[List[List[Expr]]],
            list_matrix_zero : List[List[List[Expr]]]
        ) -> float:
        """Solve the SDP problem with cvxpy"""

        moment_matrix_cvxpy = [[0 for _ in range(k)] for _ in range(k)]
        
        sympy_to_cvxpy : Dict[Expr, Variable] = {}
        for i in range(k):
            for j in range(k):
                if moment_matrix[i][j] not in sympy_to_cvxpy.keys():                
                    temp = Variable(name=moment_matrix[i][j].name)
                    sympy_to_cvxpy[moment_matrix[i][j]] = temp
                
                moment_matrix_cvxpy[i][j] = sympy_to_cvxpy[moment_matrix[i][j]]
        
        moment_matrix_cvxpy2 = vstack([hstack(row) for row in moment_matrix_cvxpy])

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
                    d = coefficients_dict(matrix_constraint[i][j])
                    for key,value in d.items():
                        matrix_constraint_cvxpy[i][j] += value * sympy_to_cvxpy[key] 
            
            matrix_constraint_cvxpy2 = vstack([hstack(row) for row in matrix_constraint_cvxpy])
            constraints.append(matrix_constraint_cvxpy2 == matrix_constraint_cvxpy2.T)
            constraints.append(matrix_constraint_cvxpy2>>0)

        for matrix_constraint in list_matrix_zero :
            ki = len(matrix_constraint)
            for i in range(len(matrix_constraint)):
                for j in range (len(matrix_constraint)):
                    d = coefficients_dict(matrix_constraint[i][j])
                    combination = 0
                    for key,value in d.items():
                        combination += value * sympy_to_cvxpy[key] 
                    constraints.append(combination == 0)

        print(f"{sympy_to_cvxpy = }")                                                       
        d = coefficients_dict(polynome_obj)
        combination = 0
        for key,value in d.items():
            combination += value * sympy_to_cvxpy[key] 

        obj = Maximize(combination)
        prob = Problem(obj, constraints)
        prob.solve(solver="CLARABEL",verbose=False) # type: ignore
        # prob.solve(solver="SCS",verbose=True) # type: ignore
        # solver mosics ?

        return float(prob.value)