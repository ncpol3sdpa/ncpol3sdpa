# typing
from typing import List, Dict, Tuple
from hypothesis.strategies import SearchStrategy

# from hypothesis import given
import sympy
from hypothesis.strategies import sampled_from, lists, builds, integers, just
from ncpol3sdpa.resolution.rules import RulesCommutative

from ncpol3sdpa.resolution.monomial import generate_monomials
from ncpol3sdpa.resolution.utils import sympy_sum
import testing.draw_strategies.float_strategies as float_strategies

one_symbol: List[sympy.Symbol] = [sympy.Symbol("x")]
two_symbols: List[sympy.Symbol] = [sympy.Symbol("x"), sympy.Symbol("y")]
three_symbols: List[sympy.Symbol] = [
    sympy.Symbol("x"),
    sympy.Symbol("y"),
    sympy.Symbol("z"),
]


def n_symbols(
    n: int, commutative: bool = True, real: bool = True
) -> List[sympy.Symbol]:
    return [sympy.Symbol(f"x{i}", commutative=commutative) for i in range(n)]


def gen_symbols(max_symbols: int) -> SearchStrategy[List[sympy.Symbol]]:
    return builds(n_symbols, integers())


def polynomials_from_monomials(
    monomials: list[sympy.Expr],
    coefs: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> SearchStrategy[sympy.Expr]:
    n = len(monomials)
    # [a,b,c,...]
    coefficients = lists(coefs, min_size=n, max_size=n)

    # [(a,1), (b, x0), (c, x1), ...]
    coef_monomials = builds(zip, coefficients, just(monomials))

    # [a*1, b*x0, c*x1, ...]
    terms = builds(lambda lst: map(lambda t: t[0] * t[1], lst), coef_monomials)

    # a*1 + b*x0 + c*x1 + ...
    poly = builds(sympy_sum, terms)
    return poly


def polynomials(
    symbols: List[sympy.Symbol],
    max_degree: int,
    coefs: SearchStrategy[float] = float_strategies.small_normal_floats,
    is_commutative: bool = True,
) -> SearchStrategy[sympy.Expr]:
    """All possible polynomials of a certain degree or lower"""
    monomials = generate_monomials(
        symbols=symbols, relaxation_order=max_degree, is_commutative=True
    )

    return polynomials_from_monomials(monomials=monomials, coefs=coefs)


def square_polynomials(
    symbols: List[sympy.Symbol],
    max_degree: int = 3,
    coefs: SearchStrategy[float] = float_strategies.small_normal_floats,
    expand: bool = True,
) -> SearchStrategy[sympy.Expr]:
    # TODO support Noncommutative and complex case with p† * p

    poly = polynomials(symbols=symbols, max_degree=max_degree).map(lambda p: p * p)
    if expand:
        poly = builds(sympy.expand, poly)
    return poly


def sos_polynomials(
    symbols: List[sympy.Symbol],
    max_degree: int = 3,
    coefs: SearchStrategy[float] = float_strategies.small_normal_floats,
    expand: bool = True,
) -> SearchStrategy[sympy.Expr]:
    """generates sum of squares polynomials"""
    polys = lists(square_polynomials(symbols, max_degree, coefs, expand), max_size=4)

    return builds(sympy_sum, polys)


def generate_rules_1to1(
    monomials: List[sympy.Expr], max_rules: int | None = None
) -> SearchStrategy[RulesCommutative]:
    """Generates a list of rules of the form Y³X² -> XY.
    Always monomial to monomial. Rules it generates must decrees the degree (otherwise
    there a risk of generating rules that loop forever)
    The scalar multiplier between the monomials is always 1"""
    monomial_gen = sampled_from(monomials)

    def sort_tuple_by_degree(
        t: List[sympy.Expr],
    ) -> Tuple[sympy.Expr, sympy.Expr]:
        x, y = t[0], t[1]
        if sympy.total_degree(x) > sympy.total_degree(y):
            return x, y
        else:
            return y, x

    monomial_2ple: SearchStrategy[Tuple[sympy.Expr, sympy.Expr]] = lists(
        monomial_gen, unique_by=sympy.total_degree, min_size=2, max_size=2
    ).map(sort_tuple_by_degree)

    rt: SearchStrategy[Dict[sympy.Expr, sympy.Expr]] = builds(
        dict, lists(monomial_2ple, unique=True, max_size=max_rules)
    )
    return rt.map(lambda x: RulesCommutative(x))
