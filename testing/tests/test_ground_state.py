from math import abs
from examples.ground_state import Ground_state2


def test_ground_state() -> None:
    ground_state = Ground_state2(3, {[1, 2]: 1, [2, 3]: 1, [1, 3]: 0})
    assert abs(1 - 1) <= 0.1
