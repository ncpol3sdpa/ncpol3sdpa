from sympy.external import import_module as import_module
from sympy.stats.crv_types import BetaDistribution as BetaDistribution, CauchyDistribution as CauchyDistribution, ChiSquaredDistribution as ChiSquaredDistribution, ExponentialDistribution as ExponentialDistribution, GammaDistribution as GammaDistribution, GaussianInverseDistribution as GaussianInverseDistribution, LogNormalDistribution as LogNormalDistribution, NormalDistribution as NormalDistribution, ParetoDistribution as ParetoDistribution, UniformDistribution as UniformDistribution
from sympy.stats.drv_types import GeometricDistribution as GeometricDistribution, NegativeBinomialDistribution as NegativeBinomialDistribution, PoissonDistribution as PoissonDistribution
from sympy.stats.frv_types import BernoulliDistribution as BernoulliDistribution, BinomialDistribution as BinomialDistribution

def do_sample_pymc(dist) -> None: ...
def _(dist: BetaDistribution): ...
