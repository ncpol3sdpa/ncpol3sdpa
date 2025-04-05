from _typeshed import Incomplete
from cvxpy.atoms.affine.vec import vec as vec
from cvxpy.atoms.norm1 import norm1 as norm1
from cvxpy.atoms.norm_inf import norm_inf as norm_inf
from cvxpy.atoms.norm_nuc import normNuc as normNuc
from cvxpy.atoms.pnorm import pnorm as pnorm
from cvxpy.atoms.sigma_max import sigma_max as sigma_max
from cvxpy.expressions.expression import Expression as Expression

def norm(x, p: int | str = 2, axis: Incomplete | None = None, keepdims: bool = False): ...
def norm2(x, axis: Incomplete | None = None): ...
