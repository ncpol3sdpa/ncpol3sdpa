from ncpol3sdpa.ground_state import ground_state_v2


def test_ground_state_1() -> None:
    """test corresponds to a situation wwhere there are 3 qubits and 2 edges between 2 of the 3 qubits
    In this situation the minimun of the energy of the system is -3"""
    ground_state = ground_state_v2.Ground_state2(
        3, {(1, 2): 1, (2, 3): 1, (1, 3): 0, (2, 1): 1, (3, 1): 0, (3, 2): 1}
    )
    assert abs(ground_state.solve_ground_state() + 3) <= 0.01


def test_ground_state_2() -> None:
    """test corresponds to a situation wwhere there are 4 qubits and 3 edges between 3 of the 4 qubits
    In this situation the minimun of the energy of the system is -6"""
    ground_state = ground_state_v2.Ground_state2(
        4,
        {
            (1, 2): 0,
            (2, 1): 0,
            (1, 3): 1,
            (3, 1): 1,
            (1, 4): 0,
            (4, 1): 0,
            (2, 3): 1,
            (3, 2): 1,
            (2, 4): 0,
            (4, 2): 0,
            (3, 4): 1,
            (4, 3): 1,
        },
    )
    assert abs(ground_state.solve_ground_state() + 6) <= 0.01


def test_ground_state_3() -> None:
    """test corresponds to a situation wwhere there are 4 qubits and 3 edges between 3 of the 4 qubits
    In this situation the minimun of the energy of the system is -6"""
    ground_state = ground_state_v2.Ground_state2(
        4,
        {
            (1, 2): 1,
            (2, 1): 1,
            (1, 3): 1,
            (3, 1): 1,
            (1, 4): 0,
            (4, 1): 0,
            (2, 3): 1,
            (3, 2): 1,
            (2, 4): 0,
            (4, 2): 0,
            (3, 4): 1,
            (4, 3): 1,
        },
    )
    assert abs(ground_state.solve_ground_state() + 9) <= 0.01
