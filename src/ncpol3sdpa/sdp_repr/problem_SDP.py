from __future__ import annotations
from typing import List, Tuple

import numpy as np
from scipy.sparse import lil_matrix, hstack, vstack

from .moment_matrix_SDP import MomentMatrixSDP
from .eq_constraint import EqConstraint
from .inequality_scalar_constraint import InequalityScalarConstraint

# for validation
EPSILON = 0.001


# high level sdp representation
class ProblemSDP:
    """An efficient representation of an SDP that is easily translatable to SDP solvers."""

    def __init__(
        self,
        moment_matrix: MomentMatrixSDP,
        objective: lil_matrix,
        is_real: bool = True,
    ) -> None:
        # The moment matrix should always be in position 0
        self.__MOMENT_MATRIX_VAR_NUM: int = 0

        self.__moment_matrix: MomentMatrixSDP = moment_matrix
        # The number of elements in this list is the number of variables.
        # Each variable is a positive semi-definite matrix
        self.__variable_sizes: List[int] = [moment_matrix.size]
        self.__objective: lil_matrix = objective
        self.constraints: List[EqConstraint] = []
        self.inequality_scalar_constraints: List[InequalityScalarConstraint] = []
        self.is_real = is_real

        assert objective.shape == (moment_matrix.size, moment_matrix.size)

    def __str__(self) -> str:
        s = (
            "SDP translation:\n"
            + f".objective: \n {self.objective.toarray()}\n"
            + f".variable_sizes: {self.variable_sizes}\n"
            + "Moment matrix: \n"
            + f"    .moment_matrix.size: \n {self.moment_matrix.size}\n"
            + f"    .moment_matrix.eq_classes: \n {self.moment_matrix.eq_classes}\n"
            + ".constraints:\n"
        )

        for c in self.constraints:
            for c2 in c.constraints:
                s = s + str(c2[0]) + "\n" + str(c2[1].toarray()) + "\n"
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
    def objective(self) -> lil_matrix:
        """The objective matrix"""
        return self.__objective

    # --- internal functions ---

    def _eq_2_coefs_constraint_re(
        self,
        coef1: Tuple[int, int],
        coef2: Tuple[int, int],
        var_number: int,
    ) -> EqConstraint:
        x, y = coef2
        i, j = coef1
        assert coef1 != coef2
        a = lil_matrix(
            (self.variable_sizes[var_number], self.variable_sizes[var_number]),
            dtype=np.float64 if self.is_real else np.complex64,  # type:ignore
        )

        a[i, j] += 0.5
        a[j, i] += 0.5
        a[x, y] -= 0.5
        a[y, x] -= 0.5

        return EqConstraint([(var_number, a)])

    def _eq_2_coefs_constraint_im(
        self,
        coef1: Tuple[int, int],
        coef2: Tuple[int, int],
        var_number: int,
    ) -> EqConstraint:
        x, y = coef2
        i, j = coef1
        assert coef1 != coef2
        a = lil_matrix(
            (self.variable_sizes[var_number], self.variable_sizes[var_number]),
            dtype=np.float64 if self.is_real else np.complex64,  # type: ignore
        )

        a[i, j] += 0.5j
        a[j, i] -= 0.5j
        a[x, y] -= 0.5j
        a[y, x] += 0.5j

        return EqConstraint([(var_number, a)])

    # --- methods ---

    # use in mosek_solver
    def compile_moment_matrix_to_constraints(self) -> None:
        """Converts the equivalence class representation of the moment matrix to low level linear
        constraints. Equivalence classes are removed to prevent errors."""

        for eq_class in self.moment_matrix.eq_classes:
            assert len(eq_class) > 0
            central_coef = eq_class.pop()
            for coef in eq_class:
                # constraint on the real part of the coefficients
                self.constraints.append(
                    self._eq_2_coefs_constraint_re(
                        central_coef, coef, var_number=self.MOMENT_MATRIX_VAR_NUM
                    )
                )
                # constraint on the imaginary part of the coefficients
                if not self.is_real:
                    self.constraints.append(
                        self._eq_2_coefs_constraint_im(
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
        size = self.moment_matrix.size

        self.compile_moment_matrix_to_constraints()
        real_moment_matrix = MomentMatrixSDP(2 * size, [])

        # creation of the real objective
        objective = complexMatrix_to_realMatrix(self.objective)

        # create the real sdp
        real_sdp = ProblemSDP(real_moment_matrix, objective)
        real_sdp.variable_sizes = [2 * size for size in self.variable_sizes]

        # adding constraints
        for constraint in self.constraints:
            real_sdp.constraints.append(
                EqConstraint(
                    [
                        (matrix_num, complexMatrix_to_realMatrix(matrix_constraint))
                        for matrix_num, matrix_constraint in constraint.constraints
                    ]
                )
            )

        for constraint in self.inequality_scalar_constraints:  # type: ignore
            var_num, mat = constraint.constraints
            real_mat = complexMatrix_to_realMatrix(mat)  # type: ignore
            real_sdp.inequality_scalar_constraints.append(
                InequalityScalarConstraint((var_num, real_mat))  # type: ignore
            )

        # create all the new sdp vars constraints
        for i in range(len(self.__variable_sizes)):
            complexSDPvar_to_realSDPvar(self, real_sdp, i)

        return real_sdp


def complexSDPvar_to_realSDPvar(
    complex_sdp: ProblemSDP, real_sdp: ProblemSDP, num_var: int
) -> None:
    """
    Add the real sdp var in the real sdp.
    The num_var of the real_sdp must be the same as the complex_sdp
    """
    pre_var = complex_sdp.variable_sizes[num_var]
    new_var = 2 * pre_var

    for j in range(pre_var):
        for i in range(j + 1):
            m = lil_matrix(
                (new_var, new_var)
            )  # we can optimize it by creating only one lil_matrix before the loop and just change the coefficients
            m[i, j] = 1
            m[i + pre_var, j + pre_var] = -1

            m[j, i] = 1
            m[j + pre_var, i + pre_var] = -1
            real_sdp.constraints.append(EqConstraint([(num_var, m)]))

    for j in range(pre_var):
        for i in range(j + 1):
            m = lil_matrix((new_var, new_var))
            m[i, j + pre_var] = 1
            m[j, i + pre_var] = 1

            m[j + pre_var, i] = 1
            m[i + pre_var, j] = 1
            real_sdp.constraints.append(EqConstraint([(num_var, m)]))


def complexMatrix_to_realMatrix(
    X: lil_matrix,
) -> lil_matrix:
    if X.shape[0] != X.shape[1]:
        raise ValueError("The matrix must be square")

    X_re = X.real.multiply(0.5)
    X_im = X.imag.multiply(0.5)

    upper = hstack([X_re, -X_im])
    lower = hstack([X_im, X_re])

    result = vstack([upper, lower]).tolil()
    return result
