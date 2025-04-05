from _typeshed import Incomplete
from sympy.core import Function as Function, NumberKind as NumberKind, S as S, sympify as sympify
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import Application as Application, ArgumentIndexError as ArgumentIndexError, Lambda as Lambda
from sympy.core.logic import fuzzy_and as fuzzy_and, fuzzy_or as fuzzy_or
from sympy.core.mod import Mod as Mod
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.operations import LatticeOp as LatticeOp, ShortCircuit as ShortCircuit
from sympy.core.power import Pow as Pow
from sympy.core.relational import Eq as Eq, Relational as Relational
from sympy.core.rules import Transform as Transform
from sympy.core.singleton import Singleton as Singleton
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy
from sympy.core.traversal import walk as walk
from sympy.logic.boolalg import And as And, Or as Or
from sympy.utilities.iterables import sift as sift

class IdentityFunction(Lambda, metaclass=Singleton):
    @property
    def signature(self): ...
    @property
    def expr(self): ...

Id: Incomplete

def sqrt(arg, evaluate: Incomplete | None = None): ...
def cbrt(arg, evaluate: Incomplete | None = None): ...
def root(arg, n, k: int = 0, evaluate: Incomplete | None = None): ...
def real_root(arg, n: Incomplete | None = None, evaluate: Incomplete | None = None): ...

class MinMaxBase(Expr, LatticeOp):
    def __new__(cls, *args, **assumptions): ...
    def evalf(self, n: int = 15, **options): ...
    def n(self, *args, **kwargs): ...

class Max(MinMaxBase, Application):
    zero: Incomplete
    identity: Incomplete
    def fdiff(self, argindex): ...

class Min(MinMaxBase, Application):
    zero: Incomplete
    identity: Incomplete
    def fdiff(self, argindex): ...

class Rem(Function):
    kind = NumberKind
    @classmethod
    def eval(cls, p, q): ...
