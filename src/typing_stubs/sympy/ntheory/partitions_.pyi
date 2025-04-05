from .residue_ntheory import is_quad_residue as is_quad_residue
from sympy.external.gmpy import gcd as gcd, jacobi as jacobi, legendre as legendre
from sympy.utilities.decorator import deprecated as deprecated
from sympy.utilities.memoization import recurrence_memo as recurrence_memo

def npartitions(n, verbose: bool = False): ...
