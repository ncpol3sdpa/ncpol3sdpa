from cvxpy.atoms.affine.binary_operators import matmul as matmul
from cvxpy.atoms.affine.diag import diag as diag
from cvxpy.atoms.one_minus_pos import one_minus_pos as one_minus_pos
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dgp2dcp.canonicalizers.mulexpression_canon import mulexpression_canon as mulexpression_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.one_minus_pos_canon import one_minus_pos_canon as one_minus_pos_canon

def eye_minus_inv_canon(expr, args): ...
