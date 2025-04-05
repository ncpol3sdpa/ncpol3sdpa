from _typeshed import Incomplete
from cvxpy.constraints import NonNeg as NonNeg, Zero as Zero
from cvxpy.reductions.solution import Solution as Solution, failure_solution as failure_solution
from cvxpy.reductions.solvers import utilities as utilities
from cvxpy.reductions.solvers.conic_solvers.conic_solver import ConicSolver as ConicSolver
from cvxpy.utilities.versioning import Version as Version

class SCIPY(ConicSolver):
    SUPPORTED_CONSTRAINTS: Incomplete
    MIP_CAPABLE: bool
    MI_SUPPORTED_CONSTRAINTS = SUPPORTED_CONSTRAINTS
    STATUS_MAP: Incomplete
    def import_solver(self) -> None: ...
    def name(self): ...
    def apply(self, problem): ...
    def solve_via_data(self, data, warm_start: bool, verbose: bool, solver_opts, solver_cache: Incomplete | None = None): ...
    def invert(self, solution, inverse_data): ...
