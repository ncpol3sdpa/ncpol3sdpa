from _typeshed import Incomplete
from cvxpy.constraints import ExpCone as ExpCone
from cvxpy.reductions.solution import Solution as Solution, failure_solution as failure_solution
from cvxpy.reductions.solvers import utilities as utilities
from cvxpy.reductions.solvers.conic_solvers.conic_solver import ConicSolver as ConicSolver
from cvxpy.reductions.solvers.conic_solvers.ecos_conif import ECOS as ECOS, dims_to_solver_dict as dims_to_solver_dict

class ECOS_BB(ECOS):
    MIP_CAPABLE: bool
    MI_SUPPORTED_CONSTRAINTS: Incomplete
    def name(self): ...
    def apply(self, problem): ...
    def invert(self, solution, inverse_data): ...
    def solve_via_data(self, data, warm_start: bool, verbose: bool, solver_opts, solver_cache: Incomplete | None = None): ...
