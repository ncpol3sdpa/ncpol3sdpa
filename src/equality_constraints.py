import sympy as sp
from constraints import *


# return the rule associated to a polynom
# exemple : rule_of_constraint(x²-x-1=0) = (x², x+1) because the rule is x² -> x+1
def rule_of_constraint(constraint):
    polynom = constraint.polynom
    polynom /= sp.LC(constraint.polynom)     # normalisation of the constraint
    leader_monomial = sp.LM(polynom)         
    polynom -= leader_monomial
    polynom *= -1                            # rewriting the constraint as x^n = -1/a * Q(x)
    return [leader_monomial, polynom]
        
#return the hashtbl rules that represent a list of constraint, constraints 
#exemple : rules_of_constraints([x²-x-1=0, x*y²+3=0]) = {x²->x+1, x*y²->-3}
def rules_of_constraints(constraints):
    rules = {}
    for constraint in constraints:
        leader_monomial, polynom = rule_of_constraint(constraint)
        rules[leader_monomial] = polynom 
    return rules
        

def solve_equality_constraints(): ...
