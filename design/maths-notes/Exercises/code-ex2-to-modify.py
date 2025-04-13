#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:25:23 2025

@author: thms
"""

from picos import Problem, RealVariable, SymmetricVariable


# x = RealVariable("x")
# y = RealVariable("y")

# P = Problem()
# P.set_objective("max",2*x*y)

# c1= P.add_constraint(x**2-x==0)
# c2= P.add_constraint(-y**2+y-1/4>=0)

# print(P)

# P.options.solver = "cvxopt"
# solution = P.solve()
# print (solution)


P = Problem()

M = SymmetricVariable("M",(3,3))

# P+= M[2,2]-M[0,2] == 0
# P+=-M[1,1]-M[0,1] +1/4 >= 0
# P+= M>>0

P.add_constraint(M[2,2]-M[0,2] == 0)

P.add_constraint(-M[1,1]-M[0,1] +1/4 >= 0)
P.add_constraint(M>>0)

P.set_objective("max",2*M[1,2])

P.options.solver = "cvxopt"
solution = P.solve()

print (solution)
