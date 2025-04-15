from _typeshed import Incomplete
from cvxpy import problems as problems
from cvxpy.atoms.elementwise.maximum import maximum as maximum
from cvxpy.atoms.elementwise.minimum import minimum as minimum
from cvxpy.constraints import Inequality as Inequality
from cvxpy.expressions.constants.parameter import Parameter as Parameter
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.problems.objective import Minimize as Minimize
from cvxpy.reductions.canonicalization import Canonicalization as Canonicalization
from cvxpy.reductions.dcp2cone.canonicalizers import CANON_METHODS as CANON_METHODS
from cvxpy.reductions.dqcp2dcp import inverse as inverse, sets as sets, tighten as tighten
from cvxpy.reductions.inverse_data import InverseData as InverseData
from cvxpy.reductions.solution import Solution as Solution
from typing import NamedTuple

class BisectionData(NamedTuple):
    feas_problem: Incomplete
    param: Incomplete
    tighten_lower: Incomplete
    tighten_upper: Incomplete

class Dqcp2Dcp(Canonicalization):
    def __init__(self, problem: Incomplete | None = None) -> None: ...
    def accepts(self, problem): ...
    def invert(self, solution, inverse_data): ...
    def apply(self, problem): ...
