from .errors import LaTeXParsingError as LaTeXParsingError
from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.parsing.latex.lark import LarkLaTeXParser as LarkLaTeXParser, TransformToSymPyExpr as TransformToSymPyExpr, parse_latex_lark as parse_latex_lark
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on

__doctest_requires__: Incomplete

def parse_latex(s, strict: bool = False, backend: str = 'antlr'): ...
