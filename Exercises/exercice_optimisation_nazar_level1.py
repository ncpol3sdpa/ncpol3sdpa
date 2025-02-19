import picos as pc
import numpy as np

#   max   2*x0*x1
# x1,x2∈R 
# s.t x0² − x0 = 0
#   & − x1² + x1 + 1/4 ≥ 0

# Relaxation SDP


P = pc.Problem()
y = pc.SymmetricVariable("y", (3,3))

P.maximize = 2*y[1,2]

P += y >> 0, y[1,1] -y[1,0] == 0, -y[2,2] + y[2,0] + 0.25*y[0,0] >= 0, y[0,0] == 1
P.solve(solver="cvxopt")

print(2*y[1,2])

