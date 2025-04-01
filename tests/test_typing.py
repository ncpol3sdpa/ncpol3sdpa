from sympy import Symbol, poly, Poly
# from typing import List
# from typeguard import typechecked
# check_type


def salutation(prenom: str) -> str:
    return "salut" + prenom


# def test_poly(polynomial : Poly) -> None:
#    print(f"test_poly {type(polynomial)}  ({isinstance(polynomial,Poly)})")


def type_test() -> None:
    x = Symbol("x")
    print(f"{isinstance(x, Symbol)}")
    # print(f"{isinstance([x,x],List[Symbol])}")
    # check_type('variablename', [x,x],List[Symbol])


# @typechecked
def int_fun(x: int) -> None:
    print(f"int_fun : {isinstance(x,int)=}")


# @typechecked
def poly_fun(x: Poly) -> None:
    print(f"int_fun : {isinstance(x,Poly)=}")


if __name__ == "__main__":
    # salutation("Pedro")

    # s = Symbol("s")
    # p = poly(s**2 + 2*s + 1)
    # test_poly(p)
    # test_poly(s)

    # type_test()

    # int_fun(1)
    # int_fun(1.5)

    y = Symbol("y")
    poly_fun(poly(y**2 + 2 * y + 1))
    poly_fun(Symbol("x"))
