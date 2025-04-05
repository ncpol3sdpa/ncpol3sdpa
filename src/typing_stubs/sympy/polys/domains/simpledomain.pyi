from sympy.polys.domains.domain import Domain

__all__ = ['SimpleDomain']

class SimpleDomain(Domain):
    is_Simple: bool
    def inject(self, *gens): ...
