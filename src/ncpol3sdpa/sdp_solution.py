import numpy as np

from numpy.typing import NDArray
from typing import List


# Data structure representing a solution of the sdp
class Solution_SDP:
    # equations found in the article "Semidefinite programming relaxations for quantum correlations"
    def __init__(
        self,
        primal_objective_value: float,
        primal_variables: List[NDArray[np.float64]],
        dual_objective_value: float,
        dual_variables: List[NDArray[np.float64]],
    ) -> None:
        """optimal value of the objective function"""
        self.primal_objective_value: float = primal_objective_value
        """value of the primal PSD variables at the optimal point. They are the variables called G^k, G^k_{g_i} in eq (30)"""
        self.primal_variables: List[NDArray[np.float64]] = primal_variables
        """value of lambda or the objective function of the dual in the dual formulation of the SDP. See (36)"""
        self.dual_objective_value: float = dual_objective_value
        """ value of the dual PSD variables associated with the PSD constraints on the primal variables. """
        self.dual_variables: List[NDArray[np.float64]] = dual_variables

        # Note: The order in which the variables appear in, in each list should be the same as their order in
        # the Problem_SDP class. For example, the main moment matrix should be in self.primal_variables[0]
