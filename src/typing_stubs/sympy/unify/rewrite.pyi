from _typeshed import Incomplete
from sympy.assumptions import ask as ask
from sympy.core.expr import Expr as Expr
from sympy.strategies.tools import subs as subs
from sympy.unify.usympy import rebuild as rebuild, unify as unify

def rewriterule(source, target, variables=(), condition: Incomplete | None = None, assume: Incomplete | None = None): ...
