from cvxpy.atoms.affine.diag import diag as diag
from cvxpy.atoms.affine.vec import vec as vec
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.problems.objective import Maximize as Maximize, Minimize as Minimize
from cvxpy.utilities.perspective_utils import form_cone_constraint as form_cone_constraint

def perspective_canon(expr, args): ...
