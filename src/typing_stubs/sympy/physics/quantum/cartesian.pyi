from _typeshed import Incomplete
from sympy.physics.quantum.operator import HermitianOperator
from sympy.physics.quantum.state import Bra, Ket, State

__all__ = ['XOp', 'YOp', 'ZOp', 'PxOp', 'X', 'Y', 'Z', 'Px', 'XKet', 'XBra', 'PxKet', 'PxBra', 'PositionState3D', 'PositionKet3D', 'PositionBra3D']

class XOp(HermitianOperator):
    @classmethod
    def default_args(self): ...

class YOp(HermitianOperator):
    @classmethod
    def default_args(self): ...

class ZOp(HermitianOperator):
    @classmethod
    def default_args(self): ...

class PxOp(HermitianOperator):
    @classmethod
    def default_args(self): ...

X: Incomplete
Y: Incomplete
Z: Incomplete
Px: Incomplete

class XKet(Ket):
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def position(self): ...

class XBra(Bra):
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def position(self): ...

class PositionState3D(State):
    @classmethod
    def default_args(self): ...
    @property
    def position_x(self): ...
    @property
    def position_y(self): ...
    @property
    def position_z(self): ...

class PositionKet3D(Ket, PositionState3D):
    @classmethod
    def dual_class(self): ...

class PositionBra3D(Bra, PositionState3D):
    @classmethod
    def dual_class(self): ...

class PxKet(Ket):
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def momentum(self): ...

class PxBra(Bra):
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def momentum(self): ...
