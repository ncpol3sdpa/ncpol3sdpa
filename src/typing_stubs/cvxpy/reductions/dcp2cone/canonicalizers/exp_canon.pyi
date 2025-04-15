from cvxpy.atoms import promote as promote
from cvxpy.constraints.exponential import ExpCone as ExpCone
from cvxpy.expressions.constants import Constant as Constant
from cvxpy.expressions.variable import Variable as Variable

def exp_canon(expr, args): ...
