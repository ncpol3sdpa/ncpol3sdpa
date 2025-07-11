from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.stats.joint_rv import ProductPSpace as ProductPSpace
from sympy.stats.rv import Distribution as Distribution, ProductDomain as ProductDomain

class StochasticPSpace(ProductPSpace):
    def __new__(cls, sym, process, distribution: Incomplete | None = None): ...
    @property
    def process(self): ...
    @property
    def domain(self): ...
    @property
    def symbol(self): ...
    @property
    def distribution(self): ...
    def probability(self, condition, given_condition: Incomplete | None = None, evaluate: bool = True, **kwargs): ...
    def compute_expectation(self, expr, condition: Incomplete | None = None, evaluate: bool = True, **kwargs): ...
