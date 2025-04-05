from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q
from sympy.assumptions.assume import AppliedPredicate as AppliedPredicate
from sympy.assumptions.cnf import EncodedCNF as EncodedCNF
from sympy.assumptions.relation.equality import EqualityPredicate as EqualityPredicate, GreaterThanPredicate as GreaterThanPredicate, LessThanPredicate as LessThanPredicate, StrictGreaterThanPredicate as StrictGreaterThanPredicate, StrictLessThanPredicate as StrictLessThanPredicate
from sympy.core import Add as Add, Mul as Mul
from sympy.core.relational import Equality as Equality, GreaterThan as GreaterThan, LessThan as LessThan, StrictGreaterThan as StrictGreaterThan, StrictLessThan as StrictLessThan
from sympy.external import import_module as import_module
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.functions.elementary.exponential import Pow as Pow
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.logic.boolalg import And as And, ITE as ITE, Implies as Implies, Not as Not, Or as Or, Xor as Xor
from sympy.printing.smtlib import smtlib_code as smtlib_code

def z3_satisfiable(expr, all_models: bool = False): ...
def z3_model_to_sympy_model(z3_model, enc_cnf): ...
def clause_to_assertion(clause): ...
def encoded_cnf_to_z3_solver(enc_cnf, z3): ...

known_functions: Incomplete
