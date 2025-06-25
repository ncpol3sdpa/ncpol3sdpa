from typing import Tuple

from scipy.sparse import lil_matrix


class InequalityScalarConstraint:
    def __init__(self, constraint: Tuple[int, lil_matrix]) -> None:
        """
        Represent a scalar inequality constraint
        < A | G[k] >
        """

        self.constraints = constraint
