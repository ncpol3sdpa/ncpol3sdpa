# from typing import List

# import sympy
import cvxpy


class Solver:

    @classmethod
    def solve(cls, polynome_obj, k : int, moment_matrix, list_matrix_positive : list,list_matrix_zero :list):   
        moment_matrix_cvxpy = [[0 for _ in range(k)] for _ in range(k)]
        
        sympy_to_cvxpy = {}
        for i in range(k):
            for j in range (k):
                if moment_matrix[i][j] not in sympy_to_cvxpy.keys():                
                    temp = cvxpy.Variable(name=moment_matrix[i][j].name)
                    sympy_to_cvxpy[moment_matrix[i][j]] = temp
                
                moment_matrix_cvxpy[i][j] = sympy_to_cvxpy[moment_matrix[i][j]]
        
        moment_matrix_cvxpy2 = cvxpy.vstack([cvxpy.hstack(row) for row in moment_matrix_cvxpy])

        constraints = [moment_matrix_cvxpy2 == moment_matrix_cvxpy2.T, \
                       moment_matrix_cvxpy2>>0, moment_matrix_cvxpy2[0,0]== 1]

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
