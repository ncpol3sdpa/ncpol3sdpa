from _typeshed import Incomplete
from sympy.core.expr import Expr as Expr
from sympy.core.singleton import S as S
from sympy.core.sympify import sympify as sympify

class Prefix(Expr):
    is_commutative: bool
    def __new__(cls, name, abbrev, exponent, base=..., latex_repr: Incomplete | None = None): ...
    @property
    def name(self): ...
    @property
    def abbrev(self): ...
    @property
    def scale_factor(self): ...
    @property
    def base(self): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...

def prefix_unit(unit, prefixes): ...

yotta: Incomplete
zetta: Incomplete
exa: Incomplete
peta: Incomplete
tera: Incomplete
giga: Incomplete
mega: Incomplete
kilo: Incomplete
hecto: Incomplete
deca: Incomplete
deci: Incomplete
centi: Incomplete
milli: Incomplete
micro: Incomplete
nano: Incomplete
pico: Incomplete
femto: Incomplete
atto: Incomplete
zepto: Incomplete
yocto: Incomplete
PREFIXES: Incomplete
kibi: Incomplete
mebi: Incomplete
gibi: Incomplete
tebi: Incomplete
pebi: Incomplete
exbi: Incomplete
BIN_PREFIXES: Incomplete
