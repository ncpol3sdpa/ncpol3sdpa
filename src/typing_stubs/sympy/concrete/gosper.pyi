from sympy.core import Dummy as Dummy, S as S, symbols as symbols
from sympy.polys import Poly as Poly, factor as factor, parallel_poly_from_expr as parallel_poly_from_expr
from sympy.utilities.iterables import is_sequence as is_sequence

def gosper_normal(f, g, n, polys: bool = True): ...
def gosper_term(f, n): ...
def gosper_sum(f, k): ...
