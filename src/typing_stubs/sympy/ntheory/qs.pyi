from _typeshed import Incomplete
from sympy.external.gmpy import gcd as gcd, invert as invert
from sympy.ntheory import isprime as isprime

class SievePolynomial:
    modified_coeff: Incomplete
    a: Incomplete
    b: Incomplete
    def __init__(self, modified_coeff=(), a: Incomplete | None = None, b: Incomplete | None = None) -> None: ...
    def eval(self, x): ...

class FactorBaseElem:
    prime: Incomplete
    tmem_p: Incomplete
    log_p: Incomplete
    soln1: Incomplete
    soln2: Incomplete
    a_inv: Incomplete
    b_ainv: Incomplete
    def __init__(self, prime, tmem_p, log_p) -> None: ...

def qs(N, prime_bound, M, ERROR_TERM: int = 25, seed: int = 1234): ...
