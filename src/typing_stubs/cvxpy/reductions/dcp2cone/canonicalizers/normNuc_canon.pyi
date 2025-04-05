from cvxpy.atoms.affine.bmat import bmat as bmat
from cvxpy.atoms.affine.trace import trace as trace
from cvxpy.constraints.constraint import Constraint as Constraint
from cvxpy.expressions.variable import Variable as Variable

def normNuc_canon(expr, args) -> tuple[float, list[Constraint]]: ...
