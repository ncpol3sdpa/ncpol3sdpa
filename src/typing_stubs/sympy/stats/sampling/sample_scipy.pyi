from _typeshed import Incomplete
from sympy.core.symbol import Dummy as Dummy
from sympy.external import import_module as import_module
from sympy.functions.elementary.exponential import exp as exp
from sympy.stats import DiscreteDistributionHandmade as DiscreteDistributionHandmade
from sympy.stats.crv import SingleContinuousDistribution as SingleContinuousDistribution
from sympy.stats.crv_types import BetaDistribution as BetaDistribution, CauchyDistribution as CauchyDistribution, ChiSquaredDistribution as ChiSquaredDistribution, ExponentialDistribution as ExponentialDistribution, GammaDistribution as GammaDistribution, LogNormalDistribution as LogNormalDistribution, NormalDistribution as NormalDistribution, ParetoDistribution as ParetoDistribution, StudentTDistribution as StudentTDistribution, UniformDistribution as UniformDistribution
from sympy.stats.drv_types import GeometricDistribution as GeometricDistribution, LogarithmicDistribution as LogarithmicDistribution, NegativeBinomialDistribution as NegativeBinomialDistribution, PoissonDistribution as PoissonDistribution, SkellamDistribution as SkellamDistribution, YuleSimonDistribution as YuleSimonDistribution, ZetaDistribution as ZetaDistribution
from sympy.stats.frv import SingleFiniteDistribution as SingleFiniteDistribution
from sympy.utilities.lambdify import lambdify as lambdify

scipy: Incomplete

def do_sample_scipy(dist, size, seed) -> None: ...
def _(dist: SingleContinuousDistribution, size, seed): ...
