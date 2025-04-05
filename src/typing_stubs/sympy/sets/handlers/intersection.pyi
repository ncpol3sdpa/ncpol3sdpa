from _typeshed import Incomplete
from sympy.core.function import Lambda as Lambda, expand_complex as expand_complex
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Float as Float, ilcm as ilcm
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, symbols as symbols
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.multipledispatch import Dispatcher as Dispatcher
from sympy.sets.conditionset import ConditionSet as ConditionSet
from sympy.sets.fancysets import ComplexRegion as ComplexRegion, ImageSet as ImageSet, Integers as Integers, Naturals as Naturals, Range as Range, Rationals as Rationals, Reals as Reals
from sympy.sets.sets import EmptySet as EmptySet, FiniteSet as FiniteSet, Intersection as Intersection, Interval as Interval, ProductSet as ProductSet, Set as Set, Union as Union, UniversalSet as UniversalSet, imageset as imageset
from sympy.simplify.radsimp import numer as numer

intersection_sets: Incomplete

def _(a, b) -> None: ...
