from cvxpy.atoms.affine.binary_operators import matmul as matmul
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dgp2dcp.canonicalizers.mul_canon import mul_canon as mul_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.mulexpression_canon import mulexpression_canon as mulexpression_canon

def pf_eigenvalue_canon(expr, args): ...
