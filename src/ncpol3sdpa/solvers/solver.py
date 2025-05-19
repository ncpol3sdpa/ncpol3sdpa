from typing import Optional
from ncpol3sdpa.sdp_repr import ProblemSDP
from ncpol3sdpa.sdp_solution import Solution_SDP


class Solver:
    """Base class for all SDP solvers.

    All solver implementations should inherit from this class and implement
    the solve method.
    """

    @classmethod
    def solve(self, problem: ProblemSDP) -> Optional[Solution_SDP]:
        """Solve the SDP problem"""

        raise NotImplementedError("This method should be implemented in a subclass")
