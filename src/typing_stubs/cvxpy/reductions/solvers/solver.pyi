import abc
from _typeshed import Incomplete
from cvxpy.reductions.reduction import Reduction as Reduction

class Solver(Reduction, metaclass=abc.ABCMeta):
    DIMS: str
    MIP_CAPABLE: bool
    BOUNDED_VARIABLES: bool
    VAR_ID: str
    DUAL_VAR_ID: str
    EQ_CONSTR: str
    NEQ_CONSTR: str
    @abc.abstractmethod
    def name(self): ...
    @abc.abstractmethod
    def import_solver(self): ...
    def is_installed(self) -> bool: ...
    @abc.abstractmethod
    def solve_via_data(self, data, warm_start: bool, verbose: bool, solver_opts, solver_cache: Incomplete | None = None): ...
    def solve(self, problem, warm_start: bool, verbose: bool, solver_opts): ...
