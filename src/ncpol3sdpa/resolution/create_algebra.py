from __future__ import annotations
from typing import List, Type

import sympy as sp

from .rules import Rule
from .algebra import AlgebraSDP
from .algebra_sdp_real import AlgebraSDPReal
from .algebra_sdp_complex import AlgebraSDPComplex


def create_AlgebraSDP(
    needed_variables: List[sp.Symbol],
    objective: sp.Expr,
    relaxation_order: int,
    substitution_rules: Rule,
    is_commutative: bool = True,
    is_real: bool = True,
) -> AlgebraSDP:
    AlgebraSubClass: Type[AlgebraSDP]
    AlgebraSubClass = AlgebraSDPReal if is_real else AlgebraSDPComplex

    return AlgebraSubClass(
        needed_variables,
        objective,
        relaxation_order,
        substitution_rules,
        is_commutative,
    )
