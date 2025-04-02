from __future__ import annotations

from typing import Dict, List, Tuple

from sympy import Expr, S, poly, rem, Mul, Pow

from ncpol3sdpa.constraints import Constraint


class Rule:
    @classmethod
    def _of_constraint(cls, constraint: Constraint) -> Tuple[Expr, Expr]:
        """Private method creating a Tuple of equivalence"""

        # express polynomial as a list of monomial
        polynomial: List[Tuple[Tuple[int, ...], int]] = poly(
            constraint.polynomial
        ).terms()

        leader_monomial = max(polynomial, key=lambda monomial: sum(monomial[0]))

        # leader_monomial expressed with variables
        leader_monomial_expressed: Expr = S.One
        for i, monomial in enumerate(poly(constraint.polynomial).gens):
            leader_monomial_expressed *= monomial ** leader_monomial[0][i]
        assert isinstance(leader_monomial_expressed, Expr)

        # rewriting the constraint as a rule
        polynomial_without_leader: Expr = constraint.polynomial
        polynomial_without_leader /= leader_monomial[1]
        polynomial_without_leader -= leader_monomial_expressed
        polynomial_without_leader *= -1
        assert isinstance(polynomial_without_leader, Expr)

        return (leader_monomial_expressed, polynomial_without_leader)

    @classmethod
    def of_constraints(cls, constraints: List[Constraint]) -> Dict[Expr, Expr]:
        """return the rules that represent a list of constraint
        exemple : of_constraints([x²-x-1=0, x*y²+3=0]) = {x²->x+1, x*y²->-3}"""
        return dict([Rule._of_constraint(constraint) for constraint in constraints])

def list_of_monomial(monomial : Expr) -> List[Expr]:
    """return a list of the factor a a monomial non commutative"""
    res = []
    for factor in monomial.as_ordered_factors():
        if isinstance(factor, Pow):
            base, exp = factor.as_base_exp()
            res.extend([base] * exp)
        else:
            res.append(factor)
    return res

def apply_rule(
    monomial: Expr, rules: Dict[Expr, Expr], commutative: bool = True
) -> Expr:
    """Apply a rule to a monomial"""
    if commutative:
        for key in rules.keys():
            if rem(monomial, key) == 0:
                return apply_rule(monomial * rules[key] / key, rules, commutative)
        return monomial
    else:
        to_change_monomial = list_of_monomial(monomial)
        for key in rules.keys():
            rule_monomial = list_of_monomial(key)
            for i in range(len(to_change_monomial) - len(rule_monomial) + 1):
                if to_change_monomial[i : i + len(rule_monomial)] == rule_monomial:
                    return apply_rule(
                        Mul(*(to_change_monomial[: max(0, i)]))
                        * rules[key]
                        * Mul(*to_change_monomial[(i + len(rule_monomial)) :]), rules, commutative
                    )
        return monomial


def apply_rule_to_polynomial(polynomial: Expr, rules: Dict[Expr, Expr], commutative: bool = True) -> Expr:
    """Apply a rule to a polynomial"""

    poly_dict: Dict[Expr, int] = polynomial.as_coefficients_dict()  # type: ignore

    res: Expr = S.Zero
    for monomial, coef in poly_dict.items():
        res += coef * apply_rule(monomial, rules, commutative)
    return res
