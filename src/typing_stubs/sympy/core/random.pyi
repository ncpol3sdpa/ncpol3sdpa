from _typeshed import Incomplete
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.misc import as_int as as_int

rng: Incomplete
choice: Incomplete
random: Incomplete
randint: Incomplete
randrange: Incomplete
sample: Incomplete
shuffle: Incomplete
uniform: Incomplete

def seed(a: Incomplete | None = None, version: int = 2) -> None: ...
def random_complex_number(a: int = 2, b: int = -1, c: int = 3, d: int = 1, rational: bool = False, tolerance: Incomplete | None = None): ...
def verify_numerically(f, g, z: Incomplete | None = None, tol: float = 1e-06, a: int = 2, b: int = -1, c: int = 3, d: int = 1): ...
def test_derivative_numerically(f, z, tol: float = 1e-06, a: int = 2, b: int = -1, c: int = 3, d: int = 1): ...
