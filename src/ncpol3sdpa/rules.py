from __future__ import annotations
from typing import List, Tuple, Dict
from ncpol3sdpa.constraints import Constraint
from sympy import rem, poly, Expr, S


class Rule:
    @classmethod
    def _of_constraint(cls, constraint: Constraint) -> Tuple[Expr, Expr]:
        """Private methode creating a Tuple of equivalence"""

        # express polynom as a list of monom
        polynom: List[Tuple[Tuple[int, ...], int]] = poly(constraint.polynom).terms()

        leader_monomial = max(polynom, key=lambda monom: sum(monom[0]))

        # leader_monom expressed with variables
        leader_monomial_expressed: Expr = S.One
        for i, monomial in enumerate(poly(constraint.polynom).gens):
            leader_monomial_expressed *= monomial ** leader_monomial[0][i]
        assert isinstance(leader_monomial_expressed, Expr)

        # rewriting the constraint as a rule
        polynom_without_leader: Expr = constraint.polynom
        polynom_without_leader /= leader_monomial[1]
        polynom_without_leader -= leader_monomial_expressed
        polynom_without_leader *= -1
        assert isinstance(polynom_without_leader, Expr)

        return (leader_monomial_expressed, polynom_without_leader)

    @classmethod
    def of_constraints(cls, constraints: List[Constraint]) -> Dict[Expr, Expr]:
        """return the rules that represent a list of constraint
        exemple : of_constraints([x²-x-1=0, x*y²+3=0]) = {x²->x+1, x*y²->-3}"""
        return dict([Rule._of_constraint(constraint) for constraint in constraints])


def apply_rule(monom: Expr, rules: Dict[Expr, Expr]) -> Expr:
    """Apply a rule to a monomial"""

    for key in rules.keys():
        if rem(monom, key) == 0:
            return apply_rule(monom * rules[key] / key, rules)
    return monom


def apply_rule_to_polynom(polynom: Expr, rules: Dict[Expr, Expr]) -> Expr:
    """Apply a rule to a polynomial"""

    poly_dict: Dict[Expr, int] = polynom.as_coefficients_dict()  # type: ignore
    res: Expr = S.Zero

    res = 0
    for monom, coef in poly_dict.items():
        res += coef * apply_rule(monom, rules)
    return res


def solve_equality_constraints() -> None: ...
