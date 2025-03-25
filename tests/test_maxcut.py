import sympy
from typing import List
import numpy as np


def gen_random_matrix(n : int):
    """ Returns a random numpy symmetric matrix, with constant diagonals """
    W = np.zeros((n, n))
    for k in range(1, n):
        if np.random.randint(2):  # 1 / 2 probability
            W += np.diag(np.ones(n - k), k)
        
    return W + W.T  # make it symmetric


# taken from example on ncpol2sdpa - examples
W0 = W = np.diag(np.ones(8), 1) + np.diag(np.ones(7), 2) + np.diag([1, 1], 7) + np.diag([1], 8)
W0 = W0 + W0.T


