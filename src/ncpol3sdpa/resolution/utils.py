from __future__ import annotations
from typing import List, Type, Any, TypeVar

from sympy import Expr, S, adjoint
import sympy as sp


type Matrix = List[List[sp.Expr]]


def degree_of_polynomial(polynomial: Expr) -> int:
    polynomial = polynomial.expand()
    terms = polynomial.as_ordered_terms()
    res = 0
    for term in terms:
        factors = term.as_ordered_factors()
        deg = 0
        for factor in factors:
            if not factor.is_number:
                _, exp = factor.as_base_exp()
                deg += exp
        res = max(deg, res)
    return res


def generate_needed_symbols(polynomials: List[sp.Expr]) -> List[sp.Expr]:
    total: sp.Expr = sp.S.One
    for p in polynomials:
        total += p

    return list(total.free_symbols)  # type: ignore


T = TypeVar("T")


class NoPublicConstructor(type):
    """Metaclass that ensures a private constructor

    If a class uses this metaclass like this:

        class SomeClass(metaclass=NoPublicConstructor):
            pass

    If you try to instantiate your class (`SomeClass()`),
    a `TypeError` will be thrown.
    """

    def __call__(cls, *args: Any, **kwargs: Any) -> None:
        raise TypeError(
            f"{cls.__module__}.{cls.__qualname__} has no public constructor"
        )

    def _create(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        return super().__call__(*args, **kwargs)  # type: ignore


def tensor_product_lower_triangle(A: Matrix, B: Matrix) -> Matrix:
    """
    Computes the tensor (Kronecker) product of two Hermitian matrices, each stored using only
    their lower triangular parts.

    The function returns the lower triangular part of the resulting matrix from the tensor product.

    Parameters:
    - A (Matrix): A Hermitian matrix of size n×n, represented as a list of lists where
                  only the lower triangular part (i >= j) is stored explicitly.
    - B (Matrix): A Hermitian matrix of size m×m, represented similarly.

    Returns:
    - Matrix: A list of lists representing the lower triangular part of the Hermitian matrix
              resulting from the tensor product A ⊗ B, of size (n*m)×(n*m).

    Notes:
    - The output matrix C is stored such that C[I1][J] represents the entry at row I1 and column J,
      with only entries for which I1 >= J being populated.

    Example:
    >>> from sympy import Matrix, I, conjugate
    >>> A = [
    ...     [1],
    ...     [2 + 3*I, 4]
    ... ]
    >>> B = [
    ...     [5],
    ...     [6 - I, 7]
    ... ]
    >>> C = tensor_product_lower_triangle(A, B)
    >>> for row in C:
    ...     print(row)
    [5]
    [30 - 5*I, 28]
    [(10 + 15*I), (20 + 30*I), 20]
    [(24 + 42*I - 3), (48 + 6*I), (56 + 21*I), 16]

    Here, A and B are 2x2 Hermitian matrices stored by their lower triangular parts,
    and the result is a 4x4 Hermitian matrix stored similarly.
    """
    n = len(A)
    m = len(B)
    size = n * m

    C = [[S.Zero] * (I1 + 1) for I1 in range(size)]

    def get_hermitian(M: Matrix, i: int, j: int) -> Expr:
        return M[i][j] if i >= j else adjoint(M[j][i])  # type: ignore

    for i in range(n):
        for j in range(n):
            a_ij = get_hermitian(A, i, j)
            for k in range(m):
                for l1 in range(m):
                    b_kl = get_hermitian(B, k, l1)

                    I1 = i * m + k
                    J = j * m + l1

                    if I1 >= J:
                        C[I1][J] += a_ij * b_kl

    return C
