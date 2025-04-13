from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.stats.crv_types import BetaDistribution as BetaDistribution, ChiSquaredDistribution as ChiSquaredDistribution, ExponentialDistribution as ExponentialDistribution, FDistributionDistribution as FDistributionDistribution, GammaDistribution as GammaDistribution, GumbelDistribution as GumbelDistribution, LaplaceDistribution as LaplaceDistribution, LogNormalDistribution as LogNormalDistribution, LogisticDistribution as LogisticDistribution, NormalDistribution as NormalDistribution, ParetoDistribution as ParetoDistribution, RayleighDistribution as RayleighDistribution, TriangularDistribution as TriangularDistribution, UniformDistribution as UniformDistribution
from sympy.stats.drv_types import GeometricDistribution as GeometricDistribution, PoissonDistribution as PoissonDistribution, ZetaDistribution as ZetaDistribution
from sympy.stats.frv_types import BinomialDistribution as BinomialDistribution, HypergeometricDistribution as HypergeometricDistribution

numpy: Incomplete

def do_sample_numpy(dist, size, rand_state) -> None: ...
def _(dist: BetaDistribution, size, rand_state): ...
