import sympy as sp

from ncpol3sdpa.equality_constraints import apply_rule, apply_rule_to_polynom


# return a list of monomials without the monom that lead the equality rules
# ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
def needed_monomials(monomials, rules):
    needed_mono = [monomial for monomial in monomials if monomial not in rules.keys()]
    return needed_mono


#
def create_matrix(L):  # L list of all the monomials used in the moment matrix
    # this list goes to the degree k of the moment matrix
    n = len(L)
    M = []
    for i in range(n):
        P = [0] * n
        M.append(P)

    for i in range(n):
        for j in range(n):
            M[i][j] = L[i] * L[j]
    return M


def create_matrix_of_constraints(
    L, Q, q
):  # L list of all the monomials used in the moment matrix
    # Q polynome of constraints Q(X,Y) < q
    n = len(L)
    M = []
    for i in range(n):
        P = [0] * n
        M.append(P)
    for i in range(n):
        for j in range(n):
            M[i][j] = (q - Q) * (L[i] * L[j])
    return M


# Return a moment matrix whith cvxpy variables
def create_moment_matrix(monomials, rules):
    n = len(monomials)
    variable_of_monomial = {}
    index_var = 0
    var = sp.symbols("y%d" % index_var)
    moment_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            monom = apply_rule(monomials[i] * monomials[j], rules)
            if monom not in variable_of_monomial:
                variable_of_monomial[monom] = var
                index_var += 1
                var = sp.symbols("y%d" % index_var)
            moment_matrix[i][j] = variable_of_monomial[monom]
    return moment_matrix, variable_of_monomial


# return the matrix of contraint with cvxpy variables
def create_matrix_constraint(variable_of_monomial, monomials, polynom, rules):
    n = len(monomials)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            moment_coeff = apply_rule_to_polynom(monomials[i] * monomials[j] * polynom, rules)
            coeff_terms = [
                (coeff, term)
                for term, coeff in sp.expand(moment_coeff)
                .as_coefficients_dict()
                .items()
            ]
            for k in range(len(coeff_terms)):
                matrix[i][j] += (
                    coeff_terms[k][0] * variable_of_monomial[coeff_terms[k][1]]
                )
    return matrix


class MomentMatrix:
    def __init__(self, polynom, constraints):
        self.optimized = None
        self.constraints = None

    def __mul__(self, other): ...

    def __repr__(self): ...

    def _method1(self): ...
