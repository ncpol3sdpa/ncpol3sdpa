from ncpol3sdpa.sdp_repr import ProblemSDP


class Solver:
    """Base class for all SDP solvers.

    All solver implementations should inherit from this class and implement
    the solve method.
    """

    @classmethod
    def solve(self, problem: ProblemSDP) -> float:
        """Solve the SDP problem.

        Args:
            problem: The SDP problem to solve.

        Returns:
            The optimal value of the objective function.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("This method should be implemented in a subclass")
