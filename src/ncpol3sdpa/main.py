
from ncpol3sdpa.monomial import *
from ncpol3sdpa.momentmatrix import *
from ncpol3sdpa.constraints import *
from ncpol3sdpa.problem import *


def main():

    x = Variable("x")
    y = Variable("y")

    p = Problem(2*max(x*y))
    c1 = Constraints()
    c2 = Constraints()
    p.add_constraint(c1)
    p.add_constraint(c2)
    p.solve()

if __name__ == '__main__':
    main()