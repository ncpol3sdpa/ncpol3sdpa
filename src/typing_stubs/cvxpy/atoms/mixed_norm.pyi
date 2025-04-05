from cvxpy.atoms.norm import norm as norm
from cvxpy.expressions.expression import Expression as Expression

def mixed_norm(X, p: int | str = 2, q: int | str = 1): ...
