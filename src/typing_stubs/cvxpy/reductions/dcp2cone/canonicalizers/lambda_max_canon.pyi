from cvxpy.atoms.affine.diag import diag_vec as diag_vec
from cvxpy.atoms.affine.promote import promote as promote
from cvxpy.atoms.affine.upper_tri import upper_tri as upper_tri
from cvxpy.constraints.psd import PSD as PSD
from cvxpy.expressions.variable import Variable as Variable

def lambda_max_canon(expr, args): ...
