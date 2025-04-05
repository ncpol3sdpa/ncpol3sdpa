from cvxpy.atoms.affine.bmat import bmat as bmat
from cvxpy.atoms.affine.diag import diag_mat as diag_mat, diag_vec as diag_vec
from cvxpy.atoms.affine.sum import sum as sum
from cvxpy.atoms.affine.upper_tri import vec_to_upper_tri as vec_to_upper_tri
from cvxpy.atoms.elementwise.log import log as log
from cvxpy.constraints.psd import PSD as PSD
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dcp2cone.canonicalizers.log_canon import log_canon as log_canon

def log_det_canon(expr, args): ...
