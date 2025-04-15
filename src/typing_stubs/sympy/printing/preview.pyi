from .latex import latex as latex
from _typeshed import Incomplete
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.misc import debug as debug

__doctest_requires__: Incomplete

def system_default_viewer(fname, fmt) -> None: ...
def pyglet_viewer(fname, fmt) -> None: ...
def preview(expr, output: str = 'png', viewer: Incomplete | None = None, euler: bool = True, packages=(), filename: Incomplete | None = None, outputbuffer: Incomplete | None = None, preamble: Incomplete | None = None, dvioptions: Incomplete | None = None, outputTexFile: Incomplete | None = None, extra_preamble: Incomplete | None = None, fontsize: Incomplete | None = None, **latex_settings) -> None: ...
