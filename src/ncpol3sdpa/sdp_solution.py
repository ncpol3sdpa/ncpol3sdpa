import numpy as np

from numpy.typing import NDArray
from typing import List, NamedTuple, TypeVar, Generic, Type

T = TypeVar("T", bound=np.generic)


# Data structure representing a solution of the sdp
class Solution_SDP(NamedTuple, Generic[T]):
    # equations found in the article "Semidefinite programming relaxations for quantum correlations"
    """Solution to a given SDP problem, returned by solvers"""

    """optimal value of the objective function
    In the documentation, corresponds to ($\\lang C \\vert bar X^0$ \\rang)"""
    primal_objective_value: float

    """value of the primal PSD variables at the optimal point. They are the variables called G^k, G^k_{g_i} in eq (30)
    In the documentation, corresponds to ($\\bar X^i$)"""
    primal_PSD_variables: List[NDArray[T]]

    """value of lambda or the objective function of the dual in the dual formulation of the SDP. See (36)
    In the documentation, corresponds to ($\\lambda$)"""
    dual_objective_value: float

    """value of the dual PSD variables associated with the PSD constraints on the primal variables.
    In the documentation, corresponds to ($\\bar Y^i$)"""
    dual_PSD_variables: List[NDArray[T]]

    """value of the dual variables associated with the equality constraints between polynomials.
    In the documentation, corresponds to ($\\nu_i$)  """
    dual_eqC_variables: NDArray[np.float64]

    """value of the dual variables associated with the local inequality constraints.
    In the documentation, corresponds to ($\\eta_i) """
    dual_ineqC_variables: NDArray[np.float64]

    """Data type (real or complex)"""
    dtype: Type[T]

    # Note: The order in which the variables appear in, in each list should be the same as their order in
    # the Problem_SDP class. For example, the main moment matrix should be in self.primal_variables[0]
