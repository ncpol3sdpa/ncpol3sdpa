from __future__ import annotations
from typing import List, Tuple

from numpy.typing import NDArray
import numpy as np

from .moment_matrix_SDP import MomentMatrixSDP
from .eq_constraint import EqConstraint

# for validation
EPSILON = 0.001


# high level sdp representation
class ProblemSDP:
    """An efficient representation of an SDP that is easily translatable to SDP solvers."""

    def __init__(
        self,
        moment_matrix: MomentMatrixSDP,
        objective: NDArray[np.float64] | NDArray[np.complex64],
    ) -> None:
        # The moment matrix should always be in position 0
        self.__MOMENT_MATRIX_VAR_NUM: int = 0

        self.__moment_matrix: MomentMatrixSDP = moment_matrix
        # The number of elements in this list is the number of variables.
        # Each variable is a positive semi-definite matrix
        self.__variable_sizes: List[int] = [moment_matrix.size]
        self.__objective: NDArray[np.complex64] | NDArray[np.float64] = objective
        self.__constraints: List[EqConstraint] = []

        assert objective.shape == (moment_matrix.size, moment_matrix.size)

    def __str__(self) -> str:
        s = (
            "SDP translation:\n"
            + f".objective: \n {self.objective}\n"
            + f".variable_sizes: {self.variable_sizes}\n"
            + "Moment matrix: \n"
            + f"    .moment_matrix.size: \n {self.moment_matrix.size}\n"
            + f"    .moment_matrix.eq_classes: \n {self.moment_matrix.eq_classes}\n"
            + ".constraints:\n"
        )

        for c in self.constraints:
            for c2 in c.constraints:
                s = s + str(c2[0]) + "\n" + str(c2[1]) + "\n"
            s = s + "\n"

        return s

    # --- Getter and Setter methods ---

    @property
    def MOMENT_MATRIX_VAR_NUM(self) -> int:
        """The number of the moment matrix variable"""
        return self.__MOMENT_MATRIX_VAR_NUM

    @MOMENT_MATRIX_VAR_NUM.setter
    def MOMENT_MATRIX_VAR_NUM(self, value: int) -> None:
        """Set the number of the moment matrix variable"""
        assert value >= 0
        self.__MOMENT_MATRIX_VAR_NUM = value

    @property
    def moment_matrix(self) -> MomentMatrixSDP:
        """The moment matrix"""
        return self.__moment_matrix

    @property
    def variable_sizes(self) -> List[int]:
        """The sizes of the variables"""
        return self.__variable_sizes

    @variable_sizes.setter
    def variable_sizes(self, value: List[int]) -> None:
        """Set the sizes of the variables"""
        self.__variable_sizes = value

    @property
    def objective(self) -> NDArray[np.complex64] | NDArray[np.float64]:
        """The objective matrix"""
        return self.__objective

    @property
    def constraints(self) -> List[EqConstraint]:
        """The constraints of the SDP"""
        return self.__constraints

    # --- unused ---

    # def _add_symmetric_variable(self, matrix_size: int) -> None:
    #     self.variable_sizes.append(matrix_size)

    # def _is_feasible(self, variable_instances: List[NDArray[np.float64]]) -> bool:
    #     """Verify that a given point is a feasible point of the problem"""
    #     for var_i in variable_instances:
    #         if np.linalg.norm(var_i - var_i.T, 1) > EPSILON:
    #             return False
    #         elif not (
    #             np.all(np.linalg.eigvals(var_i) >= -EPSILON)
    #         ):  # positive semidefinite
    #             return False

    #     moment_matrix = variable_instances[self.MOMENT_MATRIX_VAR_NUM]

    #     for eq_class in self.moment_matrix.eq_classes:
    #         eq_class_i = iter(eq_class)
    #         x, y = eq_class_i.__next__()
    #         for i, j in eq_class_i:
    #             if abs(moment_matrix[i][j] - moment_matrix[x][y]) > EPSILON:
    #                 return False

    #     for constraint in self.constraints:
    #         self._is_constraint_verified(constraint, variable_instances)

    #     return True

    # def _calculate_objective(
    #     self, variable_instances: List[NDArray[np.float64]]
    # ) -> np.float64:
    #     """Calculate the objective function at a given point"""

    #     moment_matrix: NDArray[np.float64] = variable_instances[
    #         self.MOMENT_MATRIX_VAR_NUM
    #     ]
    #     res: np.float64 = np.sum(np.multiply(self.objective, moment_matrix))
    #     assert isinstance(res, np.float64)

    #     return res

    # --- internal functions ---

    # inner function
    def _eq_2_coefs_constraint(
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

    # inner function
    def _is_constraint_verified(
        self, constraint: EqConstraint, variable_instances: List[NDArray[np.float64]]
    ) -> bool:
        """Verify if a constraint is satisfied"""
        sum = 0

        for var_num, a_matrix in constraint.constraints:
            sum += np.sum(np.multiply(a_matrix, variable_instances[var_num]))

        return abs(sum) < EPSILON

    # --- methods ---

    # use in mosek_solver
    def compile_moment_matrix_to_constraints(self) -> None:
        """Converts the equivalence class representation of the moment matrix to low level linear
        constraints. Equivalence classes are removed to prevent errors."""

        for eq_class in self.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            central_coef = eq_class.pop()
            for coef in eq_class:
                self.constraints.append(
                    self._eq_2_coefs_constraint(
                        central_coef, coef, var_number=self.MOMENT_MATRIX_VAR_NUM
                    )
                )
            eq_class = []

        # the structure of the equality constraints is star:
        # s0= s1, s0 = s2, s0 = s3, ...
        # TODO/Idea: What if it was a chain(s0 = s1, s1 = s2, s2 = s3, ...)
        # or a balanced tree or a Union-Find structure?

    # use in problem.py
    def complex_to_realSDP(self) -> ProblemSDP:
        # creation of the real moment matrix [[Hr, -Hi], [Hi, Hr]]
        real_eq_classes = []
        size = self.moment_matrix.size
        for eq_class in self.moment_matrix.eq_classes:
            new_eq_class00 = []
            new_eq_class01 = []
            new_eq_class10 = []
            for i, j in eq_class:
                new_eq_class00.append((i, j))
                new_eq_class00.append((i + size, j + size))
                new_eq_class01.append((i, j + size))
                new_eq_class10.append((i + size, j))
            real_eq_classes.append(new_eq_class00)
            real_eq_classes.append(new_eq_class01)
            real_eq_classes.append(new_eq_class10)
        real_moment_matrix = MomentMatrixSDP(2 * size, real_eq_classes)

        # creation of the real objective
        objective = complexMatrix_to_realMatrix(self.objective)

        # creation of the real SDP
        real_sdp = ProblemSDP(real_moment_matrix, objective)
        real_sdp.variable_sizes = self.variable_sizes
        real_sdp.variable_sizes[0] = 2 * size

        # adding constraints
        for constraint in self.constraints:
            c = constraint.constraints

            # equality constraint
            if len(c) == 1:
                matrix_constraint = complexMatrix_to_realMatrix(c[0][1])
                real_sdp.constraints.append(
                    EqConstraint([(real_sdp.MOMENT_MATRIX_VAR_NUM, matrix_constraint)])
                )

            # inequality constraint
            elif len(c) == 2:
                matrix_constraint = complexMatrix_to_realMatrix(c[0][1])
                real_sdp.constraints.append(
                    EqConstraint(
                        [(real_sdp.MOMENT_MATRIX_VAR_NUM, matrix_constraint), c[1]]
                    )
                )

        return real_sdp


def complexMatrix_to_realMatrix(
    X: NDArray[np.complex64] | NDArray[np.float64],
) -> NDArray[np.float64]:
    if X.shape[0] != X.shape[1]:
        raise ValueError("The matrix must be square")

    X_re = np.divide(np.real(X), 2)
    X_im = np.divide(np.imag(X), 2)

    upper = np.hstack([X_re, -X_im])
    lower = np.hstack([X_im, X_re])

    return np.vstack([upper, lower])
