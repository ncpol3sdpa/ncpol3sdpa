from __future__ import annotations
from typing import Dict, List, Tuple

from sympy import Expr, S, poly, rem, Mul, Pow

from .constraints import Constraint


def list_of_monomial(monomial: Expr) -> List[Expr]:
    """return a list of the factor a a monomial non commutative"""
    if isinstance(monomial, int):
        return [monomial]
    res = []
    for factor in monomial.as_ordered_factors():
        if isinstance(factor, Pow):
            base, exp = factor.as_base_exp()  # type: ignore
            res.extend([base] * exp)
        else:
            res.append(factor)
    return res


class Rule:
    def __init__(self, constraints: List[Constraint]) -> None:
        """Constructor of the class Rule"""

        self.rules = dict(
            [Rule.of_single_constraint(constraint) for constraint in constraints]
        )

    @classmethod
    def from_dict(cls, rules: Dict[Expr, Expr]) -> Rule:
        """Constructor of the class Rule from a dictionary"""
        res = cls([])
        res.rules = rules
        return res

    @classmethod
    def of_single_constraint(cls, constraint: Constraint) -> Tuple[Expr, Expr]:
        """Private method creating a Tuple of equivalence"""

        # express polynomial as a list of monomial
        polynomial: List[Tuple[Tuple[int, ...], float]] = poly(
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

    # @classmethod
    # def of_constraints(cls, constraints: List[Constraint]) -> Dict[Expr, Expr]:
    #     """return the rules that represent a list of constraint
    #     exemple : of_constraints([x²-x-1=0, x*y²+3=0]) = {x²->x+1, x*y²->-3}"""
    #     return dict(
    #         [Rule.of_single_constraint(constraint) for constraint in constraints]
    #     )

    def apply_to_monomial(self, monomial: Expr, is_commutative: bool = True) -> Expr:
        """Apply a rule to a monomial"""
        if is_commutative:
            for key in self.rules.keys():
                if rem(monomial, key) == 0:
                    return self.apply_to_monomial(
                        monomial * self.rules[key] / key, is_commutative
                    )
            return monomial
        else:
            to_change_monomial = list_of_monomial(monomial)
            for key in self.rules.keys():
                rule_monomial = list_of_monomial(key)
                for i in range(len(to_change_monomial) - len(rule_monomial) + 1):
                    if to_change_monomial[i : i + len(rule_monomial)] == rule_monomial:
                        return self.apply_to_monomial(
                            Mul(*(to_change_monomial[: max(0, i)]))
                            * self.rules[key]
                            * Mul(*to_change_monomial[(i + len(rule_monomial)) :]),
                            is_commutative,
                        )
            return monomial

    def apply_to_polynomial(
        self, polynomial: Expr, is_commutative: bool = True
    ) -> Expr:
        """Apply a rule to a polynomial"""

        poly_dict: Dict[Expr, float] = polynomial.as_coefficients_dict()

        res: Expr = S.Zero
        for monomial, coef in poly_dict.items():
            res += coef * self.apply_to_monomial(monomial, is_commutative)
        return res

    def filter_monomials(self, monomials: List[Expr]) -> List[Expr]:
        """Filter the monomials according to the rules"""

        return [monomial for monomial in monomials if monomial not in self.rules.keys()]
