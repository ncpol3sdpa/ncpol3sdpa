from cvxpy.atoms import reshape as reshape, vstack as vstack
from cvxpy.constraints import SOC as SOC
from cvxpy.expressions.variable import Variable as Variable

def soc_canon(expr, real_args, imag_args, real2imag): ...
