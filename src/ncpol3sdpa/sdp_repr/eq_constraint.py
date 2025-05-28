from typing import Tuple, List

from scipy.sparse import lil_matrix

# class ConstraintType(Enum):
#     EqualZero = 1

# TODO: switch the matrices to a sparse format, like scipy.sparse.coo_array
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array


class EqConstraint:
    def __init__(self, from_l: List[Tuple[int, lil_matrix]]) -> None:
        """Represents a list of constraints

        A tuple (k, A) represents the constraint :
        sum_i < A[i] | G[k,i] > = 0
        """

        self.constraints = from_l
