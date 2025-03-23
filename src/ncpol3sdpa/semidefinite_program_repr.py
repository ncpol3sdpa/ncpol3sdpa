import numpy as np
from typing import Tuple, List
from numpy.typing import NDArray

# class ConstraintType(Enum):
#     EqualZero = 1

# TODO: switch the matrices to a sparse format, like scipy.sparse.coo_array
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array

class EqConstraint:
    def __init__(self, from_l : list[Tuple[int, NDArray[np.float64]]]) -> None:
        """represents SUM over i < As[i].snd | G_g_j > = 0 where j = As[i].fs"""
        self.constraints = from_l

class MomentMatrixSDP:
    """ This is an represents size x size symmetric positive 
         matrix variable. The coefficients in each equivalence class are considered to be equal """

    def __init__(self, size: int, eq_classes : List[List[Tuple[int, int]]]):
        self.size = size 
        self.eq_classes = eq_classes

        # Validation
        once = set([])
        for eq_class in eq_classes:
            for (i,j) in eq_class:
                assert 0 <= i < size
                assert 0 <= j <= i
                assert (i,j) not in once
                once.add((i,j))

# high level sdp representation
class ProblemSDP:
    """ An efficient representation of an SDP that is easily translatable to SDP solvers. """

    def __init__(self, moment_matrix : MomentMatrixSDP, objective : NDArray[np.float64]) -> None:
        self.moment_matrix = moment_matrix
        # The number of elements in this list is the number of variables.
        # Each variable is a positive semi-definite matrix
        self.MOMENT_MATRIX_VAR_NUM = 0
        self.variable_sizes = [moment_matrix.size]
        self.objective = objective
        self.constraints : List[EqConstraint] = []
        assert(objective.shape == (moment_matrix.size, moment_matrix.size))

    def add_symmetric_variable(self, matrix_size : int) -> None:
        self.variable_sizes.append(matrix_size)

    def eq_2_coefs_constraint(self, 
        coef1: Tuple[int, int], 
        coef2: Tuple[int, int],
        var_number :int,
    ) -> EqConstraint:
        x,y = coef2
        i,j = coef1
        assert coef1 != coef2
        a = np.zeros(shape = (self.variable_sizes[var_number], self.variable_sizes[var_number]))
        a[i][j] += 0.5
        a[j][i] += 0.5
        a[x][y] -= 0.5
        a[y][x] -= 0.5

        return EqConstraint([(var_number, a)])

    def compile_moment_matrix_to_constraints(self) -> None:
        """Converts the equivalence class representation of the moment matrix to low level linear
        constraints. Equivalence classes are removed to prevent errors."""

        for eq_class in self.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            central_coef = eq_class.pop() 
            for coef in eq_class:
                self.constraints.append(\
                    self.eq_2_coefs_constraint(central_coef, coef, var_number = self.MOMENT_MATRIX_VAR_NUM))
            eq_class = []
        
        # the structure of the equality constraints is star:
        # s0= s1, s0 = s2, s0 = s3, ...
        # TODO/Idea: What if it was a chain(s0 = s1, s1 = s2, s2 = s3, ...) or a balanced tree?