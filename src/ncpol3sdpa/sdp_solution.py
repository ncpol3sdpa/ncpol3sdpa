import numpy as np

from numpy.typing import NDArray
from typing import List, NamedTuple


# Data structure representing a solution of the sdp
class Solution_SDP(NamedTuple):
    # equations found in the article "Semidefinite programming relaxations for quantum correlations"
    """optimal value of the objective function"""

    primal_objective_value: float
    """value of the primal PSD variables at the optimal point. They are the variables called G^k, G^k_{g_i} in eq (30)"""
    primal_variables: List[NDArray[np.float64]]
    """value of lambda or the objective function of the dual in the dual formulation of the SDP. See (36)"""
    dual_objective_value: float
    """ value of the dual PSD variables associated with the PSD constraints on the primal variables. """
    dual_variables: List[NDArray[np.float64]]
    """"""

    # Note: The order in which the variables appear in, in each list should be the same as their order in
    # the Problem_SDP class. For example, the main moment matrix should be in self.primal_variables[0]
