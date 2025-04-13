from _typeshed import Incomplete
from sympy import default_sort_key as default_sort_key
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import Function as Function
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.sorting import ordered as ordered
from sympy.core.sympify import sympify as sympify
from sympy.matrices.exceptions import NonInvertibleMatrixError as NonInvertibleMatrixError
from sympy.physics.units.dimensions import Dimension as Dimension, DimensionSystem as DimensionSystem
from sympy.physics.units.prefixes import Prefix as Prefix
from sympy.physics.units.quantities import Quantity as Quantity
from sympy.physics.units.unitsystem import UnitSystem as UnitSystem
from sympy.utilities.iterables import sift as sift

def convert_to(expr, target_units, unit_system: str = 'SI'): ...
def quantity_simplify(expr, across_dimensions: bool = False, unit_system: Incomplete | None = None): ...
def check_dimensions(expr, unit_system: str = 'SI'): ...
