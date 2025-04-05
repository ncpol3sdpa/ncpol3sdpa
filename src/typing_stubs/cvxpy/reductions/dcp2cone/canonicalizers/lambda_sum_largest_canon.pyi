from cvxpy.atoms import trace as trace
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dcp2cone.canonicalizers.lambda_max_canon import lambda_max_canon as lambda_max_canon

def lambda_sum_largest_canon(expr, args): ...
