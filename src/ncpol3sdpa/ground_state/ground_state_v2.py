import numpy as np
from typing import Dict, Tuple, List
from ncpol3sdpa import Constraint, Problem


class Pauli:
    Id = np.array([[1, 0], [0, 1]])
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])


def transform_pauli_matrices(n: int, i: int, W: np.ndarray) -> np.ndarray:
    """return the associated matrix of Pauli "translated" i-times to the right"""
    Id = np.array([[1, 0], [0, 1]])

    for a in range(i - 1):
        W = np.kron(Id, W)  # produit tensoriel de matrice

    for b in range(i, n):
        W = np.kron(W, Id)
    return W


class Ground_state2:
    def __init__(
        self,
        number_of_edges: int,
        # list_of_edges : List[int, int, int],
        list_of_edges: Dict[Tuple[int, int], int],
    ) -> None:
        self.number_of_edges = number_of_edges
        self.list_of_edges = list_of_edges

    def add_to_hermitian_matrix(self, i: int, j: int) -> np.ndarray:
        """return Hij : the hermitian matrix associated to the edge i-j"""
        return (
            Pauli.Id
            - np.kron(Pauli.X[i], Pauli.X[j])
            - np.kron(Pauli.Y[i], Pauli.Y[j])
            - np.kron(Pauli.Z[i], Pauli.Z[j])
        )

    def create_hermitian_matrix(
        self, number_of_edges: int, list_of_edges: Dict[Tuple[int, int], int]
    ) -> np.ndarray:
        H = np.zeros((2, 2))
        for i in range(number_of_edges - 1):
            for j in range(i + 1, number_of_edges):
                if list_of_edges[i, j] == 1:
                    H += self.add_to_hermitian_matrix(i, j)
        return H

    def solve_ground_state(self) -> float:
        number_of_edges = self.number_of_edges
        list_of_edges = self.list_of_edges

        obj = self.create_hermitian_matrix(number_of_edges, list_of_edges)

        p = Problem(obj, is_commutative=False, is_real=False)

        list_of_X: List[np.ndarray] = []
        list_of_Y: List[np.ndarray] = []
        list_of_Z: List[np.ndarray] = []

        for i in range(number_of_edges):  ##list_of_X = [X1, X2, X3...]
            list_of_X.append(
                transform_pauli_matrices(number_of_edges, i, np.array([[0, 1], [1, 0]]))
            )
            list_of_Y.append(
                transform_pauli_matrices(
                    number_of_edges, i, np.array([[0, -1j], [1j, 0]])
                )
            )
            list_of_Z.append(
                transform_pauli_matrices(
                    number_of_edges, i, np.array([[1, 0], [0, -1]])
                )
            )

        list_of_list = [list_of_X, list_of_Y, list_of_Z]

        for i in range(number_of_edges):
            for j in range(number_of_edges):
                for a in range(3):
                    for b in range(3):
                        if i != j:
                            p.add_rule(
                                list_of_list[a][i] @ list_of_list[b][j],
                                list_of_list[b][j] @ list_of_list[a][i],
                            )

        for a in range(3):
            for i in range(number_of_edges):
                p.add_rule(list_of_list[a][i] * list_of_list[a][i], 1)

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
                for b in range(1, 3):
                    c = Constraint.EqualityConstraint(
                        list_of_list[a][i] * list_of_list[b][i]
                        + list_of_list[b][i] * list_of_list[a][i]
                    )
                    p.add_constraint(c)

        return p.solve_uncheked(2)
