import sympy
from typing import List

from ncpol3sdpa.resolution.algebra_sdp_real import AlgebraSDPReal
from ncpol3sdpa.resolution.rules import Rules
from ncpol3sdpa.resolution.algebra import create_moment_matrix
import ncpol3sdpa.resolution.monomial as lib_monomial
import ncpol3sdpa.resolution.utils as utils

from testing.draw_strategies.polynomials import generate_rules_1to1
import testing.draw_strategies.polynomials as draw_poly

from hypothesis.strategies import lists, just, integers
from hypothesis import given, settings

# TODO : add arbitrarily large monomials
monomials_3_7: List[sympy.Expr] = lib_monomial.generate_monomials(
    draw_poly.three_symbols, 7, is_commutative=True
)

monomials_3_4: List[sympy.Expr] = lib_monomial.generate_monomials(
    draw_poly.three_symbols, 4, is_commutative=True
)

monomials_2_3: List[sympy.Expr] = lib_monomial.generate_monomials(
    draw_poly.two_symbols, 3, is_commutative=True
)


@given(
    generate_rules_1to1(monomials=monomials_3_7),
    lists(draw_poly.pick_monomials(monomials_3_7), max_size=20),
)
def test_filter_monomials(rules: Rules, monomial_list: List[sympy.Expr]) -> None:
    # this is mostly a crash test
    result = rules.filter_monomials(monomials=monomial_list)
    for monomial in result:
        assert monomial in monomial_list
        assert monomial not in rules.rules.keys()


# @given(just(monomials_3_7), just({}))
@settings(deadline=1000)  # Increase deadline to 1000ms
@given(just(monomials_3_4), generate_rules_1to1(monomials_3_4, max_rules=1))
def test_create_moment_matrix_commutative(
    monomials: List[sympy.Expr], substitution_rules: Rules
) -> None:
    # this is a crash test
    for big, small in substitution_rules.rules.items():
        assert sympy.total_degree(big) > sympy.total_degree(small)

    needed_monomials = substitution_rules.filter_monomials(monomials)
    _m = create_moment_matrix(needed_monomials, substitution_rules, is_commutative=True)
    # TODO assert specialization is PSD?


@given(lists(draw_poly.polynomials_commutative(draw_poly.three_symbols, 5), max_size=5))
def test_generate_needed_symbols(polynomials: List[sympy.Expr]) -> None:
    pass
    result_symbols = utils.generate_needed_symbols(polynomials)
    for symbol in result_symbols:
        assert symbol in draw_poly.three_symbols


# @hypothesis.settings(max_examples=200)
@settings(deadline=1000)
@given(
    just(draw_poly.two_symbols),
    draw_poly.polynomials_from_monomials(monomials_2_3),
    integers(min_value=3, max_value=4),
    draw_poly.generate_rules_1to1(monomials_2_3, max_rules=3),
)
def test_AlgebraSDP(
    needed_variables: List[sympy.Symbol],
    objective: sympy.Expr,
    relaxation_order: int,
    substitution_rules: Rules,
) -> None:
    # crash tests
    al = AlgebraSDPReal(
        needed_variables=needed_variables,
        objective=objective,
        relaxation_order=relaxation_order,
        substitution_rules=substitution_rules,
    )

    # TODO interesting checks
    for term in al.objective.as_coefficients_dict():
        monomial = term
        assert monomial not in substitution_rules.rules.keys()
        assert monomial in al.monomials
