import sympy as sp
from sympy import Expr, Symbol, symbols
from sympy.simplify import simplify
from sympy.core.numbers import One as SymOne

from hypothesis import given

from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import (
    sampled_from,
    lists,
    builds,
)  # , integers, just, booleans
from testing.draw_strategies.polynomials import n_symbols
from testing.draw_strategies.float_strategies import order_of_magnitude_floats

from typing import List, Tuple, Dict

from ncpol3sdpa.resolution.monomial import generate_monomials
from ncpol3sdpa.resolution import Rules, RulesCommutative, RulesNoncommutative
from ncpol3sdpa.resolution.utils import degree_of_polynomial

n_vars = 3
max_degree_c = 6
max_degree_nc = 4

vars_c = n_symbols(n_vars, commutative=True)
vars_nc = n_symbols(n_vars, commutative=False)


def monomials(commutative: bool) -> SearchStrategy[Expr]:
    vars, max_degree = (
        (vars_c, max_degree_c) if commutative else (vars_nc, max_degree_nc)
    )
    return sampled_from(
        generate_monomials(vars, max_degree, is_commutative=commutative)
    )


def coef_monomials(commutative: bool) -> SearchStrategy[Expr]:
    return builds(
        lambda a, b: a * b,
        order_of_magnitude_floats(2).filter(lambda x: x != 0.0),
        monomials(commutative),
    )


monomials_c = monomials(commutative=True)
monomials_nc = monomials(commutative=False)


def polynomial_max_coef(p: Expr) -> float:
    m = 0.0
    for k in p.as_coefficients_dict().values():
        m = max(m, abs(k))
    return m


def rules_gen(
    commutative: bool, min_rules: int = 0, max_rules: int = 3
) -> SearchStrategy[Rules]:
    deg = sp.total_degree if commutative else degree_of_polynomial
    RuleT = RulesCommutative if commutative else RulesNoncommutative
    rule_couple: SearchStrategy[Tuple[Expr, Expr]] = (
        builds(lambda a, b: (a, b), monomials(commutative), monomials(commutative))
        .filter(lambda t: deg(t[0]) != deg(t[1]))
        .map(lambda t: t if deg(t[0]) > deg(t[1]) else (t[1], t[0]))
    )

    rs: SearchStrategy[Dict[Expr, Expr]] = builds(
        dict, lists(rule_couple, min_size=min_rules, max_size=max_rules)
    )
    return builds(RuleT, rs)


@given(monomials_c, monomials_c)
def test_divides_factors_P_c(m1: Expr, m2: Expr) -> None:
    rules = RulesCommutative()
    res = rules.divides_factors(m1, m2)

    if sp.total_degree(m1) > sp.total_degree(m2):
        m1, m2 = m2, m1
    if m1 == 0:
        return
    if res is not None:
        a, b = res
        assert polynomial_max_coef(sp.simplify(m2 - a * m1 * b)) < 1e-10


@given(monomials_nc, monomials_nc)
def test_divides_factors_P_nc(m1: Expr, m2: Expr) -> None:
    rules = RulesNoncommutative()
    res = rules.divides_factors(m1, m2)

    if degree_of_polynomial(m1) > degree_of_polynomial(m2):
        m1, m2 = m2, m1

    if m1 == 0:
        return

    if res is not None:
        a, b = res
        assert polynomial_max_coef(sp.simplify(m2 - a * m1 * b)) < 1e-10


@given(monomials_c.filter(lambda x: x != 0), monomials_c)
def test_divides_c(m1: Expr, a: Expr) -> None:
    rules = RulesCommutative()
    assert rules.divides_factors(m1, a * m1) is not None
    assert rules.divides(m1, a * m1)


@given(monomials_nc.filter(lambda x: x != 0), monomials_nc, monomials_nc)
def test_divides_nc(m1: Expr, a: Expr, b: Expr) -> None:
    rules = RulesNoncommutative()
    assert rules.divides_factors(m1, a * m1 * b) is not None
    assert rules.divides(m1, a * m1 * b)


@given(lists(monomials(commutative=False), max_size=10), rules_gen(False))
def test_apply_to_polynomial_nc(monomials: List[Expr], rules: RulesCommutative) -> None:
    poly = sp.sympify(sum(monomials))
    poly_sub = rules.apply_to_polynomial(poly)

    sub_monomials = [rules.apply_to_monomial(m_i) for m_i in monomials]
    poly_sub2 = sp.sympify(sum(sub_monomials))

    assert polynomial_max_coef(sp.simplify(poly_sub - poly_sub2)) < 1e-10


