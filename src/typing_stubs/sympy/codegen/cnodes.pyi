from _typeshed import Incomplete
from sympy.codegen.ast import Attribute as Attribute, CodeBlock as CodeBlock, Declaration as Declaration, FunctionCall as FunctionCall, Node as Node, String as String, Token as Token, Type as Type, none as none
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.sympify import sympify as sympify

void: Incomplete
restrict: Incomplete
volatile: Incomplete
static: Incomplete

def alignof(arg): ...
def sizeof(arg): ...

class CommaOperator(Basic):
    def __new__(cls, *args): ...

class Label(Node):
    defaults: Incomplete

class goto(Token): ...

class PreDecrement(Basic):
    nargs: int

class PostDecrement(Basic):
    nargs: int

class PreIncrement(Basic):
    nargs: int

class PostIncrement(Basic):
    nargs: int

class struct(Node):
    defaults: Incomplete

class union(struct): ...
