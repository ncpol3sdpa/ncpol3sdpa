import sympy
from ncpol3sdpa import monomial
from typing import List
from ncpol3sdpa.algebra import degree_of_polynomial


def calculate_number_from_list(digits: List[int], base: int) -> int:
    res = 0
    power = 1
    for digit in digits:
        res += digit * power
        power *= base
    return res


def list_increment_on_test_inputs(nums: List[int], k: int) -> None:
    assert isinstance(k, int)

    for digit in nums:
        assert isinstance(digit, int)
        assert 0 <= digit and digit < k

    nums_cp = nums.copy()
    overflow = monomial.list_increment(nums_cp, k)
    if nums == [k - 1 for _ in nums]:
        assert overflow
    else:
        assert not overflow
        assert calculate_number_from_list(nums, k) + 1 == calculate_number_from_list(
            nums_cp, k
        )


def test_list_increment() -> None:
    list_increment_on_test_inputs([9, 2, 2, 2, 1, 3, 5], 10)
    list_increment_on_test_inputs([2, 2, 2, 2, 2], 10)
    list_increment_on_test_inputs([9, 9, 9, 9], 10)

    # random tests TODO


def test_generate_monomials() -> None:
    x: sympy.Symbol = sympy.symbols("x")
    y: sympy.Symbol = sympy.symbols("y")
    z: sympy.Symbol = sympy.symbols("z")

    assert [1] == monomial.generate_monomials([x], 0)
    assert [1] == monomial.generate_monomials([x, y], 0)
    assert [1] == monomial.generate_monomials([x, y, z], 0)

    assert [1, x, x**2] == monomial.generate_monomials([x], 2)

    xy1 = monomial.generate_monomials([x, y], 1)
    assert len(xy1) == 3
    assert 1 in xy1
    assert x in xy1
    assert y in xy1

    xyz1 = monomial.generate_monomials([x, y, z], 1)
    assert len(xyz1) == 4
    assert 1 in xyz1
    assert x in xyz1
    assert y in xyz1
    assert z in xyz1

    xy2 = monomial.generate_monomials([x, y], 2)
    assert len(xy2) == 6
    assert 1 in xy2
    assert x in xy2
    assert y in xy2
    assert y**2 in xy2
    assert x**2 in xy2
    assert x * y in xy2


def test_generate_monomials_non_commutative() -> None:
    x, y, z = sympy.symbols("x y z", commutative=False)
    assert (monomial.generate_monomials([x, y], 2, False)) == [
        1,
        x,
        y,
        x**2,
        x * y,
        y * x,
        y**2,
    ]
    assert monomial.generate_monomials([x, y, z], 2, False) == [
        1,
        x,
        y,
        z,
        x**2,
        x * y,
        x * z,
        y * x,
        y**2,
        y * z,
        z * x,
        z * y,
        z**2,
    ]
    assert (monomial.generate_monomials([sympy.S.One, x, y], 3, False)) == [
        1,
        x,
        y,
        x**2,
        x * y,
        y * x,
        y**2,
        x**3,
        x**2 * y,
        x * y * x,
        x * y**2,
        y * x**2,
        y * x * y,
        y**2 * x,
        y**3,
    ]

def test_generate_monomials_complex() -> None:
    z = sympy.symbols("z", real=False)
    assert monomial.generate_monomials([z], 1, False, False) == [1, z, z.conjugate()]
    assert set(monomial.generate_monomials([z], 2, False, False)) == set([1, z, z.conjugate(), z**2, z*z.conjugate(), z.conjugate()**2])

def test_degree() -> None:
    x, y = sympy.symbols("x y", commutative=False)
    p1 = x * y + x**2
    p2 = x * y + y**2
    p3 = 10 + 3 * x * y * x * y
    assert degree_of_polynomial(p1) == 2
    assert degree_of_polynomial(p2) == 2
    assert degree_of_polynomial(p3) == 4


if __name__ == "__main__":
    test_list_increment()
    test_generate_monomials()
    test_generate_monomials_non_commutative()
    test_degree()
    print("All tests passed!")
