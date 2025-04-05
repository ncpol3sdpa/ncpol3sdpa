from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import NotIterable as NotIterable, flatten as flatten, is_sequence as is_sequence, iterable as iterable
from sympy.utilities.misc import filldedent as filldedent
from typing import Any

__doctest_requires__: Incomplete
MATH_DEFAULT: dict[str, Any]
MPMATH_DEFAULT: dict[str, Any]
NUMPY_DEFAULT: dict[str, Any]
SCIPY_DEFAULT: dict[str, Any]
CUPY_DEFAULT: dict[str, Any]
JAX_DEFAULT: dict[str, Any]
TENSORFLOW_DEFAULT: dict[str, Any]
SYMPY_DEFAULT: dict[str, Any]
NUMEXPR_DEFAULT: dict[str, Any]
MATH: Incomplete
MPMATH: Incomplete
NUMPY: Incomplete
SCIPY: Incomplete
CUPY: Incomplete
JAX: Incomplete
TENSORFLOW: Incomplete
SYMPY: Incomplete
NUMEXPR: Incomplete
MATH_TRANSLATIONS: Incomplete
MPMATH_TRANSLATIONS: Incomplete
NUMPY_TRANSLATIONS: dict[str, str]
SCIPY_TRANSLATIONS: dict[str, str]
CUPY_TRANSLATIONS: dict[str, str]
JAX_TRANSLATIONS: dict[str, str]
TENSORFLOW_TRANSLATIONS: dict[str, str]
NUMEXPR_TRANSLATIONS: dict[str, str]
MODULES: Incomplete

def lambdify(args, expr, modules: Incomplete | None = None, printer: Incomplete | None = None, use_imps: bool = True, dummify: bool = False, cse: bool = False, docstring_limit: int = 1000): ...
def lambdastr(args, expr, printer: Incomplete | None = None, dummify: Incomplete | None = None): ...

class _EvaluatorPrinter:
    def __init__(self, printer: Incomplete | None = None, dummify: bool = False) -> None: ...
    def doprint(self, funcname, args, expr, *, cses=()): ...

class _TensorflowEvaluatorPrinter(_EvaluatorPrinter): ...

def implemented_function(symfunc, implementation): ...
