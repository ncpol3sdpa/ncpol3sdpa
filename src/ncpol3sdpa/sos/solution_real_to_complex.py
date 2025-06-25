import numpy as np

from numpy.typing import NDArray
from typing import TypeVar

from ncpol3sdpa.sdp_solution import Solution_SDP

T = TypeVar("T", bound=np.generic)


def matrix_real_to_complex(s: NDArray[np.float64]) -> NDArray[np.complex64]:
    """Symmetric s of dimetion 2n converted to hermetian matrix"""
    (p, m) = np.shape(s)
    assert p == m
    assert p % 2 == 0
    n = p // 2
    # fmt: off
    s11 = s[0:n  , 0:n  ]
    s12 = s[0:n  , n:2*n]
    s21 = s[n:2*n, 0:n  ]
    s22 = s[n:2*n, n:2*n]
    # fmt: on

    h_re = 0.5 * (s11 + s22)
    h_im = 0.5 * (s21 - s12)
    print("Re diff", s11 - s22)
    print("Im diff", s12 - s12.T)
    return h_re + 1j * h_im


def solution_real_to_complex(
    solution: Solution_SDP[np.float64],
) -> Solution_SDP[np.complex64]:
    return Solution_SDP(
        primal_objective_value=solution.primal_objective_value,
        dual_objective_value=solution.dual_objective_value,
        dual_eqC_variables=solution.dual_eqC_variables,
        dual_ineqC_variables=solution.dual_ineqC_variables,
        dual_PSD_variables=[
            matrix_real_to_complex(Z) for Z in solution.dual_PSD_variables
        ],
        primal_PSD_variables=[
            matrix_real_to_complex(Z) for Z in solution.primal_PSD_variables
        ],
    )
