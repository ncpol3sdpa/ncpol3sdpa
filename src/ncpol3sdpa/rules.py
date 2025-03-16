from __future__ import annotations
from typing import List, Tuple, Dict, Any
from ncpol3sdpa.constraints import Constraint
from sympy import rem, poly, Symbol
# from sympy.ntheory import qs

class Rule:

    @classmethod
    def _of_constraint(cls, constraint : Constraint) -> Tuple[Any]:
        """Private methode creating a Tuple of equivalence"""

        # express polynom as a list of monom
        polynom = poly(constraint.polynom).terms()  

        leader_monomial = max(polynom,key=lambda monom : sum(monom[0]))

        # leader_monom expressed with variables
        leader_monomial_expressed = 1  
        for monom_index in range(len(poly(constraint.polynom).gens)):
            leader_monomial_expressed *= (
                poly(constraint.polynom).gens[monom_index] ** leader_monomial[0][monom_index]
            )

        # rewriting the constraint as a rule
        polynom_without_leader = constraint.polynom  
        polynom_without_leader /= leader_monomial[1]
        polynom_without_leader -= leader_monomial_expressed
        polynom_without_leader *= -1

        return (
            leader_monomial_expressed.as_expr(), 
            polynom_without_leader.as_expr()
        )

    @classmethod
    def of_constraints(cls, constraints : List[Constraint]) -> Dict[Symbol, Any]:
        """return the rules that represent a list of constraint
        exemple : of_constraints([x²-x-1=0, x*y²+3=0]) = {x²->x+1, x*y²->-3}"""
        return dict([
            Rule._of_constraint(constraint) 
            for constraint in constraints
        ])

def apply_rule(monom, rules):
    for key in rules.keys():
        if rem(monom, key) == 0:
            return apply_rule(monom*rules[key]/key, rules) 
    return monom

def apply_rule_to_polynom(polynom, rules):
    poly_dict = polynom.as_coefficients_dict()
    res = 0
    for monom,coeff in poly_dict.items():
        res += coeff*apply_rule(monom, rules)
    return res

def solve_equality_constraints(): ...
