from _typeshed import Incomplete
from sympy.core import I as I, S as S, pi as pi
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.expr import Expr as Expr
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Lambda as Lambda, Subs as Subs, WildFunction as WildFunction, diff as diff, expand as expand, expand_complex as expand_complex, expand_mul as expand_mul, expand_trig as expand_trig
from sympy.core.mul import Mul as Mul, prod as prod
from sympy.core.relational import Eq as Eq, Ge as Ge, Gt as Gt, Lt as Lt, Ne as Ne, Relational as Relational, Unequality as Unequality
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Wild as Wild, symbols as symbols
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, im as im, periodic_argument as periodic_argument, polar_lift as polar_lift, re as re
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.hyperbolic import asinh as asinh, cosh as cosh, coth as coth, sinh as sinh
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min, sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise, piecewise_exclusive as piecewise_exclusive
from sympy.functions.elementary.trigonometric import atan as atan, cos as cos, sin as sin, sinc as sinc
from sympy.functions.special.bessel import besseli as besseli, besselj as besselj, besselk as besselk, bessely as bessely
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.functions.special.error_functions import Ei as Ei, erf as erf, erfc as erfc
from sympy.functions.special.gamma_functions import digamma as digamma, gamma as gamma, lowergamma as lowergamma, uppergamma as uppergamma
from sympy.functions.special.singularity_functions import SingularityFunction as SingularityFunction
from sympy.integrals import Integral as Integral, integrate as integrate
from sympy.integrals.transforms import IntegralTransform as IntegralTransform, IntegralTransformError as IntegralTransformError
from sympy.logic.boolalg import And as And, Or as Or, conjuncts as conjuncts, disjuncts as disjuncts, to_cnf as to_cnf
from sympy.matrices.matrixbase import MatrixBase as MatrixBase
from sympy.polys.polyerrors import PolynomialError as PolynomialError
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import Poly as Poly
from sympy.polys.rationaltools import together as together
from sympy.polys.rootoftools import RootSum as RootSum
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning, ignore_warnings as ignore_warnings, sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.misc import debugf as debugf

def DEBUG_WRAP(func): ...
def expand_dirac_delta(expr): ...
def laplace_correspondence(f, fdict, /): ...
def laplace_initial_conds(f, t, fdict, /): ...

class LaplaceTransform(IntegralTransform):
    def doit(self, **hints): ...

def laplace_transform(f, t, s, legacy_matrix: bool = True, **hints): ...

class InverseLaplaceTransform(IntegralTransform):
    def __new__(cls, F, s, x, plane, **opts): ...
    @property
    def fundamental_plane(self): ...
    def doit(self, **hints): ...

def inverse_laplace_transform(F, s, t, plane: Incomplete | None = None, **hints): ...
