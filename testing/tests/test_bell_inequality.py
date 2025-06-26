from ncpol3sdpa.bell_inequality import Bell_inequality


def test_bell_inequality_1() -> None:
    assert abs(Bell_inequality.solve_bell_inequality() - 2.828) <= 0.01
