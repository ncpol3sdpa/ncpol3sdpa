from _typeshed import Incomplete
from cvxpy import Zero as Zero
from cvxpy.constraints import NonNeg as NonNeg
from cvxpy.reductions.dcp2cone.cone_matrix_stuffing import ParamConeProg as ParamConeProg
from cvxpy.reductions.solution import Solution as Solution, failure_solution as failure_solution
from cvxpy.reductions.solvers import utilities as utilities
from cvxpy.reductions.solvers.conic_solvers.conic_solver import ConicSolver as ConicSolver
from cvxpy.utilities.versioning import Version as Version
from typing import Any

log: Incomplete

class PDLP(ConicSolver):
    SUPPORTED_CONSTRAINTS: Incomplete
    PDLP_MODEL: str
    def name(self) -> str: ...
    def import_solver(self) -> None: ...
    def apply(self, problem: ParamConeProg) -> tuple[dict, dict]: ...
    def invert(self, solution: dict[str, Any], inverse_data: dict[str, Any]) -> Solution: ...
    def solve_via_data(self, data: dict[str, Any], warm_start: bool, verbose: bool, solver_opts: dict[str, Any], solver_cache: dict = None) -> Solution: ...
