import numpy as np
from numpy.typing import NDArray
from sympy import Expr

from ncpol3sdpa.problem import Problem
from ncpol3sdpa.funs import generate_n_variables, ith_bit
from ncpol3sdpa.constraints import Constraint


# TODO :
# > move dans une partie examples*
# > ajouter assert (fonctions sur graphe notamment)


def gen_random_matrix(n: int) -> NDArray[np.float64]:
    """Returns a random numpy symmetric matrix, with constant diagonals"""
    W = np.zeros((n, n))
    for k in range(1, n):
        if np.random.randint(2):  # 1 / 2 probability
            W += np.diag(np.ones(n - k), k)

    return W + W.T  # make it symmetric


def gen_bipartite_graph(n: int, k: int) -> NDArray[np.float64]:
    """Generates a random n-vertices bipartite graph
    The bipartition consists in the vertices [0, ... k - 1] and [k, ... n - 1]
    Purpose : computation of maxcut optimum is polynomial -> testing efficiency for large graphs"""
    g = np.zeros((n, n))
    for s in range(k):
        for t in range(k, n):
            if np.random.randint(2):
                g[s, t] = 1
                g[t, s] = 1
    return g


def solve_maxcut_bipartite(g: NDArray[np.float64], k: int) -> int:
    """Efficient polynomial-time solving of Maxcut on bipartite graphs
    Useful for testing relaxation efficiency on larger graphs"""
    n = len(g)
    n_edges = 0
    for s in range(k):
        n_edges += sum(g[s, i] for i in range(k, n))

    return n_edges  # is actually the optimum for bipartite graphs


def solve_maxcut_naive(g: NDArray[np.float64]) -> int:
    """Implements naive algorithm for maxcut
    Purpose is providing a check + testing relaxation efficiency"""

    n = len(g)
    if n > 20:  # a bit verbose ??
        print(
            "Warning : Maxcut-naive called with big arguments; do you want to continue ? "
        )

    max_edges = 0
    # we iterate over the 2^(n - 1) bipartitions
    for bp in range(2 ** (n - 1)):
        # i-th bit of bp indicates whether i is in the same part as (n - 1) or not
        n_edges = 0
        for s in range(n - 1):
            for t in range(s + 1, n - 1):
                n_edges += g[s, t] * (ith_bit(bp, s) ^ ith_bit(bp, t))
                # adds 1 iff s and t in different parts & {s, t} is an edge of g
            if not ith_bit(bp, s):
                n_edges += g[s, n - 1]

        max_edges = max(n_edges, max_edges)
    return max_edges


def maxcut_relaxation(n: int = 8, M: NDArray[np.float64] | None = None) -> float:
    """Max-Cut example; if M is None, gen_random_matrix is called"""

    if M is None:
        M = gen_random_matrix(n)

    x = np.array(generate_n_variables(n))

    maxcut_constraints = [
        Constraint.EqualityConstraint(xi**2 - xi) for xi in x
    ]  # equality : xi in {0, 1}

    maxcut_objective: Expr = np.dot(x, np.dot(M, np.ones(n) - np.transpose(x)))

    print(f"{x[0] = }")
    print(f"{type(x[0]) = }")

    maxcut = Problem(maxcut_objective)
    maxcut.add_constraints(maxcut_constraints)

    return maxcut.solve()


if __name__ == "__main__":
    # taken from example on ncpol2sdpa - examples
    W0 = W = (
        np.diag(np.ones(8), 1)
        + np.diag(np.ones(7), 2)
        + np.diag([1, 1], 7)
        + np.diag([1], 8)
    )
    W0 = W0 + W0.T

    print("Running maxcut_relaxation on example : ")
    print(maxcut_relaxation(8, W0))
