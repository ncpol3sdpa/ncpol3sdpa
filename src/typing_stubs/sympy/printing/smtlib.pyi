from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q
from sympy.assumptions.assume import AppliedPredicate as AppliedPredicate
from sympy.assumptions.relation.binrel import AppliedBinaryRelation as AppliedBinaryRelation
from sympy.assumptions.relation.equality import EqualityPredicate as EqualityPredicate, GreaterThanPredicate as GreaterThanPredicate, LessThanPredicate as LessThanPredicate, StrictGreaterThanPredicate as StrictGreaterThanPredicate, StrictLessThanPredicate as StrictLessThanPredicate
from sympy.core import Add as Add, Basic as Basic, Expr as Expr, Float as Float, Integer as Integer, Mul as Mul, Rational as Rational, Symbol as Symbol
from sympy.core.function import Function as Function, UndefinedFunction as UndefinedFunction
from sympy.core.relational import Equality as Equality, GreaterThan as GreaterThan, LessThan as LessThan, Relational as Relational, StrictGreaterThan as StrictGreaterThan, StrictLessThan as StrictLessThan, Unequality as Unequality
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.functions.elementary.exponential import Pow as Pow, exp as exp, log as log
from sympy.functions.elementary.hyperbolic import cosh as cosh, sinh as sinh, tanh as tanh
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import acos as acos, asin as asin, atan as atan, atan2 as atan2, cos as cos, sin as sin, tan as tan
from sympy.logic.boolalg import And as And, Boolean as Boolean, BooleanFalse as BooleanFalse, BooleanFunction as BooleanFunction, BooleanTrue as BooleanTrue, ITE as ITE, Implies as Implies, Not as Not, Or as Or, Xor as Xor
from sympy.printing.printer import Printer as Printer
from sympy.sets import Interval as Interval

class SMTLibPrinter(Printer):
    printmethod: str
    symbol_table: dict
    def __init__(self, settings: dict | None = None, symbol_table: Incomplete | None = None) -> None: ...
    def emptyPrinter(self, expr) -> None: ...

def smtlib_code(expr, auto_assert: bool = True, auto_declare: bool = True, precision: Incomplete | None = None, symbol_table: Incomplete | None = None, known_types: Incomplete | None = None, known_constants: Incomplete | None = None, known_functions: Incomplete | None = None, prefix_expressions: Incomplete | None = None, suffix_expressions: Incomplete | None = None, log_warn: Incomplete | None = None): ...
