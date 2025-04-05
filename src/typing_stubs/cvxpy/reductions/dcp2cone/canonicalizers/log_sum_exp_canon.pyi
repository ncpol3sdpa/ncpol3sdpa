from cvxpy.atoms import exp as exp, promote as promote, reshape as reshape, sum as sum
from cvxpy.expressions.constants import Constant as Constant
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dcp2cone.canonicalizers.exp_canon import exp_canon as exp_canon

def log_sum_exp_canon(expr, args): ...
