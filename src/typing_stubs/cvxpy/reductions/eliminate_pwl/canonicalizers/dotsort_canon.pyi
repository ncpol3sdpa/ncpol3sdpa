from cvxpy import Constant as Constant
from cvxpy.atoms.affine.binary_operators import outer as outer
from cvxpy.atoms.affine.sum import sum as sum
from cvxpy.atoms.affine.vec import vec as vec
from cvxpy.expressions.variable import Variable as Variable

def dotsort_canon(expr, args): ...
