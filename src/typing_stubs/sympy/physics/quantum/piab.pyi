from sympy.physics.quantum.operator import HermitianOperator
from sympy.physics.quantum.state import Bra, Ket

__all__ = ['PIABHamiltonian', 'PIABKet', 'PIABBra']

class PIABHamiltonian(HermitianOperator): ...

class PIABKet(Ket):
    @classmethod
    def dual_class(self): ...

class PIABBra(Bra):
    @classmethod
    def dual_class(self): ...
