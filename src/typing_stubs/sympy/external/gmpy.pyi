from .ntheory import bit_scan0 as python_bit_scan0, bit_scan1 as python_bit_scan1, factorial as python_factorial, gcd as python_gcd, gcdext as python_gcdext, invert as python_invert, iroot as python_iroot, is_bpsw_prp as python_is_bpsw_prp, is_euler_prp as python_is_euler_prp, is_fermat_prp as python_is_fermat_prp, is_fibonacci_prp as python_is_fibonacci_prp, is_lucas_prp as python_is_lucas_prp, is_selfridge_prp as python_is_selfridge_prp, is_square as python_is_square, is_strong_bpsw_prp as python_is_strong_bpsw_prp, is_strong_lucas_prp as python_is_strong_lucas_prp, is_strong_prp as python_is_strong_prp, is_strong_selfridge_prp as python_is_strong_selfridge_prp, jacobi as python_jacobi, kronecker as python_kronecker, lcm as python_lcm, legendre as python_legendre, remove as python_remove, sqrt as python_sqrt, sqrtrem as python_sqrtrem
from .pythonmpq import PythonMPQ
from _typeshed import Incomplete

__all__ = ['GROUND_TYPES', 'HAS_GMPY', 'SYMPY_INTS', 'MPQ', 'MPZ', 'bit_scan1', 'bit_scan0', 'remove', 'factorial', 'sqrt', 'is_square', 'sqrtrem', 'gcd', 'lcm', 'gcdext', 'invert', 'legendre', 'jacobi', 'kronecker', 'iroot', 'is_fermat_prp', 'is_euler_prp', 'is_strong_prp', 'is_fibonacci_prp', 'is_lucas_prp', 'is_selfridge_prp', 'is_strong_lucas_prp', 'is_strong_selfridge_prp', 'is_bpsw_prp', 'is_strong_bpsw_prp']

SYMPY_INTS: tuple[type, ...]
HAS_GMPY: int
GROUND_TYPES: str
MPZ: Incomplete
MPQ: Incomplete
bit_scan1: Incomplete
bit_scan0: Incomplete
remove: Incomplete
factorial: Incomplete
sqrt: Incomplete
is_square: Incomplete
sqrtrem: Incomplete
gcd: Incomplete
lcm: Incomplete
gcdext: Incomplete
invert: Incomplete
legendre: Incomplete
jacobi: Incomplete
kronecker: Incomplete

def iroot(x, n): ...

is_fermat_prp: Incomplete
is_euler_prp: Incomplete
is_strong_prp: Incomplete
is_fibonacci_prp: Incomplete
is_lucas_prp: Incomplete
is_selfridge_prp: Incomplete
is_strong_lucas_prp: Incomplete
is_strong_selfridge_prp: Incomplete
is_bpsw_prp: Incomplete
is_strong_bpsw_prp: Incomplete
bit_scan1 = python_bit_scan1
bit_scan0 = python_bit_scan0
remove = python_remove
factorial = python_factorial
gcdext = python_gcdext
invert = python_invert
legendre = python_legendre
kronecker = python_kronecker
is_fermat_prp = python_is_fermat_prp
is_euler_prp = python_is_euler_prp
is_strong_prp = python_is_strong_prp
is_fibonacci_prp = python_is_fibonacci_prp
is_lucas_prp = python_is_lucas_prp
is_selfridge_prp = python_is_selfridge_prp
is_strong_lucas_prp = python_is_strong_lucas_prp
is_strong_selfridge_prp = python_is_strong_selfridge_prp
is_bpsw_prp = python_is_bpsw_prp
is_strong_bpsw_prp = python_is_strong_bpsw_prp
MPZ = int
MPQ = PythonMPQ
bit_scan1 = python_bit_scan1
bit_scan0 = python_bit_scan0
remove = python_remove
factorial = python_factorial
sqrt = python_sqrt
is_square = python_is_square
sqrtrem = python_sqrtrem
gcd = python_gcd
lcm = python_lcm
gcdext = python_gcdext
invert = python_invert
legendre = python_legendre
jacobi = python_jacobi
kronecker = python_kronecker
iroot = python_iroot
is_fermat_prp = python_is_fermat_prp
is_euler_prp = python_is_euler_prp
is_strong_prp = python_is_strong_prp
is_fibonacci_prp = python_is_fibonacci_prp
is_lucas_prp = python_is_lucas_prp
is_selfridge_prp = python_is_selfridge_prp
is_strong_lucas_prp = python_is_strong_lucas_prp
is_strong_selfridge_prp = python_is_strong_selfridge_prp
is_bpsw_prp = python_is_bpsw_prp
is_strong_bpsw_prp = python_is_strong_bpsw_prp
