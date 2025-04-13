from sympy.core import Add as Add, Basic as Basic, Dummy as Dummy, Mul as Mul, Pow as Pow, S as S, expand_mul as expand_mul, factor_terms as factor_terms, sympify as sympify
from sympy.core.function import count_ops as count_ops, expand_log as expand_log
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.rules import Transform as Transform
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.functions import exp as exp, exp_polar as exp_polar, log as log, polarify as polarify, root as root, unpolarify as unpolarify
from sympy.matrices.expressions.matexpr import MatrixSymbol as MatrixSymbol
from sympy.ntheory.factor_ import multiplicity as multiplicity
from sympy.polys import gcd as gcd, lcm as lcm

def powsimp(expr, deep: bool = False, combine: str = 'all', force: bool = False, measure=...): ...
def powdenest(eq, force: bool = False, polar: bool = False): ...
