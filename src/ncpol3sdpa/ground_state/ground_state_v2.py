# import numpy as np
from typing import Dict, Tuple, List, Any
from ncpol3sdpa import Constraint, Problem
from sympy.physics.quantum import HermitianOperator


""""
class Pauli:
    Id = np.array([[1, 0], [0, 1]])
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])

"""

""""
class Variables:
    Id = HermitianOperator("Id")  # type: ignore
    X = HermitianOperator("X")  # type: ignore
    Y = HermitianOperator("Y")  # type: ignore
    Z = HermitianOperator("Z")  # type: ignore

    Id_var = Matrix([[1, 0], [0, 1]])
    X_var = Matrix([[0, 1], [1, 0]])
    Y_var = Matrix([[0, -1j], [1j, 0]])
    Z_var = Matrix([[1, 0], [0, -1]])

"""

"""def transform_pauli_matrices(n: int, i: int, W: Matrix) -> np.ndarray:
    return  Wi the associated matrix of Pauli W "translated" i-times to the right with tensor products

    for a in range(i - 1):
        W = TensorProduct(Variables.Id_var, W)  # produit tensoriel de matrice

    for b in range(i, n):
        W = TensorProduct(W, Variables.Id_var)
    return W

"""


class Ground_state2:
    def __init__(
        self,
        number_of_edges: int,
        list_of_edges: Dict[Tuple[int, int], int],
    ) -> None:
        self.number_of_edges = number_of_edges
        self.list_of_edges = list_of_edges

    """def create_list_matrices_X(self) -> List[np.ndarray]:
        number_of_edges = self.number_of_edges
        list_of_X: List[np.ndarray] = []
        for i in range(number_of_edges):  ##list_of_X = [X1, X2, X3...]
            list_of_X.append(
                transform_pauli_matrices(number_of_edges, i, np.array([[0, 1], [1, 0]]))
            )
        return list_of_X

    def create_list_matrices_Y(self) -> List[np.ndarray]:
        number_of_edges = self.number_of_edges
        list_of_Y: List[np.ndarray] = []
        for i in range(number_of_edges):
            list_of_Y.append(
                transform_pauli_matrices(
                    number_of_edges, i, np.array([[0, -1j], [1j, 0]])
                )
            )
        return list_of_Y

    def create_list_matrices_Z(self) -> List[np.ndarray]:
        number_of_edges = self.number_of_edges
        list_of_Z: List[np.ndarray] = []
        for i in range(number_of_edges):
            list_of_Z.append(
                transform_pauli_matrices(
                    number_of_edges, i, np.array([[1, 0], [0, -1]])
                )
            )
        return list_of_Z

    """

    def create_variables_X(self) -> List[HermitianOperator]:
        list_of_X: List[HermitianOperator] = []
        for i in range(self.number_of_edges):
            x = HermitianOperator("x")  # type: ignore
            list_of_X.append(x)
        return list_of_X

    def create_variables_Y(self) -> List[HermitianOperator]:
        list_of_Y: List[HermitianOperator] = []
        for i in range(self.number_of_edges):
            y = HermitianOperator("y")  # type: ignore
            list_of_Y.append(y)
        return list_of_Y

    def create_variables_Z(self) -> List[HermitianOperator]:
        list_of_Z: List[HermitianOperator] = []
        for i in range(self.number_of_edges):
            z = HermitianOperator("z")  # type: ignore
            list_of_Z.append(z)
        return list_of_Z

    def add_to_hermitian_matrix(self, i: int, j: int) -> Any:
        """return Hij : the hermitian matrix associated to the edge i-j"""
        list_of_X = self.create_variables_X()
        list_of_Y = self.create_variables_Y()
        list_of_Z = self.create_variables_Z()

        res = (
            -list_of_X[i] * list_of_X[j]
            - list_of_Y[i] * list_of_Y[j]
            - list_of_Z[i] * list_of_Z[j]
        )
        return res

    def create_hermitian_matrix(
        self, number_of_edges: int, list_of_edges: Dict[Tuple[int, int], int]
    ) -> HermitianOperator:
        H = 0
        for i in range(number_of_edges - 1):
            for j in range(i + 1, number_of_edges):
                if (
                    list_of_edges.get((i, j), 0) == 1
                ):  ##renvoie 0 si la clé n'est pas dans le dictionnaire
                    H += self.add_to_hermitian_matrix(i, j)
        return H  # type: ignore

    def solve_ground_state(self) -> float:
        number_of_edges = self.number_of_edges
        list_of_edges = self.list_of_edges

        obj = -self.create_hermitian_matrix(number_of_edges, list_of_edges)

        p = Problem(obj, is_commutative=False, is_real=False)

        list_of_X: List[HermitianOperator] = self.create_variables_X()
        list_of_Y: List[HermitianOperator] = self.create_variables_Y()
        list_of_Z: List[HermitianOperator] = self.create_variables_Z()

        list_of_list = [list_of_X, list_of_Y, list_of_Z]

        for i in range(1, number_of_edges):
            for j in range(1, number_of_edges):
                for a in range(2):
                    for b in range(a + 1, 3):
                        if i != j:
                            p.add_rule(
                                list_of_list[a][i] * list_of_list[b][j],
                                list_of_list[b][j] * list_of_list[a][i],
                            )

        for a in range(3):
            for i in range(number_of_edges):
                p.add_rule(list_of_list[a][i] * list_of_list[a][i], 1)  # type: ignore

        for i in range(number_of_edges):
            c1 = Constraint.EqualityConstraint(
                list_of_X[i] * list_of_Y[i] - 1j * list_of_Z[i]
            )
            p.add_constraint(c1)

            c2 = Constraint.EqualityConstraint(
                list_of_Z[i] * list_of_X[i] - 1j * list_of_Y[i]
            )
            p.add_constraint(c2)

            c3 = Constraint.EqualityConstraint(
                list_of_Y[i] * list_of_Z[i] - 1j * list_of_X[i]
            )
            p.add_constraint(c3)

        for i in range(number_of_edges):
            for a in range(2):
                for b in range(a + 1, 3):
                    c = Constraint.EqualityConstraint(
                        list_of_list[a][i] * list_of_list[b][i]
                        + list_of_list[b][i] * list_of_list[a][i]
                    )
                    p.add_constraint(c)

        return -p.solve(2)
