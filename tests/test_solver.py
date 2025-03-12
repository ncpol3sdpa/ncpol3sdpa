from ncpol3sdpa.solver import *
from sympy import symbols 

def test_1():
    y1, y2, y3, y4, y5, y6 = symbols("y1 y2 y3 y4 y5 y6")
    p_obj = 2*y5 
    constraint2 = [[y4-y2]]
    constraint3 = [[-y6+y3+0.25*y1]]
    moment_matrix = [
        [y1, y2, y3], 
        [y2, y4, y5],
        [y3, y5, y6]
    ]
    constraint_zero = [constraint2]
    constraint_positiv = [constraint3]
    assert(abs(Solver.solve(p_obj, 3, moment_matrix, constraint_positiv, constraint_zero) - 2.414) <= 0.1)

