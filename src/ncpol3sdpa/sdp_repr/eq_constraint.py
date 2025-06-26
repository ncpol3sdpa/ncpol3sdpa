from typing import Tuple, List, NamedTuple

from scipy.sparse import lil_matrix


class EqConstraint(NamedTuple):
    """Represents a list of constraints

    A tuple (k, A) represents the constraint :
    sum_i < A[i] | G[k,i] > = 0
    """

    constraints: List[Tuple[int, lil_matrix]]
