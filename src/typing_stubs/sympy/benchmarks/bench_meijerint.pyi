from _typeshed import Incomplete
from sympy.abc import x as x, y as y
from sympy.core.cache import clear_cache as clear_cache
from sympy.core.numbers import oo as oo, pi as pi
from sympy.core.symbol import Symbol as Symbol, symbols as symbols
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.special.bessel import besseli as besseli
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.integrals.integrals import integrate as integrate
from sympy.integrals.transforms import fourier_transform as fourier_transform, inverse_fourier_transform as inverse_fourier_transform, inverse_laplace_transform as inverse_laplace_transform, inverse_mellin_transform as inverse_mellin_transform, laplace_transform as laplace_transform, mellin_transform as mellin_transform

LT = laplace_transform
FT = fourier_transform
MT = mellin_transform
IFT = inverse_fourier_transform
ILT = inverse_laplace_transform
IMT = inverse_mellin_transform
nu: Incomplete
beta: Incomplete
rho: Incomplete
apos: Incomplete
bpos: Incomplete
cpos: Incomplete
dpos: Incomplete
posk: Incomplete
p: Incomplete
k: Incomplete
negk: Incomplete
mu1: Incomplete
mu2: Incomplete
sigma1: Incomplete
sigma2: Incomplete
rate: Incomplete

def normal(x, mu, sigma): ...
def exponential(x, rate): ...

alpha: Incomplete
betadist: Incomplete
kint: Incomplete
chi: Incomplete
chisquared: Incomplete
dagum: Incomplete
d1: Incomplete
d2: Incomplete
f: Incomplete
nupos: Incomplete
sigmapos: Incomplete
rice: Incomplete
mu: Incomplete
laplace: Incomplete
u: Incomplete
tpos: Incomplete

def E(expr) -> None: ...

bench: Incomplete
timings: Incomplete
