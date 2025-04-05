from _typeshed import Incomplete
from sympy.core import Dummy as Dummy, Symbol as Symbol, Tuple as Tuple
from sympy.core.basic import Basic as Basic
from sympy.core.expr import Atom as Atom, Expr as Expr
from sympy.core.numbers import Float as Float, Integer as Integer, oo as oo
from sympy.core.relational import Ge as Ge, Gt as Gt, Le as Le, Lt as Lt
from sympy.core.sympify import SympifyError as SympifyError, sympify as sympify
from sympy.utilities.iterables import filter_symbols as filter_symbols, iterable as iterable, numbered_symbols as numbered_symbols, topological_sort as topological_sort
from typing import Any

class CodegenAST(Basic): ...

class Token(CodegenAST):
    defaults: dict[str, Any]
    not_in_args: list[str]
    indented_args: Incomplete
    @property
    def is_Atom(self): ...
    def __new__(cls, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def kwargs(self, exclude=(), apply: Incomplete | None = None): ...

class BreakToken(Token): ...

break_: Incomplete

class ContinueToken(Token): ...

continue_: Incomplete

class NoneToken(Token):
    def __eq__(self, other): ...
    def __hash__(self): ...

none: Incomplete

class AssignmentBase(CodegenAST):
    def __new__(cls, lhs, rhs): ...
    @property
    def lhs(self): ...
    @property
    def rhs(self): ...

class Assignment(AssignmentBase):
    op: str

class AugmentedAssignment(AssignmentBase):
    binop: str
    @property
    def op(self): ...

class AddAugmentedAssignment(AugmentedAssignment):
    binop: str

class SubAugmentedAssignment(AugmentedAssignment):
    binop: str

class MulAugmentedAssignment(AugmentedAssignment):
    binop: str

class DivAugmentedAssignment(AugmentedAssignment):
    binop: str

class ModAugmentedAssignment(AugmentedAssignment):
    binop: str

augassign_classes: Incomplete

def aug_assign(lhs, op, rhs): ...

class CodeBlock(CodegenAST):
    def __new__(cls, *args): ...
    def __iter__(self): ...
    @property
    def free_symbols(self): ...
    @classmethod
    def topological_sort(cls, assignments): ...
    def cse(self, symbols: Incomplete | None = None, optimizations: Incomplete | None = None, postprocess: Incomplete | None = None, order: str = 'canonical'): ...

class For(Token): ...

class String(Atom, Token):
    not_in_args: Incomplete
    is_Atom: bool
    def kwargs(self, exclude=(), apply: Incomplete | None = None): ...
    @property
    def func(self): ...

class QuotedString(String): ...
class Comment(String): ...

class Node(Token):
    defaults: dict[str, Any]
    def attr_params(self, looking_for): ...

class Type(Token):
    @classmethod
    def from_expr(cls, expr): ...
    def cast_check(self, value, rtol: Incomplete | None = None, atol: int = 0, precision_targets: Incomplete | None = None): ...

class IntBaseType(Type):
    cast_nocheck: Incomplete

class _SizedIntType(IntBaseType): ...

class SignedIntType(_SizedIntType):
    @property
    def min(self): ...
    @property
    def max(self): ...

class UnsignedIntType(_SizedIntType):
    @property
    def min(self): ...
    @property
    def max(self): ...

two: Incomplete

class FloatBaseType(Type):
    cast_nocheck = Float

class FloatType(FloatBaseType):
    @property
    def max_exponent(self): ...
    @property
    def min_exponent(self): ...
    @property
    def max(self): ...
    @property
    def tiny(self): ...
    @property
    def eps(self): ...
    @property
    def dig(self): ...
    @property
    def decimal_dig(self): ...
    def cast_nocheck(self, value): ...

class ComplexBaseType(FloatBaseType):
    def cast_nocheck(self, value): ...

class ComplexType(ComplexBaseType, FloatType): ...

intc: Incomplete
intp: Incomplete
int8: Incomplete
int16: Incomplete
int32: Incomplete
int64: Incomplete
uint8: Incomplete
uint16: Incomplete
uint32: Incomplete
uint64: Incomplete
float16: Incomplete
float32: Incomplete
float64: Incomplete
float80: Incomplete
float128: Incomplete
float256: Incomplete
complex64: Incomplete
complex128: Incomplete
untyped: Incomplete
real: Incomplete
integer: Incomplete
complex_: Incomplete
bool_: Incomplete

class Attribute(Token):
    defaults: Incomplete

value_const: Incomplete
pointer_const: Incomplete

class Variable(Node):
    defaults: Incomplete
    @classmethod
    def deduced(cls, symbol, value: Incomplete | None = None, attrs=..., cast_check: bool = True): ...
    def as_Declaration(self, **kwargs): ...
    __lt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    __gt__: Incomplete

class Pointer(Variable):
    def __getitem__(self, key): ...

class Element(Token):
    defaults: Incomplete

class Declaration(Token): ...
class While(Token): ...
class Scope(Token): ...
class Stream(Token): ...

stdout: Incomplete
stderr: Incomplete

class Print(Token):
    defaults: Incomplete

class FunctionPrototype(Node):
    @classmethod
    def from_FunctionDefinition(cls, func_def): ...

class FunctionDefinition(FunctionPrototype):
    @classmethod
    def from_FunctionPrototype(cls, func_proto, body): ...

class Return(Token): ...
class FunctionCall(Token, Expr): ...
class Raise(Token): ...
class RuntimeError_(Token): ...
