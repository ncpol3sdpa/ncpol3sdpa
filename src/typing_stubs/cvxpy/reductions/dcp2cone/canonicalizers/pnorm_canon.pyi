from cvxpy.atoms.affine.sum import sum as sum
from cvxpy.atoms.affine.vec import vec as vec
from cvxpy.atoms.elementwise.abs import abs as abs
from cvxpy.constraints.second_order import SOC as SOC
from cvxpy.expressions.constants import Constant as Constant
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.eliminate_pwl.canonicalizers.abs_canon import abs_canon as abs_canon
from cvxpy.utilities.power_tools import gm_constrs as gm_constrs

def pnorm_canon(expr, args): ...
