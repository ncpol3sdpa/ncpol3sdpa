from sympy.polys.domains.domain import Domain

__all__ = ['CharacteristicZero']

class CharacteristicZero(Domain):
    has_CharacteristicZero: bool
    def characteristic(self): ...
