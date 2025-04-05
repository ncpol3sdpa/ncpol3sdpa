import abc
from .integrals import Integral as Integral
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.containers import Dict as Dict
from sympy.core.expr import Expr as Expr
from sympy.core.function import Derivative as Derivative
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import E as E, Integer as Integer, Number as Number
from sympy.core.power import Pow as Pow
from sympy.core.relational import Boolean as Boolean, Eq as Eq, Ne as Ne
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction, asinh as asinh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction, acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan, cos as cos, cot as cot, csc as csc, sec as sec, sin as sin, tan as tan
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.functions.special.elliptic_integrals import elliptic_e as elliptic_e, elliptic_f as elliptic_f
from sympy.functions.special.error_functions import Chi as Chi, Ci as Ci, Ei as Ei, Shi as Shi, Si as Si, erf as erf, erfi as erfi, fresnelc as fresnelc, fresnels as fresnels, li as li
from sympy.functions.special.gamma_functions import uppergamma as uppergamma
from sympy.functions.special.polynomials import OrthogonalPolynomial as OrthogonalPolynomial, assoc_laguerre as assoc_laguerre, chebyshevt as chebyshevt, chebyshevu as chebyshevu, gegenbauer as gegenbauer, hermite as hermite, jacobi as jacobi, laguerre as laguerre, legendre as legendre
from sympy.functions.special.zeta_functions import polylog as polylog
from sympy.logic.boolalg import And as And
from sympy.ntheory.factor_ import primefactors as primefactors
from sympy.polys.polytools import Poly as Poly, degree as degree, gcd_list as gcd_list, lcm_list as lcm_list
from sympy.simplify.radsimp import fraction as fraction
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers.solvers import solve as solve
from sympy.strategies.core import condition as condition, do_one as do_one, null_safe as null_safe, switch as switch
from sympy.utilities.iterables import iterable as iterable
from sympy.utilities.misc import debug as debug
from typing import NamedTuple, Sequence

@dataclass
class Rule(ABC, metaclass=abc.ABCMeta):
    integrand: Expr
    variable: Symbol
    @abstractmethod
    def eval(self) -> Expr: ...
    @abstractmethod
    def contains_dont_know(self) -> bool: ...

@dataclass
class AtomicRule(Rule, ABC, metaclass=abc.ABCMeta):
    def contains_dont_know(self) -> bool: ...

@dataclass
class ConstantRule(AtomicRule):
    def eval(self) -> Expr: ...

@dataclass
class ConstantTimesRule(Rule):
    constant: Expr
    other: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class PowerRule(AtomicRule):
    base: Expr
    exp: Expr
    def eval(self) -> Expr: ...

@dataclass
class NestedPowRule(AtomicRule):
    base: Expr
    exp: Expr
    def eval(self) -> Expr: ...

@dataclass
class AddRule(Rule):
    substeps: list[Rule]
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class URule(Rule):
    u_var: Symbol
    u_func: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class PartsRule(Rule):
    u: Symbol
    dv: Expr
    v_step: Rule
    second_step: Rule | None
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class CyclicPartsRule(Rule):
    parts_rules: list[PartsRule]
    coefficient: Expr
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class TrigRule(AtomicRule, ABC, metaclass=abc.ABCMeta): ...

@dataclass
class SinRule(TrigRule):
    def eval(self) -> Expr: ...

@dataclass
class CosRule(TrigRule):
    def eval(self) -> Expr: ...

@dataclass
class SecTanRule(TrigRule):
    def eval(self) -> Expr: ...

@dataclass
class CscCotRule(TrigRule):
    def eval(self) -> Expr: ...

@dataclass
class Sec2Rule(TrigRule):
    def eval(self) -> Expr: ...

@dataclass
class Csc2Rule(TrigRule):
    def eval(self) -> Expr: ...

@dataclass
class HyperbolicRule(AtomicRule, ABC, metaclass=abc.ABCMeta): ...

@dataclass
class SinhRule(HyperbolicRule):
    def eval(self) -> Expr: ...

@dataclass
class CoshRule(HyperbolicRule):
    def eval(self): ...

@dataclass
class ExpRule(AtomicRule):
    base: Expr
    exp: Expr
    def eval(self) -> Expr: ...

@dataclass
class ReciprocalRule(AtomicRule):
    base: Expr
    def eval(self) -> Expr: ...

@dataclass
class ArcsinRule(AtomicRule):
    def eval(self) -> Expr: ...

@dataclass
class ArcsinhRule(AtomicRule):
    def eval(self) -> Expr: ...

@dataclass
class ReciprocalSqrtQuadraticRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...

@dataclass
class SqrtQuadraticDenomRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    coeffs: list[Expr]
    def eval(self) -> Expr: ...

@dataclass
class SqrtQuadraticRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...

@dataclass
class AlternativeRule(Rule):
    alternatives: list[Rule]
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class DontKnowRule(Rule):
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class DerivativeRule(AtomicRule):
    def eval(self) -> Expr: ...

@dataclass
class RewriteRule(Rule):
    rewritten: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class CompleteSquareRule(RewriteRule): ...

