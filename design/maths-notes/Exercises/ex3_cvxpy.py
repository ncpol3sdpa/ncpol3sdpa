import cvxpy as cp

Y = cp.Variable((3,3))

constraints = [Y >> 0, Y[1,1] - Y[0, 1] == 0, -Y[2,2] + Y[0,2] + 0.25*Y[0,0] >= 0, Y[0, 0] == 1, Y == Y.T]

obj = cp.Maximize(Y[1,2] - Y[2,1])

prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", Y.value)
