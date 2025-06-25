from ncpol3sdpa.sdp_repr import ProblemSDP


class Solver:
    """Base class for all SDP solvers.

    This abstract class defines the interface that all solver implementations
    must follow. Specific solver implementations should inherit from this class
    and provide concrete implementations of the solve method.

    Notes
    -----
    Each solver may have different capabilities, performance characteristics,
    and dependencies. Refer to specific solver documentation for details.
    """

    @classmethod
    def solve(cls, problem: ProblemSDP, verbose: bool = False) -> float:
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
        raise NotImplementedError("This method should be implemented in a subclass")
