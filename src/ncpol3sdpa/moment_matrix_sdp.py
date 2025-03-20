from __future__ import annotations
from typing import List, Tuple, Dict, Any
from ncpol3sdpa.rules import apply_rule
import sympy
from numpy.typing import NDArray
import numpy as np

class UnionFindEntry:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y
        self.rank = 0

# SDP Moment matrix representation
class MomentMatrixSDP:
    """ This is an implicit moment_matrix_size x moment_matrix_size symmetric positive matrix variable, say G
    There is a union find data structure to mark which coefficients inside the matrix should be considered 
    equal. """

    def __init__(self, matrix_size : int) -> None:
        self.matrix_size = matrix_size
        self.constraints : list[ConvexEqConstraint] = []

        # This is the union find. Only use the upper half of this matrix because we already know 
        # that G is symmetric. Could be optimized here if needed
        self._equal_coefficients = [[UnionFindEntry(i,j)] \
                                        for i in range(matrix_size) \
                                        for j in range(matrix_size)]

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


def create_moment_matrix_in_SDP(
        monomials : List[sympy.Poly], 
        rules : Dict[sympy.Poly, Any]
    ) -> MomentMatrixSDP :
    """Construct the representation of the SDP Moment Matrix"""

    n : int = len(monomials)
    position_of_monomial : Dict[sympy.Poly, Tuple[int, int]] = {}
    result_matrix_SDP = MomentMatrixSDP(n)

    for i, monomial1 in enumerate(monomials):
        for j in range(i,n):
            monomial2 = monomials[j]
            monomial_ij : sympy.Poly = apply_rule(monomial1 * monomial2, rules)
            if monomial_ij not in position_of_monomial.keys():
                position_of_monomial[monomial_ij] = (i, j)
            else:
                # Union find is very overkill for this... It does have the advantage of being able to
                # represent only valid states. Something to think about.
                result_matrix_SDP.union((i,j), position_of_monomial[monomial_ij])

    return result_matrix_SDP

def objective_to_matrix(objective : sympy.Poly, relaxation_order : int, \
        position_of_monomial : Dict[sympy.Poly, Tuple[int, int]]) -> NDArray[np.float64]:
    """Transform the polynomial representation to a matrix representation.
    In other words gives A such that: objective = Tr(A.T x M))"""

    result = np.zeros(shape = (relaxation_order, relaxation_order), dtype = np.float64)

    Gg_ij = objective.as_coefficients_dict()
    for monomial, coef in Gg_ij.items():
        assert monomial in position_of_monomial.keys(), \
               "Constraint matrix is too small for the required objective"
        i, j = position_of_monomial[monomial]
        result[i,j] = coef
    return result
