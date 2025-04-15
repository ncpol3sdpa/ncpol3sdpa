import cvxpy as cp

Y = cp.Variable((6, 6))


M1 = cp.vstack([
    cp.hstack([Y[0, 3] - Y[0, 1], Y[1, 3] - Y[0, 3], Y[1, 4] - Y[0, 4]]),
    cp.hstack([Y[1, 3] - Y[0, 3], Y[2, 3] - Y[1, 3], Y[2, 4] - Y[1, 4]]),
    cp.hstack([Y[1, 4] - Y[0, 4], Y[2, 4] - Y[1, 4], Y[2, 5] - Y[1, 5]])
])

M2 = cp.vstack([
    cp.hstack([-Y[0, 5] + Y[0, 2] + 0.25 * Y[0, 0], -Y[1, 5] + Y[0, 4] + 0.25 * Y[0, 1], -Y[2, 5] + Y[0, 5] + 0.25 * Y[0, 2]]),
    cp.hstack([-Y[1, 5] + Y[0, 4] + 0.25 * Y[0, 1], -Y[2, 5] + Y[1, 4] + 0.25 * Y[0, 3], -Y[3, 5] + Y[1, 5] + 0.25 * Y[0, 4]]),
    cp.hstack([-Y[1, 5] + Y[0, 4] + 0.25 * Y[0, 1], -Y[2, 5] + Y[1, 4] + 0.25 * Y[0, 3], -Y[4, 5] + Y[2, 5] + 0.25 * Y[0, 5]])
])

constraints = [Y >> 0, M1 == 0, M2 >> 0]

obj = cp.Maximize(2*Y[0,4])

prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", Y.value)
