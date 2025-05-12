from ncpol3sdpa.sdp_repr import ProblemSDP


class Solver:
    @classmethod
    def solve(self, problem: ProblemSDP) -> float:
        """Solve the SDP problem"""

        raise NotImplementedError("This method should be implemented in a subclass")
