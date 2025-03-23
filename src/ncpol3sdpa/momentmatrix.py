from __future__ import annotations
from typing import List, Tuple, Dict, Any
import sympy as sp
from ncpol3sdpa.rules import apply_rule, apply_rule_to_polynom
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.constraints import Constraint
import math

def needed_monomials(monomials : List[sp.Poly], rules : Dict[sp.Poly, Any]) -> List[sp.Poly]:
    """Filter the monomials according to the rules"""
    # ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
    return [
        monomial 
        for monomial in monomials 
        if monomial not in rules.keys()
    ]

def create_moment_matrix(monomials : List[sp.Poly]) -> List[List[sp.Poly]]:
    """Create the moment matrix of the monomials"""
    return [
        [ x*y for x in monomials ] 
        for y in monomials
    ]

def create_moment_matrix_commutative(
    monomials : List[sp.Poly], 
    substitution_rules : Dict[sp.Poly, Any]
) -> List[List[sp.Poly]]:
    """Create the moment matrix of the monomials for the commutative case"""

    matrix_size = len(monomials)
    return [[apply_rule(monomials[i] * monomials[j], substitution_rules) \
            for j in range(i+1)] for i in range(matrix_size)]

def create_constraint_matrix(
    monomials : List[sp.Poly],
    Q : sp.Poly,
    q : sp.Poly
) -> List[List[sp.Poly]]:
    """Create the matrix of constraints
    The constraints are of the form Q(X,Y) >= 0
    """
    return [
        [ (q - Q) * (x * y) for x in monomials ]
        for y in monomials
    ]

def create_constraint_matrix_commutative(
    monomials : List[sp.Poly],
    constraint_polynomial : sp.Poly,
    rules : Dict[sp.Poly, Any] 
) -> List[List[sp.Poly]]:
    """Create the matrix of constraints
    The constraints are of the form `constraint_polynomial >= 0`
    """

    n = len(monomials)
    return [[apply_rule_to_polynom(
                            sp.expand(monomials[i] * monomials[j] * constraint_polynomial), \
                            rules) \
            for j in range(i+1)] for i in range(n)]


def create_moment_matrix_cvxpy(
        monomials : List[sp.Poly], 
        rules : Dict[sp.Poly, Any]
    ) -> Tuple[List[List[sp.Poly]], Dict[sp.Poly, Any]]:
    """Return a moment matrix whith cvxpy variables"""

    n : int = len(monomials)
    index_var : int = 0
    moment_matrix : List[List[sp.Poly]] = [[0 for _ in range(n)] for _ in range(n)]
    variable_of_monomial = {}

    for i, monom1 in enumerate(monomials):
        for j, monom2 in enumerate(monomials):
            monom : sp.Poly = apply_rule(monom1 * monom2, rules)
            if monom not in variable_of_monomial:
                variable_of_monomial[monom] = sp.symbols(f"y{index_var}")
                index_var += 1
            moment_matrix[i][j] = variable_of_monomial[monom]

    return moment_matrix, variable_of_monomial


def create_constraints_matrix_cvxpy(
        variable_of_monomial : Dict[sp.Poly, Any],
        monomials : List[sp.Poly], 
        polynom : sp.Poly,
        rules : Dict[sp.Poly, Any]
    ) -> List[List[sp.Poly]]:
    """return the matrix of contraint with cvxpy variables"""

    n = len(monomials)
    matrix : List[List[sp.Poly]] = [[0 for _ in range(n)] for _ in range(n)]

    for i, monom1 in enumerate(monomials):
        for j, monom2 in enumerate(monomials):
            moment_coeff : sp.Poly = apply_rule_to_polynom(monom1 * monom2 * polynom, rules)
            constraints_dict = sp.expand(moment_coeff).as_coefficients_dict()
            for term, coeff in constraints_dict.items():
                matrix[i][j] += coeff * variable_of_monomial[term]
                
    return matrix

class MomentMatrix:
    def __init__(self, polynom : sp.Poly, monomials : List[sp.Poly]) -> None:
        self.optimized = None
        self.constraints = None

    def __mul__(self, other : MomentMatrix) -> MomentMatrix:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def _method1(self) -> None:
        raise NotImplementedError

class AlgebraSDP:
    def __init__(self, objective : sp.Poly, relaxation_order : int, substitution_rules : Dict[sp.Poly, sp.Poly]) -> None:
        """ Construct the symbolic Moment Matrices and soundings data structures. Works for the commutative case """ 
        self.objective = objective
        self.relaxation_order = relaxation_order
        self.substitution_rules = substitution_rules
        self.monomials : List[sp.Poly] = needed_monomials( \
                generate_monomials_commutative(objective.free_symbols, relaxation_order), \
                substitution_rules\
        )

        # In the commutative case, the moment matrix is symmetric
        self.moment_matrix = create_moment_matrix_commutative(self.monomials, self.substitution_rules)
        matrix_size = len (self.moment_matrix)

        # equivalence classes of equal coefficients
        self.monomial_to_positions : Dict[sp.Poly,List[Tuple[int, int]]]= {}
        for i in range(matrix_size):
            for j in range(i+1):
                monomial = self.moment_matrix[i][j]
                if monomial in self.monomial_to_positions.keys():
                    self.monomial_to_positions[monomial].append((i,j))
                else:
                    self.monomial_to_positions[monomial] = [(i,j)]

        # This is the positive semi-definite matrices in the sdp 
        #                                       v TODO Should this be a new type? discuss
        self.constraint_moment_matrices : List[ List[List[sp.poly]] ] = []
        # List of polynomials that equal 0
        self.equality_constraints : List[sp.poly] = []
    
    def add_constraint(self, constraint : Constraint) -> None:
        # validation
        for variable in constraint.polynom.free_symbols:
            # TODO Is this reasonable? Can be modified
            assert variable in self.objective.free_symbols

        if constraint.is_equality_constraint:
            self.equality_constraints.append(constraint.polynom)
        else:
            #inequality constraint
            # p.10 of Semidefinite programming relaxations for quantum correlations
            
            k_i = math.floor(self.relaxation_order - sp.degree(constraint.polynom)/2) 
            assert k_i >= 0, "Insufficient relaxation order to capture the constraint {constraint.polynom}"
            
            # TODO This is redundant work, does this matter?
            constraint_monomials = needed_monomials( \
                generate_monomials_commutative(self.objective.free_symbols, k_i), \
                self.substitution_rules\
            )

            self.constraint_moment_matrices.append( \
                create_constraint_matrix_commutative(constraint_monomials, constraint.polynom, self.substitution_rules))

    def add_constraints(self, constraints : List[Constraint]) -> None:
        for constraint in constraints:
            self.add_constraint(constraint)