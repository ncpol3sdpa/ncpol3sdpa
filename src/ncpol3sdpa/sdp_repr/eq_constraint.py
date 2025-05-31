from typing import Tuple, List, NamedTuple

import numpy as np
from numpy.typing import NDArray


class EqConstraint(NamedTuple):
    """Represents a list of constraints

    A tuple (k, A) represents the constraint :
    sum_i < A[i] | G[k,i] > = 0
    """

    constraint: List[Tuple[int, NDArray[np.float64] | NDArray[np.complex64]]]
