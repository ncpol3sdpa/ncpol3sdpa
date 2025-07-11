from _typeshed import Incomplete
from sympy.codegen.ast import Assignment as Assignment, FloatBaseType as FloatBaseType, FunctionDefinition as FunctionDefinition, IntBaseType as IntBaseType, Return as Return, String as String, Variable as Variable
from sympy.core import Add as Add, Float as Float, Integer as Integer, Mul as Mul
from sympy.core.symbol import Symbol as Symbol
from sympy.external import import_module as import_module

lfortran: Incomplete
asr_mod: Incomplete
asr: Incomplete
src_to_ast: Incomplete
ast_to_asr: Incomplete

class ASR2PyVisitor(asr.ASTVisitor):
    def __init__(self) -> None: ...
    def visit_TranslationUnit(self, node) -> None: ...
    def visit_Assignment(self, node) -> None: ...
    def visit_BinOp(self, node) -> None: ...
    def visit_Variable(self, node) -> None: ...
    def visit_Sequence(self, seq) -> None: ...
    def visit_Num(self, node) -> None: ...
    def visit_Function(self, node) -> None: ...
    def ret_ast(self): ...

class ASR2PyVisitor:
    def __init__(self, *args, **kwargs) -> None: ...

def call_visitor(fort_node): ...
def src_to_sympy(src): ...
