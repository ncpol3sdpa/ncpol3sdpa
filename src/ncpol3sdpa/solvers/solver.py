from abc import ABC, abstractmethod
from typing import Any, Dict

from ncpol3sdpa.sdp_repr import ProblemSDP
from ncpol3sdpa.sdp_solution import Solution_SDP


class Solver(ABC):
    """Base class for all SDP solvers.

    This abstract class defines the interface that all solver implementations
    must follow. Specific solver implementations should inherit from this class
    and provide concrete implementations of the solve method.

    Notes
    -----
    Each solver may have different capabilities, performance characteristics,
    and dependencies. Refer to specific solver documentation for details.
    """

    @abstractmethod
    def solve(
        cls, problem: ProblemSDP, **config: Dict[str, Any]
    ) -> Solution_SDP[Any] | None:
        """Solve the semidefinite programming (SDP) problem.

        Parameters
        ----------
        problem : ProblemSDP
            The semidefinite programming problem to be solved.

        Returns
        -------
        float
            The optimal value of the objective function.
        """

        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def is_available(cls) -> bool:
        """Check if the solver is available for use.

        Returns
        -------
        bool
            True if the solver is available, False otherwise.
        """

        raise NotImplementedError("Subclasses must implement this method.")
