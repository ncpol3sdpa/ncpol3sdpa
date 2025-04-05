from cvxpy.atoms.affine.reshape import reshape as reshape
from cvxpy.expressions.expression import DEFAULT_ORDER_DEPRECATION_MSG as DEFAULT_ORDER_DEPRECATION_MSG, Expression as Expression
from typing import Literal

def vec(X, order: Literal['F', 'C', None] = None): ...
