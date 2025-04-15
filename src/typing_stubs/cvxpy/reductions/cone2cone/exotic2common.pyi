from _typeshed import Incomplete
from cvxpy.atoms.affine.hstack import hstack as hstack
from cvxpy.atoms.affine.reshape import reshape as reshape
from cvxpy.constraints.power import PowCone3D as PowCone3D, PowConeND as PowConeND
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.canonicalization import Canonicalization as Canonicalization
from cvxpy.reductions.solution import Solution as Solution

EXOTIC_CONES: Incomplete

def pow_nd_canon(con, args): ...

class Exotic2Common(Canonicalization):
    CANON_METHODS: Incomplete
    def __init__(self, problem: Incomplete | None = None) -> None: ...
    def invert(self, solution, inverse_data): ...
