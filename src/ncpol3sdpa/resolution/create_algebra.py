from __future__ import annotations
from typing import List, Type

import sympy as sp

from .rules import Rules
from .algebra import AlgebraSDP
from .algebra_sdp_real import AlgebraSDPReal
from .algebra_sdp_complex import AlgebraSDPComplex
from .algebra_sdp_nc_complex import AlgebraSDPncComplex
from .algebra_sdp_nc_real import AlgebraSDPncReal


def create_AlgebraSDP(
    needed_variables: List[sp.Symbol],
    objective: sp.Expr,
    relaxation_order: int,
    substitution_rules: Rules,
    is_commutative: bool = True,
    is_real: bool = True,
) -> AlgebraSDP:
    AlgebraSubClass: Type[AlgebraSDP]
    match (is_commutative, is_real):
        case (True, True):
            AlgebraSubClass = AlgebraSDPReal
        case (True, False):
            AlgebraSubClass = AlgebraSDPComplex
        case (False, True):
            AlgebraSubClass = AlgebraSDPncReal
        case (False, False):
            AlgebraSubClass = AlgebraSDPncComplex

    return AlgebraSubClass(
        needed_variables,
        objective,
        relaxation_order,
        substitution_rules,
    )
