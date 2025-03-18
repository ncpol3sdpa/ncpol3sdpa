from ncpol3sdpa.solver import Solver
from sympy import symbols, Symbol # type: ignore
# from typing import List

def test_1() -> None:
    # : Poly = poly() 
    y1: Symbol = (symbols("y1"))
    y2: Symbol = (symbols("y2"))
    y3: Symbol = (symbols("y3"))
    y4: Symbol = (symbols("y4"))
    y5: Symbol = (symbols("y5"))
    y6: Symbol = (symbols("y6"))
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

    solution : float = Solver.solve_cvxpy(
        p_obj,3, moment_matrix, constraint_positiv, constraint_zero
    )
    assert(abs(solution - 2.414) <= 0.1)


if __name__ == "__main__":
    test_1()