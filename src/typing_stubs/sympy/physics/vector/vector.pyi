from _typeshed import Incomplete
from sympy.core.evalf import EvalfMixin
from sympy.printing.defaults import Printable

__all__ = ['Vector']

class Vector(Printable, EvalfMixin):
    simp: bool
    is_number: bool
    args: Incomplete
    def __init__(self, inlist) -> None: ...
    @property
    def func(self): ...
    def __hash__(self): ...
    def __add__(self, other): ...
    def dot(self, other): ...
    def __truediv__(self, other): ...
    def __eq__(self, other): ...
    def __mul__(self, other): ...
    def __neg__(self): ...
    def outer(self, other): ...
    def __rsub__(self, other): ...
    def __sub__(self, other): ...
    def cross(self, other): ...
    __radd__ = __add__
    __rmul__ = __mul__
    def separate(self): ...
    def __and__(self, other): ...
    __rand__ = __and__
    def __xor__(self, other): ...
    def __or__(self, other): ...
    def diff(self, var, frame, var_in_dcm: bool = True): ...
    def express(self, otherframe, variables: bool = False): ...
    def to_matrix(self, reference_frame): ...
    def doit(self, **hints): ...
    def dt(self, otherframe): ...
    def simplify(self): ...
    def subs(self, *args, **kwargs): ...
    def magnitude(self): ...
    def normalize(self): ...
    def applyfunc(self, f): ...
    def angle_between(self, vec): ...
    def free_symbols(self, reference_frame): ...
    def free_dynamicsymbols(self, reference_frame): ...
    def xreplace(self, rule): ...

class VectorTypeError(TypeError):
    def __init__(self, other, want) -> None: ...
