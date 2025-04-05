import numpy as np
from _typeshed import Incomplete
from cvxpy import Zero as Zero
from cvxpy.constraints import ExpCone as ExpCone, NonNeg as NonNeg, SOC as SOC
from cvxpy.reductions.dcp2cone.cone_matrix_stuffing import ParamConeProg as ParamConeProg
from cvxpy.reductions.solution import Solution as Solution, failure_solution as failure_solution
from cvxpy.reductions.solvers import utilities as utilities
from cvxpy.reductions.solvers.conic_solvers.conic_solver import ConicSolver as ConicSolver, dims_to_solver_dict as dims_to_solver_dict
from pyscipopt.scip import Model as ScipModel
from scipy.sparse import dok_matrix
from typing import Any, Generic, Iterator

log: Incomplete
ScipModel = Generic
STATUS_MAP: Incomplete

class ConstraintTypes:
    EQUAL: str
    LESS_THAN_OR_EQUAL: str

class VariableTypes:
    BINARY: str
    INTEGER: str
    CONTINUOUS: str

class SCIP(ConicSolver):
    MIP_CAPABLE: bool
    SUPPORTED_CONSTRAINTS: Incomplete
    MI_SUPPORTED_CONSTRAINTS = SUPPORTED_CONSTRAINTS
    def name(self) -> str: ...
    def import_solver(self) -> None: ...
    def apply(self, problem: ParamConeProg) -> tuple[dict, dict]: ...
    def invert(self, solution: dict[str, Any], inverse_data: dict[str, Any]) -> Solution: ...
    def solve_via_data(self, data: dict[str, Any], warm_start: bool, verbose: bool, solver_opts: dict[str, Any], solver_cache: dict = None) -> Solution: ...
    def add_model_lin_constr(self, model: ScipModel, variables: list, rows: Iterator, ctype: str, A: dok_matrix, b: np.ndarray) -> list: ...
    def add_model_soc_constr(self, model: ScipModel, variables: list, rows: Iterator, A: dok_matrix, b: np.ndarray) -> tuple: ...

def get_variable_type(n: int, data: dict[str, Any]) -> str: ...
