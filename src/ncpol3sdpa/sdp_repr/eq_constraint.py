from typing import Tuple, List, Union

import numpy as np
from numpy.typing import NDArray

# class ConstraintType(Enum):
#     EqualZero = 1

# TODO: switch the matrices to a sparse format, like scipy.sparse.coo_array
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array


class EqConstraint:
    def __init__(
        self,
        from_l: List[Tuple[int, Union[NDArray[np.float64], NDArray[np.complex64]]]],
    ) -> None:
        """Represents a list of constraints

        A tuple (k, A) represents the constraint :
        sum_i < A[i] | G[k,i] > = 0
        """

        self.constraints = from_l