@dataclass
class PiecewiseRule(Rule):
    subfunctions: Sequence[tuple[Rule, bool | Boolean]]
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class HeavisideRule(Rule):
    harg: Expr
    ibnd: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class DiracDeltaRule(AtomicRule):
    n: Expr
    a: Expr
    b: Expr
    def eval(self) -> Expr: ...

@dataclass
class TrigSubstitutionRule(Rule):
    theta: Expr
    func: Expr
    rewritten: Expr
    substep: Rule
    restriction: bool | Boolean
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...

@dataclass
class ArctanRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...

@dataclass
class OrthogonalPolyRule(AtomicRule, ABC, metaclass=abc.ABCMeta):
    n: Expr

@dataclass
class JacobiRule(OrthogonalPolyRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr: ...

@dataclass
class GegenbauerRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr: ...

@dataclass
class ChebyshevTRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...

@dataclass
class ChebyshevURule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...

@dataclass
class LegendreRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...

@dataclass
class HermiteRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...

@dataclass
class LaguerreRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...

@dataclass
class AssocLaguerreRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr: ...

@dataclass
class IRule(AtomicRule, ABC, metaclass=abc.ABCMeta):
    a: Expr
    b: Expr

@dataclass
class CiRule(IRule):
    def eval(self) -> Expr: ...

@dataclass
class ChiRule(IRule):
    def eval(self) -> Expr: ...

@dataclass
class EiRule(IRule):
    def eval(self) -> Expr: ...

@dataclass
class SiRule(IRule):
    def eval(self) -> Expr: ...

@dataclass
class ShiRule(IRule):
    def eval(self) -> Expr: ...

@dataclass
class LiRule(IRule):
    def eval(self) -> Expr: ...

@dataclass
class ErfRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...

@dataclass
class FresnelCRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...

@dataclass
class FresnelSRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...

@dataclass
class PolylogRule(AtomicRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr: ...

@dataclass
class UpperGammaRule(AtomicRule):
    a: Expr
    e: Expr
    def eval(self) -> Expr: ...

@dataclass
class EllipticFRule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr: ...

@dataclass
class EllipticERule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr: ...

class IntegralInfo(NamedTuple):
    integrand: Expr
    symbol: Symbol

def manual_diff(f, symbol): ...
def manual_subs(expr, *args): ...

inverse_trig_functions: Incomplete

def find_substitutions(integrand, symbol, u_var): ...
def rewriter(condition, rewrite): ...
def proxy_rewriter(condition, rewrite): ...
def multiplexer(conditions): ...
def alternatives(*rules): ...
def constant_rule(integral): ...
def power_rule(integral): ...
def exp_rule(integral): ...
def orthogonal_poly_rule(integral): ...
def special_function_rule(integral): ...
def nested_pow_rule(integral: IntegralInfo): ...
def inverse_trig_rule(integral: IntegralInfo, degenerate: bool = True): ...
def add_rule(integral): ...
def mul_rule(integral: IntegralInfo): ...
def parts_rule(integral): ...
def trig_rule(integral): ...
def trig_product_rule(integral: IntegralInfo): ...
def quadratic_denom_rule(integral): ...
def sqrt_linear_rule(integral: IntegralInfo): ...
def sqrt_quadratic_rule(integral: IntegralInfo, degenerate: bool = True): ...
def hyperbolic_rule(integral: tuple[Expr, Symbol]): ...
def make_wilds(symbol): ...
def sincos_pattern(symbol): ...
def tansec_pattern(symbol): ...
def cotcsc_pattern(symbol): ...
def heaviside_pattern(symbol): ...
def uncurry(func): ...
def trig_rewriter(rewrite): ...

sincos_botheven_condition: Incomplete
sincos_botheven: Incomplete
sincos_sinodd_condition: Incomplete
sincos_sinodd: Incomplete
sincos_cosodd_condition: Incomplete
sincos_cosodd: Incomplete
tansec_seceven_condition: Incomplete
tansec_seceven: Incomplete
tansec_tanodd_condition: Incomplete
tansec_tanodd: Incomplete
tan_tansquared_condition: Incomplete
tan_tansquared: Incomplete
cotcsc_csceven_condition: Incomplete
cotcsc_csceven: Incomplete
cotcsc_cotodd_condition: Incomplete
cotcsc_cotodd: Incomplete

def trig_sincos_rule(integral): ...
def trig_tansec_rule(integral): ...
def trig_cotcsc_rule(integral): ...
def trig_sindouble_rule(integral): ...
def trig_powers_products_rule(integral): ...
def trig_substitution_rule(integral): ...
def heaviside_rule(integral): ...
def dirac_delta_rule(integral: IntegralInfo): ...
def substitution_rule(integral): ...

partial_fractions_rule: Incomplete
cancel_rule: Incomplete
distribute_expand_rule: Incomplete
trig_expand_rule: Incomplete

def derivative_rule(integral): ...
def rewrites_rule(integral): ...
def fallback_rule(integral): ...
def integral_steps(integrand, symbol, **options): ...
def manualintegrate(f, var): ...
