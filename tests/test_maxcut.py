from typing import Optional
import numpy as np
from numpy.typing import NDArray

from ncpol3sdpa.problem import Problem
from ncpol3sdpa.funs import generate_n_variables
from ncpol3sdpa.constraints import Constraint


# TODO :
# > move dans une partie examples
# > ajouter assert (fonctions sur graphe notamment)

def gen_random_matrix(n: int) -> NDArray[np.float64]:
    """Returns a random numpy symmetric matrix, with constant diagonals"""
    W = np.zeros((n, n))
    for k in range(1, n):
        if np.random.randint(2):  # 1 / 2 probability
            W += np.diag(np.ones(n - k), k)

    return W + W.T  # make it symmetric

def gen_bipartite_graph(n : int, k : int) -> NDArray[np.float64]:
    """ Generates a random n-vertices bipartite graph
     The bipartition consists in the vertices [0, ... k - 1] and [k, ... n - 1]
     Purpose : computation of maxcut optimum is polynomial -> testing efficiency for big graphs """
    ...

def solve_maxcut_bipartite(g : NDArray[np.float64], k : int) -> int:
    """ Efficient polynomial-time solving of Maxcut on bipartite graphs 
     Useful for testing relaxation efficiency on larger graphs """
    ...

def solve_maxcut_naive(g : NDArray[np.float64]) -> int:
    """ Implements naive algorithm for maxcut 
     Purpose is providing a check + testing relaxation efficiency """
    ...

# taken from example on ncpol2sdpa - examples
W0 = W = (
    np.diag(np.ones(8), 1)
    + np.diag(np.ones(7), 2)
    + np.diag([1, 1], 7)
    + np.diag([1], 8)
)
W0 = W0 + W0.T


def test_maxcut(n: int = 8, M: Optional[NDArray[np.float64]] = None) -> None:
    """Max-Cut example; if M is None, gen_random_matrix is called"""
    if M is None:
        M = gen_random_matrix(n)
    x = generate_n_variables(n)

    maxcut_constraints = [
        Constraint.EqualityConstraint(xi**2 - xi) for xi in x
    ]  # equality : xi in {0, 1}
    e = np.ones(n)
    # C'est enervant de typer ce type d'expression: il est mal typé.
    # mais il n'est pas faux non plus. TODO
    maxcut_objective = np.dot(x, np.dot(M, e - np.transpose(x)))  # type: ignore

    maxcut = Problem(maxcut_objective)
    maxcut.add_constraints(maxcut_constraints)

    maxcut.solve()
