from ncpol3sdpa.sdp_repr import (
    MomentMatrixSDP,
    ProblemSDP,
    EqConstraint,
)

from scipy.sparse import lil_matrix

# typing
from typing import Tuple, TypeVar, List
from hypothesis.strategies import SearchStrategy, DrawFn

# from hypothesis import given
import numpy as np
from hypothesis.strategies import integers, composite, permutations, lists
from hypothesis.extra import numpy as hyp_np

import testing.draw_strategies.float_strategies as float_strategies

# TODO: Figure out typing for hypothesis


@composite
def triangular_position(draw: DrawFn, max: int) -> Tuple[int, int]:
    """Generates integers (i,j) such that max > i >= j >= 0"""
    n1 = draw(integers(min_value=0, max_value=max - 1))  # inclusive on both sides
    n2 = draw(integers(min_value=0, max_value=n1))
    return (n1, n2)


@composite
def symmetric_matrices(
    draw: DrawFn,
    size: int | SearchStrategy[int],
    elements: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> lil_matrix:
    if not isinstance(size, int):
        size = draw(size)
    m = draw(hyp_np.arrays(np.float64, shape=(size, size), elements=elements))

    return lil_matrix(m + m.T)


A = TypeVar("A")


@composite
def equivalence_classes(draw: DrawFn, list: List[A]) -> List[List[A]]:
    """Generate a list of equivalence classes from a list. This means that
    every element in list appears exactly once in one of the elements of result
    Exemple: [1,2,3,4,5,6] becomes [[1,6,4], [2], [3,5]]"""
    n = len(list)
    # More classes is simpler, so this the correct way for shrinking
    number_of_classes = n - draw(integers(min_value=0, max_value=n - 1))
    class_generator = integers(
        min_value=0, max_value=number_of_classes - 1
    )  # order does not mater here

    shuffle = draw(permutations(list))

    rt: List[List[A]] = [[] for _ in range(number_of_classes)]
    for elem in shuffle:
        class_of_elem = draw(class_generator)
        rt[class_of_elem].append(elem)

    return rt


@composite
def gen_MomentMatrixSDPs(
    draw: DrawFn, min_size: int = 1, max_size: int | None = None
) -> MomentMatrixSDP:
    assert min_size >= 0
    size = draw(integers(min_value=min_size, max_value=max_size))
    all_positions: List[Tuple[int, int]] = [
        (i, j) for j in range(size) for i in range(size) if j <= i
    ]
    return MomentMatrixSDP(size, draw(equivalence_classes(all_positions)))


@composite
def gen_ProblemSDPs_no_constraints(
    draw: DrawFn,
    num_strat: SearchStrategy[float] = float_strategies.small_normal_floats,
    min_size: int = 1,
    max_size: int | None = None,
    max_vars: int = 10,
) -> ProblemSDP:
    assert min_size >= 0
    mm = draw(gen_MomentMatrixSDPs(min_size=min_size, max_size=max_size))
    obj = draw(symmetric_matrices(mm.size, num_strat))
    rt = ProblemSDP(mm, obj)
    rt.variable_sizes += draw(
        lists(integers(min_value=min_size, max_value=max_size), max_size=max_vars)
    )
    return rt


@composite
def gen_eq_constraints(
    draw: DrawFn,
    problem: ProblemSDP,
    num_strat: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> EqConstraint:
    num_vars = len(problem.variable_sizes)
    involved_vars = draw(
        lists(
            integers(min_value=0, max_value=num_vars - 1),
            max_size=num_vars,
            unique=True,
        )
    )

    # the formatting on this is atrocious ...
    terms: List[Tuple[int, lil_matrix]] = [
        (
            var_num,
            draw(
                symmetric_matrices(
                    size=problem.variable_sizes[var_num], elements=num_strat
                )
            ),
        )
        for var_num in involved_vars
    ]

    return EqConstraint(terms)


@composite
def gen_ProblemSDPs_with_constraints(
    draw: DrawFn,
    problem_strat: SearchStrategy[ProblemSDP],
    max_constraints: int = 10,
    num_strat: SearchStrategy[float] = float_strategies.small_normal_floats,
) -> ProblemSDP:
    problem = draw(problem_strat)
    gen_constraints = gen_eq_constraints(num_strat=num_strat, problem=problem)
    gen_constraints_s = lists(elements=gen_constraints, max_size=max_constraints)
    problem.constraints = draw(gen_constraints_s)
    return problem
