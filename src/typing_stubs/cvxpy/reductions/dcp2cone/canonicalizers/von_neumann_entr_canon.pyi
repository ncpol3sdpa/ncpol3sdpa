from cvxpy import Variable as Variable, lambda_sum_largest as lambda_sum_largest, trace as trace
from cvxpy.atoms.affine.sum import sum as sum
from cvxpy.constraints.nonpos import NonNeg as NonNeg
from cvxpy.constraints.zero import Zero as Zero
from cvxpy.reductions.dcp2cone.canonicalizers.entr_canon import entr_canon as entr_canon
from cvxpy.reductions.dcp2cone.canonicalizers.lambda_sum_largest_canon import lambda_sum_largest_canon as lambda_sum_largest_canon

def von_neumann_entr_canon(expr, args): ...
