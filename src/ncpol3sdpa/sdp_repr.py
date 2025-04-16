import numpy as np
from typing import Tuple, List
from numpy.typing import NDArray

# class ConstraintType(Enum):
#     EqualZero = 1

# TODO: switch the matrices to a sparse format, like scipy.sparse.coo_array
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array

# for validation
EPSILON = 0.001


class EqConstraint:
    """Represents a list of constraints

    A tuple (k, A) represents the constraint :
    sum_i < A[i] | G[k,i] > = 0
    """

    def __init__(self, from_l: List[Tuple[int, NDArray[np.float64]]]) -> None:
        self.constraints = from_l


class MomentMatrixSDP:
    """This is an represents size x size symmetric positive
    matrix variable. The coefficients in each equivalence class are considered to be equal"""

    def __init__(self, size: int, eq_classes: List[List[Tuple[int, int]]]):
        self.size = size
        self.eq_classes = eq_classes

        # Validation
        once = set()
        for eq_class in eq_classes:
            for i, j in eq_class:
                assert 0 <= i < size
                assert 0 <= j <= i
                assert (i, j) not in once
                once.add((i, j))


# high level sdp representation
class ProblemSDP:
    """An efficient representation of an SDP that is easily translatable to SDP solvers."""

    def __init__(
        self, moment_matrix: MomentMatrixSDP, objective: NDArray[np.float64]
    ) -> None:
        # The moment matrix should always be in position 0
        self.MOMENT_MATRIX_VAR_NUM = 0

        self.moment_matrix = moment_matrix
        # The number of elements in this list is the number of variables.
        # Each variable is a positive semi-definite matrix
        self.variable_sizes = [moment_matrix.size]
        self.objective: NDArray[np.float64] = objective
        self.constraints: List[EqConstraint] = []
        assert objective.shape == (moment_matrix.size, moment_matrix.size)

    def add_symmetric_variable(self, matrix_size: int) -> None:
        self.variable_sizes.append(matrix_size)

    def eq_2_coefs_constraint(
        self,
        coef1: Tuple[int, int],
        coef2: Tuple[int, int],
        var_number: int,
    ) -> EqConstraint:
        x, y = coef2
        i, j = coef1
        assert coef1 != coef2
        a = np.zeros(
            shape=(self.variable_sizes[var_number], self.variable_sizes[var_number])
        )
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
                self.constraints.append(
                    self.eq_2_coefs_constraint(
                        central_coef, coef, var_number=self.MOMENT_MATRIX_VAR_NUM
                    )
                )
            eq_class = []

        # the structure of the equality constraints is star:
        # s0= s1, s0 = s2, s0 = s3, ...
        # TODO/Idea: What if it was a chain(s0 = s1, s1 = s2, s2 = s3, ...)
        # or a balanced tree or a Union-Find structure?

    # --- Validation ---
    def is_constraint_verified(
        self, constraint: EqConstraint, variable_instances: List[NDArray[np.float64]]
    ) -> bool:
        """Verify if a constraint is satisfied"""
        sum = 0

        for var_num, a_matrix in constraint.constraints:
            sum += np.sum(np.multiply(a_matrix, variable_instances[var_num]))

        return abs(sum) < EPSILON

    def is_feasible(self, variable_instances: List[NDArray[np.float64]]) -> bool:
        """Verify that a given point is a feasible point of the problem"""
        for var_i in variable_instances:
            if np.linalg.norm(var_i - var_i.T, 1) > EPSILON:
                return False
            elif not (
                np.all(np.linalg.eigvals(var_i) >= -EPSILON)
            ):  # positive semidefinite
                return False

        moment_matrix = variable_instances[self.MOMENT_MATRIX_VAR_NUM]

        for eq_class in self.moment_matrix.eq_classes:
            eq_class_i = iter(eq_class)
            x, y = eq_class_i.__next__()
            for i, j in eq_class_i:
                if abs(moment_matrix[i][j] - moment_matrix[x][y]) > EPSILON:
                    return False

        for constraint in self.constraints:
            self.is_constraint_verified(constraint, variable_instances)

        return True

    def calculate_objective(
        self, variable_instances: List[NDArray[np.float64]]
    ) -> np.float64:
        """Calculate the objective function at a given point"""

        moment_matrix: NDArray[np.float64] = variable_instances[
            self.MOMENT_MATRIX_VAR_NUM
        ]
        res: np.float64 = np.sum(np.multiply(self.objective, moment_matrix))
        assert isinstance(res, np.float64)

        return res

    def __str__(self) -> str:
        return (
            "SDP translation:\n"
            + f".objective: \n {self.objective}\n"
            + f".variable_sizes: {self.variable_sizes}\n"
            + "Moment matrix: \n"
            + f"    .moment_matrix.size: \n {self.moment_matrix.size}\n"
            + f"    .moment_matrix.eq_classes: \n {self.moment_matrix.eq_classes}\n"
            + f".constraints: {[c.constraints for c in self.constraints]}"
        )
