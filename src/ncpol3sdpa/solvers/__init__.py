from enum import Enum, auto

from ncpol3sdpa.sdp_repr import ProblemSDP
from .cvxpy_solver import CvxpySolver
from .mosek_solver import MosekSolver


class AvailableSolvers(Enum):
    CVXPY = auto()
    MOSEK = auto()

    def solve(self, problem: ProblemSDP) -> float:
        """Solve the SDP problem"""

        match self:
            case AvailableSolvers.CVXPY:
                return CvxpySolver().solve(problem)
            case AvailableSolvers.MOSEK:
                return MosekSolver().solve(problem)


__all__ = ["AvailableSolvers"]
