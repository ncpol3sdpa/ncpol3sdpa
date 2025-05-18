# typing
from typing import List, Dict, Tuple
from hypothesis.strategies import SearchStrategy, DrawFn

# from hypothesis import given
import sympy
from hypothesis.strategies import composite, one_of, lists, just, builds, integers
from ncpol3sdpa.resolution.rules import Rule

from ncpol3sdpa.resolution.monomial import generate_monomials
import testing.draw_strategies.float_strategies as float_strategies

one_symbol: List[sympy.Symbol] = [sympy.Symbol("x")]
two_symbols: List[sympy.Symbol] = [sympy.Symbol("x"), sympy.Symbol("y")]
three_symbols: List[sympy.Symbol] = [
    sympy.Symbol("x"),
    sympy.Symbol("y"),
    sympy.Symbol("z"),
]


def n_symbols(n: int) -> List[sympy.Symbol]:
    return [sympy.Symbol(f"x{i}") for i in range(n)]


def gen_symbols(max_symbols: int) -> SearchStrategy[List[sympy.Symbol]]:
    return builds(n_symbols, integers())


@composite
def polynomials_from_monomials(
    draw: DrawFn,
    monomials: list[sympy.Expr],
    coefs: SearchStrategy[float] = float_strategies.small_normal_floats,
    is_commutative: bool = True,
) -> sympy.Expr:
    terms: List[sympy.Expr] = [draw(coefs) * monomial for monomial in monomials]
    poly = sum(terms)
    if isinstance(poly, sympy.Expr):
        return poly
    else:
        return sympy.core.numbers.Zero()  # type: ignore


def polynomials_commutative(
    symbols: List[sympy.Symbol],
    degree: int,
    coefs: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> SearchStrategy[sympy.Expr]:
    """All possible polynomials of a certain degree or lower"""
    monomials = generate_monomials(
        symbols=symbols, relaxation_order=degree, is_commutative=True
    )

    return polynomials_from_monomials(
        monomials=monomials, coefs=coefs, is_commutative=True
    )  # .filter(leading coefficients non zero?)


def pick_monomials(monomials: List[sympy.Expr]) -> SearchStrategy[sympy.Expr]:
    def justifier(x: sympy.Expr) -> SearchStrategy[sympy.Expr]:
        return just(x)

    rt: SearchStrategy[sympy.Expr] = one_of(list(map(justifier, monomials)))
    return rt


def generate_rules_1to1(
    monomials: List[sympy.Expr], max_rules: int | None = None
) -> SearchStrategy[Rule]:
    """Generates a list of rules of the form Y³X² -> XY.
    Always monomial to monomial. Rules it generates must decrees the degree (otherwise
    there a risk of generating rules that loop forever)
    The scalar multiplier between the monomials is always 1"""
    monomial_gen = pick_monomials(monomials)

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
    return rt.map(lambda x: Rule.from_dict(x))
