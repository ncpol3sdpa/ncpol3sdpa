from sympy.core.basic import Basic as Basic
from sympy.core.logic import fuzzy_and as fuzzy_and, fuzzy_bool as fuzzy_bool
from sympy.core.relational import Eq as Eq, is_eq as is_eq
from sympy.logic.boolalg import And as And
from sympy.multipledispatch import dispatch as dispatch
from sympy.sets.sets import FiniteSet as FiniteSet, Interval as Interval, ProductSet as ProductSet, Set as Set, tfn as tfn
