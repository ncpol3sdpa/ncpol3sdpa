from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.parsing.latex.lark.transformer import TransformToSymPyExpr as TransformToSymPyExpr

class LarkLaTeXParser:
    parser: Incomplete
    print_debug_output: Incomplete
    transform_expr: Incomplete
    transformer: Incomplete
    def __init__(self, print_debug_output: bool = False, transform: bool = True, grammar_file: Incomplete | None = None, transformer: Incomplete | None = None) -> None: ...
    def doparse(self, s: str): ...

def parse_latex_lark(s: str): ...