@given(lists(coef_monomials(commutative=True), max_size=10), rules_gen(True))
def test_apply_to_polynomial_c(monomials: List[Expr], rules: RulesCommutative) -> None:
    poly = sp.sympify(sum(monomials))
    poly_sub = rules.apply_to_polynomial(poly)

    sub_monomials = [rules.apply_to_monomial(m_i) for m_i in monomials]
    poly_sub2 = sp.sympify(sum(sub_monomials))

    assert polynomial_max_coef(sp.simplify(poly_sub - poly_sub2)) < 1e-10


def test_apply_rule() -> None:
    x, y = sp.symbols("x y")
    rules = RulesCommutative({x**2: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x**6 * y**2 * 5
    assert simplify(rules.apply_to_monomial(p1) - x * y) == 0
    assert simplify(rules.apply_to_monomial(p2) - x * y) == 0
    assert simplify(rules.apply_to_monomial(p3) - 5 * x * y**2) == 0


def test_apply_rule_nc() -> None:
    # non commutative tests
    x, y = sp.symbols("x y", commutative=False)
    rules = RulesNoncommutative({x * y: x})
    p1 = x * y
    p2 = x**2 * y
    p3 = x * y * x * y
    p4 = x * y * y
    assert rules.apply_to_monomial(p1) == x
    assert rules.apply_to_monomial(p2) == x**2
    assert rules.apply_to_monomial(p3) == x**2
    assert rules.apply_to_monomial(p4) == x


def test_needed_monomials() -> None:
    x: Symbol = symbols("x")
    y: Symbol = symbols("y")
    rules = RulesCommutative({x**2: x, y**3: 6 * x * y})
    monomials_list: List[Expr] = [
        SymOne(),
        x,
        x**2,
        y,
        y**2,
        x * y,
        x**2 * y,
        x * y**2,
        x**3,
        y**3,
    ]
    res = set(rules.filter_monomials(monomials_list))
    expected = [1, x, y, x * y, y**2, x * y**2]
    assert len(res) == len(expected)
    for monomial in expected:
        assert monomial in res


def test_needed_monomials_noncommutative() -> None:
    x: Symbol = symbols("x", commutative=False)
    y: Symbol = symbols("y", commutative=False)
    rules = RulesNoncommutative({x * y: x})
    monomials_list: List[Expr] = [
        SymOne(),
        x,
        y,
        #
        x**2,
        y**2,
        x * y,
        y * x,
        #
        x**2 * y,
        x * y * x,
        y * x**2,
        #
        x * y**2,
        y * x * y,
        y**2 * x,
        #
        x**3,
        y**3,
    ]
    res = set(rules.filter_monomials(monomials_list))
    expected = [
        SymOne(),
        x,
        y,
        #
        x**2,
        y**2,
        # x * y,
        y * x,
        #
        # x**2 * y,
        # x * y * x,
        y * x**2,
        #
        # x * y**2,
        # y * x * y,
        y**2 * x,
        #
        x**3,
        y**3,
    ]
    assert len(res) == len(expected)
    for monomial in expected:
        assert monomial in res


def test_needed_monomials_noncommutative2() -> None:
    x: Symbol = symbols("x", commutative=False)
    y: Symbol = symbols("y", commutative=False)
    rules = RulesNoncommutative({x * y: x, y**2: 6 * y * x})
    monomials_list: List[Expr] = [
        SymOne(),
        x,
        y,
        #
        x**2,
        y**2,
        x * y,
        y * x,
        #
        x**2 * y,
        x * y * x,
        y * x**2,
        #
        x * y**2,
        y * x * y,
        y**2 * x,
        #
        x**3,
        y**3,
    ]
    res = set(rules.filter_monomials(monomials_list))
    expected = [
        SymOne(),
        x,
        y,
        #
        x**2,
        # y**2,
        # x * y,
        y * x,
        #
        # x**2 * y,
        # x * y * x,
        y * x**2,
        #
        # x * y**2,
        # y * x * y,
        # y**2 * x,
        #
        x**3,
        # y**3,
    ]
    assert len(res) == len(expected)
    for monomial in expected:
        assert monomial in res
