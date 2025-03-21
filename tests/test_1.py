from ncpol3sdpa.constraints import Constraint


def test_1() -> None:
    assert True


def test_2() -> None:
    c = Constraint.EqualityConstraint(None)

    assert c is not None

def f(n : int) -> int:
    return n + 1

