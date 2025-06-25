# typing
from typing import List
from hypothesis.strategies import SearchStrategy

# from hypothesis import given
import sympy
from hypothesis.strategies import builds, integers, booleans, just, lists


import ncpol3sdpa.problem as problem
from ncpol3sdpa.resolution.constraints import Constraint
import testing.draw_strategies.float_strategies as float_strategies
import testing.draw_strategies.polynomials as polynomials


def constraint_gen(
    symbols: List[sympy.Symbol],
    max_degree: int = 10,
    floats: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> SearchStrategy[Constraint]:
    polynomials_custom = builds(
        polynomials.polynomials,
        symbols=just(symbols),
        degree=integers(min_value=0, max_value=max_degree),
        coefs=floats,
    )
    return builds(
        Constraint,
        is_equality_constraint=booleans(),
        polynomial=polynomials_custom,
        substitution=just(False),
    )


def substitution_gen(
    symbols: List[sympy.Symbol],
    max_degree: int = 10,
    floats: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> SearchStrategy[Constraint]:
    raise NotImplementedError


def problems_no_constraints(
    symbols: List[sympy.Symbol],
    floats: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> SearchStrategy[problem.Problem]:
    raise NotImplementedError
    return builds(
        problem.Problem,
        obj=polynomials.polynomials(
            symbols=symbols,
            max_degree=10,
            coefs=floats,  # TODO no 10 constants
        ),
    )


def problems(
    symbols: List[sympy.Symbol],
    floats: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> SearchStrategy[problem.Problem]:
    constraints = lists(elements=constraint_gen(symbols=symbols, floats=floats))
    return builds(
        (lambda x, y: x.constraints.append(y)),
        problems_no_constraints(symbols=symbols, floats=floats),
        constraints,
    )
