from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import AppliedUndef as AppliedUndef
from sympy.core.relational import Relational as Relational
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.logic.boolalg import BooleanFunction as BooleanFunction
from sympy.sets.fancysets import ImageSet as ImageSet
from sympy.sets.sets import FiniteSet as FiniteSet
from sympy.tensor.indexed import Indexed as Indexed

def extract_solution(set_sol, n: int = 10): ...
