from ncpol3sdpa.momentmatrix import MomentMatrix
import cvxpy


class Solver:
    @classmethod
    def solve(k : int, moment_matrix : MomentMatrix, list_matrix_positive : list,list_matrix_zero :list):   
        Y = cvxpy.Variable(k,k)
        constraints = [Y == Y.T, Y>>0]
        
        dict = {}
        for i in range(k):
            for j in range(k):
                if moment_matrix[i][j] not in dict.keys():
                    temp = cvxpy.Variable(moment_matrix[i][j].name)
                    dict[moment_matrix[i][j]] = temp

                Y[i, j] = dict[moment_matrix[i][j]]

        for matrix_constraint in list_matrix_positive:
            Z = cvxpy.Variable(len(matrix_constraint), len(matrix_constraint))
            constraints.append(Z == Z.T, Z >> 0)
            for i in range(len(matrix_constraint)):
                for j in range(len(matrix_constraint)):
                    d = matrix_constraint[i][j].as_coefficients_dict()
                    for key, value in d.items():
                        Z[i, j] += value * dict[key]


Solver.solve()

m = MomentMatrix()
n = MomentMatrix()

m * n

print(m)
