import cvxpy as cp

Y  = [cp.Variable(name=f"x{i}") for i in range(6)]

M = cp.vstack([
    cp.hstack([Y[0], Y[1], Y[2]]),
    cp.hstack([Y[1], Y[3], Y[4]]),
    cp.hstack([Y[2], Y[4], Y[5]])
])

constraints = [Y[3]-Y[1] == 0, -Y[5]+Y[2]+0.25*Y[0] >= 0, M >> 0, Y[0] == 1]

obj = cp.Maximize(2*Y[4])

prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
