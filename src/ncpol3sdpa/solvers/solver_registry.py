from enum import Enum, auto
from typing import Dict, Type
import numpy

from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver
from .cvxpy_solver import CvxpySolver
from .mosek_solver import MosekSolver


class AvailableSolvers(Enum):
    """Enumeration of available SDP solvers."""

    CVXPY = auto()
    MOSEK = auto()


class SolverRegistry:
    """Registry for managing available solvers."""

    _solvers: Dict[AvailableSolvers, Type[Solver]] = {}

    @classmethod
    def register(
        cls, solver_type: AvailableSolvers, solver_class: Type[Solver]
    ) -> None:
        """Register a solver implementation for a specific solver type."""

        cls._solvers[solver_type] = solver_class

    @classmethod
    def get_solver(cls, solver_type: AvailableSolvers) -> Solver:
        """Get a solver instance for the specified solver type."""

        if solver_type not in cls._solvers:
            raise ValueError(f"No solver registered for {solver_type}")
        return cls._solvers[solver_type]()

    @classmethod
    def solve(
        cls, problem: ProblemSDP, solver_type: AvailableSolvers
    ) -> Solution_SDP[numpy.float64] | None:
        """Solve the problem using the specified solver type."""

        solver = cls.get_solver(solver_type)
        return solver.solve(problem)


# Register available solvers
SolverRegistry.register(AvailableSolvers.CVXPY, CvxpySolver)
SolverRegistry.register(AvailableSolvers.MOSEK, MosekSolver)
