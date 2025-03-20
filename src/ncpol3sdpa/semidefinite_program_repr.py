import numpy as np
import sympy
from typing import Tuple
from numpy.typing import NDArray
from typing import List, Dict
from moment_matrix_sdp import MomentMatrixSDP

# class ConstraintType(Enum):
#     EqualZero = 1

# TODO: switch the matrices to a sparse format, like scipy.sparse.coo_array
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array

class ConvexEqConstraint:
    def __init__(self, from_l : list[Tuple[int, NDArray[np.float64]]]) -> None:
        """represents SUM over i < As[i].snd | G_g_As[i].fst > = 0"""
        #  indice de variable v     v symetric r_j x r_j
        self.constraints = from_l


# high level sdp representation
class ProblemSDP:
    """ An efficient representation of an SDP that is easily translatable to SDP solvers. """

    def __init__(self, moment_matrix : MomentMatrixSDP, objective : NDArray[np.float64]) -> None:
        self.moment_matrix = moment_matrix
        self.objective = objective
        self.constraints : list[ConvexEqConstraint] = []
        self._variable_sizes = [moment_matrix.matrix_size] # variables considered positive semi-definite
        assert(objective.shape == (moment_matrix.matrix_size, moment_matrix.matrix_size))

    def add_symmetric_variable(self, matrix_size : int) -> None:
        self._variable_sizes.append(matrix_size)

    def add_constraint_positive(self, monomials_to_pos : Dict[sympy.Monomial, Tuple[int, int]], \
        constraint_moment_matrix: List[List[sympy.Poly]]) -> None:
        """From a moment matrix, generate the variables that represent this constraint"""
        p = len(constraint_moment_matrix)
        assert(p >= 0)
        assert(p == len(constraint_moment_matrix[0]))

        for i in range(p):
            for j in range(i, p):
                # This is a polynomial in the i,j th place of the constraint matrix
                Gg_ij = constraint_moment_matrix[i][j].as_coefficients_dict()
                for monomial, coef in Gg_ij.items():
                    assert monomial in monomials_to_pos.keys(), \
                           "Constraint matrix is too small for the required objective"
                    x, y = monomials_to_pos[monomial]
                    # TODO

        self.convex_constraint.append(blah)
