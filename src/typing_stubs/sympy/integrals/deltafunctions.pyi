from .integrals import Integral as Integral, integrate as integrate
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions import DiracDelta as DiracDelta, Heaviside as Heaviside

def change_mul(node, x): ...
def deltaintegrate(f, x): ...
