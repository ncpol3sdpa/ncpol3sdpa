from _typeshed import Incomplete
from cvxpy import problems as problems
from cvxpy.expressions import cvxtypes as cvxtypes
from cvxpy.expressions.expression import Expression as Expression
from cvxpy.problems.objective import Minimize as Minimize
from cvxpy.reductions.canonicalization import Canonicalization as Canonicalization
from cvxpy.reductions.inverse_data import InverseData as InverseData

class Dcp2Cone(Canonicalization):
    cone_canon_methods: Incomplete
    quad_canon_methods: Incomplete
    quad_obj: Incomplete
    def __init__(self, problem: Incomplete | None = None, quad_obj: bool = False) -> None: ...
    def accepts(self, problem): ...
    def apply(self, problem): ...
    def canonicalize_tree(self, expr, affine_above: bool) -> tuple[Expression, list]: ...
    def canonicalize_expr(self, expr, args, affine_above: bool) -> tuple[Expression, list]: ...
