from _typeshed import Incomplete
from sympy.assumptions.assume import AppliedPredicate as AppliedPredicate, Predicate as Predicate
from sympy.core.relational import Eq as Eq, Ge as Ge, Gt as Gt, Le as Le, Lt as Lt, Ne as Ne
from sympy.core.singleton import S as S
from sympy.logic.boolalg import And as And, Equivalent as Equivalent, ITE as ITE, Implies as Implies, Nand as Nand, Nor as Nor, Not as Not, Or as Or, Xnor as Xnor, Xor as Xor

class Literal:
    def __new__(cls, lit, is_Not: bool = False): ...
    @property
    def arg(self): ...
    def rcall(self, expr): ...
    def __invert__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class OR:
    def __init__(self, *args) -> None: ...
    @property
    def args(self): ...
    def rcall(self, expr): ...
    def __invert__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class AND:
    def __init__(self, *args) -> None: ...
    def __invert__(self): ...
    @property
    def args(self): ...
    def rcall(self, expr): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def to_NNF(expr, composite_map: Incomplete | None = None): ...
def distribute_AND_over_OR(expr): ...

class CNF:
    clauses: Incomplete
    def __init__(self, clauses: Incomplete | None = None) -> None: ...
    def add(self, prop) -> None: ...
    def extend(self, props): ...
    def copy(self): ...
    def add_clauses(self, clauses) -> None: ...
    @classmethod
    def from_prop(cls, prop): ...
    def __iand__(self, other): ...
    def all_predicates(self): ...
    def rcall(self, expr): ...
    @classmethod
    def all_or(cls, *cnfs): ...
    @classmethod
    def all_and(cls, *cnfs): ...
    @classmethod
    def to_CNF(cls, expr): ...
    @classmethod
    def CNF_to_cnf(cls, cnf): ...

class EncodedCNF:
    data: Incomplete
    encoding: Incomplete
    def __init__(self, data: Incomplete | None = None, encoding: Incomplete | None = None) -> None: ...
    def from_cnf(self, cnf) -> None: ...
    @property
    def symbols(self): ...
    @property
    def variables(self): ...
    def copy(self): ...
    def add_prop(self, prop) -> None: ...
    def add_from_cnf(self, cnf) -> None: ...
    def encode_arg(self, arg): ...
    def encode(self, clause): ...
