from _typeshed import Incomplete
from sympy.core import sympify as sympify
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.relational import Eq as Eq, Ge as Ge, Le as Le
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy
from sympy.functions.elementary.complexes import sign as sign
from sympy.matrices.dense import Matrix as Matrix, zeros as zeros
from sympy.solvers.solveset import linear_eq_to_matrix as linear_eq_to_matrix
from sympy.utilities.iterables import numbered_symbols as numbered_symbols
from sympy.utilities.misc import filldedent as filldedent

class UnboundedLPError(Exception): ...
class InfeasibleLPError(Exception): ...

def lpmin(f, constr): ...
def lpmax(f, constr): ...
def linprog(c, A: Incomplete | None = None, b: Incomplete | None = None, A_eq: Incomplete | None = None, b_eq: Incomplete | None = None, bounds: Incomplete | None = None): ...
def show_linprog(c, A: Incomplete | None = None, b: Incomplete | None = None, A_eq: Incomplete | None = None, b_eq: Incomplete | None = None, bounds: Incomplete | None = None): ...
