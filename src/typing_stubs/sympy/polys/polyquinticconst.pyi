from _typeshed import Incomplete

__all__ = ['PolyQuintic']

class PolyQuintic:
    zeta1: Incomplete
    zeta2: Incomplete
    zeta3: Incomplete
    zeta4: Incomplete
    def __init__(self, poly) -> None: ...
    @property
    def f20(self): ...
    @property
    def b(self): ...
    @property
    def o(self): ...
    @property
    def a(self): ...
    @property
    def c(self): ...
    @property
    def F(self): ...
    def l0(self, theta): ...
    def T(self, theta, d): ...
    def order(self, theta, d): ...
    def uv(self, theta, d): ...
    @property
    def zeta(self): ...
