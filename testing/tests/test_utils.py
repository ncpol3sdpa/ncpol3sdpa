import sympy as sp
from sympy.physics.quantum import Dagger

from ncpol3sdpa.resolution.utils import tensor_product_lower_triangle


def test_tensor_product() -> None:
    a, b, c, d, e, f = sp.symbols("a b c d e f", real=True)
    x1, y1, z1, x2, y2, z2 = sp.symbols("x1 y1 z1 x2 y2 z2", commutative=False)
    a1, b1, c1, d1, e1, f1 = sp.symbols("a1 b1 c1 d1 e1 f1", commutative=False)
    a2, b2, c2, d2, e2, f2 = sp.symbols("a2 b2 c2 d2 e2 f2", commutative=False)
    A = [[a], [b, c]]

    B = [[d], [e, f]]

    C = tensor_product_lower_triangle(A, B)
    assert C == [
        [a * d],
        [a * e, a * f],
        [b * d, b * e, c * d],
        [b * e, b * f, c * e, c * f],
    ]

    X = [[x1], [y1, z1]]
    Y = [[x2], [y2, z2]]
    Z = tensor_product_lower_triangle(X, Y)

    assert Z == [
        [x1 * x2],
        [x1 * y2, x1 * z2],
        [y1 * x2, y1 * y2.adjoint(), z1 * x2],
        [y1 * y2, y1 * z2, z1 * y2, z1 * z2],
    ]

    A1 = [[a1], [b1, c1], [d1, e1, f1]]

    B1 = [[a2], [b2, c2], [d2, e2, f2]]

    C1 = tensor_product_lower_triangle(A1, B1)

    assert C1 == [
        [a1 * a2],
        [a1 * b2, a1 * c2],
        [a1 * d2, a1 * e2, a1 * f2],
        [b1 * a2, b1 * Dagger(b2), b1 * Dagger(d2), c1 * a2],
        [b1 * b2, b1 * c2, b1 * Dagger(e2), c1 * b2, c1 * c2],
        [b1 * d2, b1 * e2, b1 * f2, c1 * d2, c1 * e2, c1 * f2],
        [
            d1 * a2,
            d1 * Dagger(b2),
            d1 * Dagger(d2),
            e1 * a2,
            e1 * Dagger(b2),
            e1 * Dagger(d2),
            f1 * a2,
        ],
        [
            d1 * b2,
            d1 * c2,
            d1 * Dagger(e2),
            e1 * b2,
            e1 * c2,
            e1 * Dagger(e2),
            f1 * b2,
            f1 * c2,
        ],
        [
            d1 * d2,
            d1 * e2,
            d1 * f2,
            e1 * d2,
            e1 * e2,
            e1 * f2,
            f1 * d2,
            f1 * e2,
            f1 * f2,
        ],
    ]


test_tensor_product()
