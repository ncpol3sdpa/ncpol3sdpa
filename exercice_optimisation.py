import picos as pc
import numpy as np


n = 6


P = pc.Problem()
Y = pc.SymmetricVariable("Y", (n, n)) 

P.maximize = 2*Y[1,2]

M1 = pc.RealVariable("M1", (3, 3))
m1 = [
    [Y[0,3]-Y[0,1], Y[1,3]-Y[0,3], Y[1,4]-Y[0,4]],
    [Y[1,3]-Y[0,3], Y[3,3]-Y[1,3], Y[3,4]-Y[1,4]],
    [Y[1,4]-Y[0,4], Y[3,4]-Y[1,5], Y[3,5]-Y[1,5]]
]

for i in range(3):
	for j in range(3):
		P.add_constraint(M1[i,j] == m1[i][j])


M2 = pc.RealVariable("M2", (3, 3))
m2 = [
    [-Y[0,5]+Y[0,2]+0.25*Y[0,0], -Y[1,5]+Y[0,4]+0.25*Y[0,1], -Y[2,5]+Y[0,5]+0.25*Y[0,2]],
    [-Y[1,5]+Y[0,4]+0.25*Y[0,1], -Y[3,5]+Y[1,4]+0.25*Y[0,3], -Y[4,5]+Y[1,5]+0.25*Y[0,4]],
    [-Y[1,5]+Y[0,4]+0.25*Y[0,1], -Y[3,5]+Y[1,4]+0.25*Y[0,3], -Y[5,5]+Y[2,5]+0.25*Y[0,5]],
]

for i in range(3):
	for j in range(3):
		P.add_constraint(M2[i,j] == m2[i][j])

P += M1 == 0, M2 >> 0, Y >> 0, Y <= 1000

P.maximize = 2*Y[1,2] 

P.solve(solver="cvxopt")
print(Y)


P += Y >= 0, M1 == 0, M2 >= 0 

