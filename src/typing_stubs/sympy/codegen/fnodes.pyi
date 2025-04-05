from _typeshed import Incomplete
from sympy.codegen.ast import Attribute as Attribute, CodeBlock as CodeBlock, FunctionCall as FunctionCall, Node as Node, String as String, Token as Token, Variable as Variable, none as none
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import Function as Function
from sympy.core.numbers import Float as Float, Integer as Integer
from sympy.core.symbol import Str as Str
from sympy.core.sympify import sympify as sympify
from sympy.logic import false as false, true as true
from sympy.utilities.iterables import iterable as iterable

pure: Incomplete
elemental: Incomplete
intent_in: Incomplete
intent_out: Incomplete
intent_inout: Incomplete
allocatable: Incomplete

class Program(Token): ...
class use_rename(Token): ...

class use(Token):
    defaults: Incomplete

class Module(Token):
    defaults: Incomplete

class Subroutine(Node): ...
class SubroutineCall(Token): ...

class Do(Token):
    defaults: Incomplete

class ArrayConstructor(Token): ...

class ImpliedDoLoop(Token):
    defaults: Incomplete

class Extent(Basic):
    def __new__(cls, *args): ...

assumed_extent: Incomplete

def dimension(*args): ...

assumed_size: Incomplete

def array(symbol, dim, intent: Incomplete | None = None, *, attrs=(), value: Incomplete | None = None, type: Incomplete | None = None): ...
def allocated(array): ...
def lbound(array, dim: Incomplete | None = None, kind: Incomplete | None = None): ...
def ubound(array, dim: Incomplete | None = None, kind: Incomplete | None = None): ...
def shape(source, kind: Incomplete | None = None): ...
def size(array, dim: Incomplete | None = None, kind: Incomplete | None = None): ...
def reshape(source, shape, pad: Incomplete | None = None, order: Incomplete | None = None): ...
def bind_C(name: Incomplete | None = None): ...

class GoTo(Token):
    defaults: Incomplete

class FortranReturn(Token):
    defaults: Incomplete

class FFunction(Function): ...
class F95Function(FFunction): ...

class isign(FFunction):
    nargs: int

class dsign(FFunction):
    nargs: int

class cmplx(FFunction):
    nargs: int

class kind(FFunction):
    nargs: int

class merge(F95Function):
    nargs: int

class _literal(Float): ...
class literal_sp(_literal): ...
class literal_dp(_literal): ...

class sum_(Token, Expr):
    defaults: Incomplete

class product_(Token, Expr):
    defaults: Incomplete
