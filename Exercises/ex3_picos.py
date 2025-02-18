import picos

P = picos.Problem()
Y = picos.HermitianVariable("Y", 3) # Xi^dag = Xi 
ro = picos.HermitianVariable("ro", 3)



P.maximize = Y[1,2] + Y[2,1]
P.add_constraint(Y[1,1] - Y[1,0] == 0)
P.add_constraint((Y[2,2] - Y[2,0] + 0.25).real >= 0)
P.add_constraint((Y[2,2] - Y[2,0]).imag == 0)
P.add_constraint(Y >> 0)

P.solve(solver="cvxopt")

print(P)

