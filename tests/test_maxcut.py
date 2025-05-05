import numpy as np
from examples.maxcut import maxcut_relaxation


def test_maxcut_relaxation() -> None:
    """Max-Cut example; if M is None, gen_random_matrix is called"""
    # coming soon
    W0 = np.diag(np.ones(8), 1)
    W0 = W0 + W0.T
    res = maxcut_relaxation(9, W0)

    assert res <= 1
