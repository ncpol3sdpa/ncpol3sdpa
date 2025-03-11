# return the rule associated to a polynom
# exemple : rule_of_constraint(x²-x-1=0) = (x², x+1) because the rule is x² -> x+1
def rule_of_constraint(constraint):
    polynom = constraint.polynom.terms()  # express polynom as a list of monom

    max_degree = (
        constraint.polynom.total_degree()
    )  # degree of the polynom seen as a multivariable polynom

    leader_monomials = [
        monom for monom in polynom if sum(monom[0]) == max_degree
    ]  # list of monom that maximize the degree of the polynom

    leader_monomial = leader_monomials[0]

    leader_monomial_expressed = 1  # leader_monom expressed with variables
    for monom_index in range(len(constraint.polynom.gens)):
        leader_monomial_expressed *= (
            constraint.polynom.gens[monom_index] ** leader_monomial[0][monom_index]
        )

    polynom_without_leader = constraint.polynom  # rewriting the constraint as a rule
    polynom_without_leader /= leader_monomial[1]
    polynom_without_leader -= leader_monomial_expressed
    polynom_without_leader *= -1

    return [leader_monomial_expressed, polynom_without_leader]


# return the hashtbl rules that represent a list of constraint, constraints
# exemple : rules_of_constraints([x²-x-1=0, x*y²+3=0]) = {x²->x+1, x*y²->-3}
def rules_of_constraints(constraints):
    rules = {}
    for constraint in constraints:
        leader_monomial, polynom = rule_of_constraint(constraint)
        rules[leader_monomial] = polynom
    return rules


def solve_equality_constraints(): ...
