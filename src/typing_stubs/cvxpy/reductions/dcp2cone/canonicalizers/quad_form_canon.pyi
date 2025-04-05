from cvxpy.atoms import sum_squares as sum_squares
from cvxpy.atoms.quad_form import decomp_quad as decomp_quad
from cvxpy.expressions.constants import Constant as Constant
from cvxpy.reductions.dcp2cone.canonicalizers.quad_over_lin_canon import quad_over_lin_canon as quad_over_lin_canon

def quad_form_canon(expr, args): ...
