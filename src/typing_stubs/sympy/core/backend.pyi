from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, diff as diff, expand as expand
from sympy.core.intfunc import igcd as igcd
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import E as E, I as I, Integer as Integer, Rational as Rational, pi as pi
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol, symbols as symbols, var as var
from sympy.core.sympify import SympifyError as SympifyError, sympify as sympify
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.hyperbolic import acosh as acosh, acoth as acoth, asinh as asinh, atanh as atanh, cosh as cosh, coth as coth, sinh as sinh, tanh as tanh
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan, cos as cos, cot as cot, csc as csc, sec as sec, sin as sin, tan as tan
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.matrices.dense import Matrix as Matrix, diag as diag, eye as eye, ones as ones, symarray as symarray, zeros as zeros
from sympy.matrices.immutable import ImmutableMatrix as ImmutableMatrix
from sympy.matrices.matrixbase import MatrixBase as MatrixBase
from sympy.utilities.lambdify import lambdify as lambdify

__all__ = ['Symbol', 'Integer', 'sympify', 'S', 'SympifyError', 'exp', 'log', 'gamma', 'sqrt', 'I', 'E', 'pi', 'Matrix', 'sin', 'cos', 'tan', 'cot', 'csc', 'sec', 'asin', 'acos', 'atan', 'acot', 'acsc', 'asec', 'sinh', 'cosh', 'tanh', 'coth', 'asinh', 'acosh', 'atanh', 'acoth', 'lambdify', 'symarray', 'diff', 'zeros', 'eye', 'diag', 'ones', 'expand', 'Function', 'symbols', 'var', 'Add', 'Mul', 'Derivative', 'ImmutableMatrix', 'MatrixBase', 'Rational', 'Basic', 'igcd', 'AppliedUndef']

def sympify(a, *, strict: bool = False): ...
