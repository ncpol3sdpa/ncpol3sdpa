from _typeshed import Incomplete
from cvxpy import atoms as atoms
from cvxpy.atoms.affine.add_expr import AddExpression as AddExpression
from cvxpy.atoms.affine.binary_operators import DivExpression as DivExpression
from cvxpy.atoms.affine.sum import Sum as Sum
from cvxpy.atoms.affine.unary_operators import NegExpression as NegExpression

INVERTIBLE: Incomplete

def inverse(expr): ...
def invertible(expr): ...
