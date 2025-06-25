from enum import Enum, auto
from typing import Dict, Type

from ncpol3sdpa.sdp_repr import ProblemSDP
from .solver import Solver
from .cvxpy_solver import CvxpySolver
from .mosek_solver import MosekSolver


class AvailableSolvers(Enum):
    """Enumeration of available SDP solvers.

    This enum provides a consistent interface for selecting different SDP solver
    implementations that can be used to solve optimization problems.
    """

    CVXPY = auto()
    """CVXPY: A Python library for convex optimization."""
    MOSEK = auto()
    """MOSEK: A commercial optimization solver for large-scale problems."""


class SolverRegistry:
    """Registry for managing available SDP solvers.

    This class implements a registry pattern to manage, retrieve, and use
    different SDP solver implementations. It allows for easy registration of new
    solvers and provides a consistent interface for solving optimization problems.
    """

    _solvers: Dict[AvailableSolvers, Type[Solver]] = {}

    @classmethod
    def register(
        cls, solver_type: AvailableSolvers, solver_class: Type[Solver]
    ) -> None:
        """Register a solver implementation for a specific solver type.

        Parameters
        ----------
        solver_type : AvailableSolvers
            The enum value representing the solver type.
        solver_class : Type[Solver]
            The solver class implementing the Solver interface.

        Notes
        -----
        This method is typically called during initialization to register all available
        solver implementations.
        """

        cls._solvers[solver_type] = solver_class

    @classmethod
    def get_solver(cls, solver_type: AvailableSolvers) -> Solver:
        """Get a solver instance for the specified solver type.

        Parameters
        ----------
        solver_type : AvailableSolvers
            The enum value representing the desired solver.

        Returns
        -------
        Solver
            An instance of the requested solver.

        Raises
        ------
        ValueError
            If no solver is registered for the specified type.
        """

        if solver_type not in cls._solvers:
            raise ValueError(f"No solver registered for {solver_type}")
        return cls._solvers[solver_type]()

    @classmethod
    def solve(cls, problem: ProblemSDP, solver_type: AvailableSolvers) -> float:
        """Solve the problem using the specified solver type.

        This is a convenience method that handles both retrieving the appropriate
        solver and executing the solve operation.

        Parameters
        ----------
        problem : ProblemSDP
            The semidefinite programming problem to solve.
        solver_type : AvailableSolvers
            The enum value representing the solver to use.

        Returns
        -------
        float
            The optimal value of the objective function.

        Raises
        ------
        ValueError
            If no solver is registered for the specified type.
        """

        solver = cls.get_solver(solver_type)
        return solver.solve(problem)


# Register available solvers
SolverRegistry.register(AvailableSolvers.CVXPY, CvxpySolver)
SolverRegistry.register(AvailableSolvers.MOSEK, MosekSolver)
