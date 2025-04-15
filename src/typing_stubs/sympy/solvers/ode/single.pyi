from .hypergeometric import equivalence_hypergeometric as equivalence_hypergeometric, get_sol_2F1_hypergeometric as get_sol_2F1_hypergeometric, match_2nd_2F1_hypergeometric as match_2nd_2F1_hypergeometric, match_2nd_hypergeometric as match_2nd_hypergeometric
from .ode import dsolve as dsolve, homogeneous_order as homogeneous_order, ode_sol_simplicity as ode_sol_simplicity, odesimp as odesimp
from .riccati import match_riccati as match_riccati, solve_riccati as solve_riccati
from _typeshed import Incomplete
from sympy.core import Add as Add, Pow as Pow, Rational as Rational, S as S
from sympy.core.cache import cached_property as cached_property
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, Subs as Subs, diff as diff, expand as expand
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import zoo as zoo
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.functions import airyai as airyai, airybi as airybi, besselj as besselj, bessely as bessely, cbrt as cbrt, exp as exp, log as log, sqrt as sqrt, tan as tan
from sympy.integrals import Integral as Integral
from sympy.polys import Poly as Poly
from sympy.polys.polytools import cancel as cancel, degree as degree, factor as factor
from sympy.polys.solvers import PolyNonlinearError as PolyNonlinearError
from sympy.simplify import collect as collect, logcombine as logcombine, posify as posify, separatevars as separatevars, simplify as simplify
from sympy.simplify.radsimp import fraction as fraction
from sympy.solvers.deutils import ode_order as ode_order
from sympy.solvers.solvers import solve as solve
from sympy.utilities import numbered_symbols as numbered_symbols
from typing import ClassVar, Iterator

class ODEMatchError(NotImplementedError): ...

class SingleODEProblem:
    eq: Expr
    func: AppliedUndef
    sym: Symbol
    prep: Incomplete
    params: Incomplete
    def __init__(self, eq, func, sym, prep: bool = True, **kwargs) -> None: ...
    def order(self) -> int: ...
    def eq_preprocessed(self) -> Expr: ...
    def eq_high_order_free(self) -> Expr: ...
    def eq_expanded(self) -> Expr: ...
    def get_numbered_constants(self, num: int = 1, start: int = 1, prefix: str = 'C') -> list[Symbol]: ...
    def iter_numbered_constants(self, start: int = 1, prefix: str = 'C') -> Iterator[Symbol]: ...
    def is_autonomous(self): ...
    def get_linear_coefficients(self, eq, func, order): ...

class SingleODESolver:
    hint: ClassVar[str]
    has_integral: ClassVar[bool]
    ode_problem: SingleODEProblem
    order: list | None
    def __init__(self, ode_problem) -> None: ...
    def matches(self) -> bool: ...
    def get_general_solution(self, *, simplify: bool = True) -> list[Equality]: ...

class SinglePatternODESolver(SingleODESolver):
    def wilds(self): ...
    def wilds_match(self): ...

class NthAlgebraic(SingleODESolver):
    hint: str
    has_integral: bool

class FirstExact(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class FirstLinear(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class AlmostLinear(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class Bernoulli(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class Factorable(SingleODESolver):
    hint: str
    has_integral: bool

class RiccatiSpecial(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class RationalRiccati(SinglePatternODESolver):
    has_integral: bool
    hint: str
    order: Incomplete

class SecondNonlinearAutonomousConserved(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class Liouville(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class Separable(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class SeparableReduced(Separable):
    hint: str
    has_integral: bool
    order: Incomplete

class HomogeneousCoeffSubsDepDivIndep(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class HomogeneousCoeffSubsIndepDivDep(SinglePatternODESolver):
    hint: str
    has_integral: bool
    order: Incomplete

class HomogeneousCoeffBest(HomogeneousCoeffSubsIndepDivDep, HomogeneousCoeffSubsDepDivIndep):
    hint: str
    has_integral: bool
    order: Incomplete

class LinearCoefficients(HomogeneousCoeffBest):
    hint: str
    has_integral: bool
    order: Incomplete

class NthOrderReducible(SingleODESolver):
    hint: str
    has_integral: bool

class SecondHypergeometric(SingleODESolver):
    hint: str
    has_integral: bool

class NthLinearConstantCoeffHomogeneous(SingleODESolver):
    hint: str
    has_integral: bool

class NthLinearConstantCoeffVariationOfParameters(SingleODESolver):
    hint: str
    has_integral: bool

class NthLinearConstantCoeffUndeterminedCoefficients(SingleODESolver):
    hint: str
    has_integral: bool

class NthLinearEulerEqHomogeneous(SingleODESolver):
    hint: str
    has_integral: bool

class NthLinearEulerEqNonhomogeneousVariationOfParameters(SingleODESolver):
    hint: str
    has_integral: bool

class NthLinearEulerEqNonhomogeneousUndeterminedCoefficients(SingleODESolver):
    hint: str
    has_integral: bool

class SecondLinearBessel(SingleODESolver):
    hint: str
    has_integral: bool

class SecondLinearAiry(SingleODESolver):
    hint: str
    has_integral: bool

class LieGroup(SingleODESolver):
    hint: str
    has_integral: bool

solver_map: Incomplete
