from sympy.core.add import Add as Add
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.functions.elementary.exponential import exp as exp
from sympy.simplify.simplify import simplify as simplify
from sympy.stats.rv import is_random as is_random
from sympy.stats.symbolic_probability import Covariance as Covariance, RandomSymbol as RandomSymbol, Variance as Variance

def variance_prop(expr, consts=(), include_covar: bool = False): ...
