import numpy as np
from typing import Tuple
from numpy.typing import NDArray

# class ConstraintType(Enum):
#     EqualZero = 1

# TODO: switch the matrices to a sparse format, like scipy.sparse.coo_array
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array

class ConvexEqConstraint:
    def __init__(self, from_l : list[Tuple[int, NDArray[np.float64]]]) -> None:
        """represents SUM over i < As[i].snd | G_g_As[i].fst > = 0"""
        #  indice de variable v     v symetric r_j x r_j
        self.constraints = from_l


class UnionFindEntry:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y
        self.rank = 0

# high level sdp representation
class ProblemSDP:
    """ There is an implicit moment_matrix_size x moment_matrix_size symmetric positive matrix variable, say G
    Objective is a matrix of coefficients, such that the objective function is Tr(objective.T * G).
    There is a union find data structure to mark which coefficients inside the matrix should be considered 
    equal. """

    
    def __init__(self, moment_matrix_size : int, objective : NDArray[np.float64]) -> None:
        self.moment_matrix_size = moment_matrix_size
        self.objective = objective
        self.constraints : list[ConvexEqConstraint] = []
        # This is the union find. Only use the upper half of this matrix because we already know 
        # that G is symmetric. Could be optimized here if needed
        self._variable_sizes = [moment_matrix_size] # considered positive semi-definite
        self._equal_coefficients = [[UnionFindEntry(i,j)] \
                                        for i in range(moment_matrix_size) \
                                        for j in range(moment_matrix_size)]

    def add_symmetric_variable(self, matrix_size : int) -> None:
        self._variable_sizes.append(matrix_size)

    def add_eq_constraint(self, convex_constraint : ConvexEqConstraint) -> None:
        self.convex_constraint = convex_constraint

    def are_equivalent(self, coef_cord1 : Tuple[int, int], coef_cord2 :Tuple[int, int]) -> bool:
        """Returns true if the both coefficient are in the same equivalence class.
        coefficients m ust be above the diagonal (x >= y) """
        repr1 = self._find(coef_cord1)
        repr2 = self._find(coef_cord2)
        return repr1 == repr2
    
    def union(self, coef_cord1 : Tuple[int, int], coef_cord2 : Tuple[int, int],) -> None:
        """Declare two coefficients in the moment matrix as the same
        coefficients m ust be above the diagonal (x >= y)"""
        entry_1 = self._find(coef_cord1)
        entry_2 = self._find(coef_cord2)

        # union by rank optimisation
        if entry_1.rank > entry_2.rank:
            entry_1, entry_2 = entry_2, entry_1
        
        entry_2.x, entry_2.y = entry_1.x, entry_1.y 
   
        if entry_2.rank == entry_1.rank:
            entry_2.rank += 1

    def _find(self, coef_cord1 : Tuple[int, int]) -> UnionFindEntry:
        """ Find the representative of an equivalence class in the moment matrix   
        coefficients m ust be above the diagonal (x >= y)"""
        (cursor_x, cursor_y) = coef_cord1
        assert(cursor_x >= cursor_y)
        next_entry = self._equal_coefficients[cursor_x][cursor_y]
        if (cursor_x, cursor_y) != (next_entry.x, next_entry.y):
            # Recursive function is really the best way to implement this, but not the best in python maybe
            result = self._find((next_entry.x, next_entry.y))
            # path shortening
            self._equal_coefficients[cursor_x][cursor_y] = result
            return result
        else:
            return next_entry
