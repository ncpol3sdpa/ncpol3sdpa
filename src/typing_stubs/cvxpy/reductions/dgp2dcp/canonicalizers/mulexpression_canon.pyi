from cvxpy.atoms.affine.bmat import bmat as bmat
from cvxpy.atoms.affine.hstack import hstack as hstack
from cvxpy.atoms.affine.reshape import reshape as reshape
from cvxpy.atoms.log_sum_exp import log_sum_exp as log_sum_exp
from cvxpy.utilities.shape import mul_shapes_promote as mul_shapes_promote

def mulexpression_canon(expr, args): ...
