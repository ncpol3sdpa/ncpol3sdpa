from __future__ import annotations
from sympy import Expr, S, total_degree
import sympy
import numpy as np
from typing import List, Dict, Tuple, Any
from numpy.typing import NDArray
# from sympy.ntheory import generate

from ncpol3sdpa.rules import Rule, apply_rule_to_polynom
from ncpol3sdpa.momentmatrix import create_moment_matrix_cvxpy, create_constraints_matrix_cvxpy
from ncpol3sdpa.monomial import generate_monomials_commutative
from ncpol3sdpa.solver import Solver
from ncpol3sdpa.constraints import Constraint
import ncpol3sdpa.semidefinite_program_repr as sdp_repr
import ncpol3sdpa.momentmatrix as momentmatrix
from ncpol3sdpa.semidefinite_program_repr import ProblemSDP, MomentMatrixSDP

def polynomial_to_matrix(algebra : momentmatrix.AlgebraSDP, poly : sympy.Poly) -> NDArray[np.float64]:
    """Returns a symmetric A matrix such that poly = Tr(A.T @ G) where G is the moment matrix. In other
    words express poly as a linear combination of the coefficients of G. 
    Requires that all monomials of poly exist within the moment matrix: 
        poly.free_vars included in algebra.moment_matrix free_vars
        and deg(poly) <= 2*algebra.relaxation_order"""
    moment_matrix_size = len(algebra.moment_matrix)
    a_0 = np.zeros(shape = (moment_matrix_size, moment_matrix_size))
    for monomial, coef in poly.as_coefficients_dict().items():
        assert monomial in algebra.monomial_to_positions.keys()
        assert 0 < len(algebra.monomial_to_positions[monomial])
        # The 0 is arbitrary (?) could be any other element of the list. 
        # TODO/Idea What happens if we chose other than 0? at random?
        monomial_x, monomial_y = algebra.monomial_to_positions[monomial][0]

        # The matrices must be symmetric
        a_0[monomial_x][monomial_y] += 0.5*coef
        a_0[monomial_y][monomial_x] += 0.5*coef

    return a_0

def algebra_to_SDP_add_equality_constraint(
    problem: ProblemSDP, 
    algebra : momentmatrix.AlgebraSDP,
    eq_constraint : sympy.Poly
) -> None :
    implied_constraints = algebra.expand_eq_constraint(eq_constraint)
    for implied_constraint in implied_constraints:
        #constraint matrix
        a_0 = polynomial_to_matrix(algebra, implied_constraint)
        
        constraint = sdp_repr.EqConstraint([(problem.MOMENT_MATRIX_VAR_NUM, a_0)])
        problem.constraints.append(constraint)

def algebra_to_SDP_add_inequality_constraint(
    problem: ProblemSDP, 
    algebra : momentmatrix.AlgebraSDP,
    constraint_moment_matrix : List[List[sympy.Poly]]
) -> None :
    """Adds the translation of an inequality constraint"""
    constraint_matrix_size = len(constraint_moment_matrix)

    new_var = len(problem.variable_sizes)
    problem.variable_sizes.append(constraint_matrix_size)

    for i, row in enumerate(constraint_moment_matrix):
        for j, poly in enumerate(row):
            a_k = np.zeros(shape = (constraint_matrix_size, constraint_matrix_size))
            a_k[i][j] -= 0.5
            a_k[j][i] -= 0.5

            a_0 = polynomial_to_matrix(algebra, poly)
            constraint = sdp_repr.EqConstraint([(problem.MOMENT_MATRIX_VAR_NUM, a_0), (new_var, a_k)])
            problem.constraints.append(constraint)


def algebra_to_SDP(algebra : momentmatrix.AlgebraSDP) -> ProblemSDP:
    """Convert the algebraic representation to the numeric SDP representation"""
    
    moment_matrix_size = len(algebra.moment_matrix)

    # Convert objective
    objective = polynomial_to_matrix(algebra, algebra.objective)
    
    # Moment matrix
    equiv_classes : List[List[Tuple[int, int]]] = \
        list(algebra.monomial_to_positions.values())
    
    moment_matrix_repr = MomentMatrixSDP(moment_matrix_size, equiv_classes)
     
    result_SDP = ProblemSDP(moment_matrix_repr, objective)

    # Translate Equality constraints
    
    for eq_constraint in algebra.equality_constraints:
        algebra_to_SDP_add_equality_constraint(result_SDP, algebra, eq_constraint)

    # Translate Inequality constrains

    for constraint_matrix in algebra.constraint_moment_matrices:
        algebra_to_SDP_add_inequality_constraint(\
                    result_SDP, algebra, constraint_matrix)

    return result_SDP 


def polynom_linearized(
        variable_of_monomial : Dict[Any,Any],
        polynom : Expr,
        rules : Dict[Expr,Expr]
    ) -> Expr:
    """Return the linearized polynom"""
    # 2*X*Y -> 2 Y_(i,j)

    polynom = apply_rule_to_polynom(polynom, rules)
    dict_monoms : Dict[Any,Any]
    dict_monoms = polynom.expand().as_coefficients_dict()
    combination : Expr = S.Zero
    for key, value in dict_monoms.items():
        combination += value * variable_of_monomial[key]
    return combination


class Problem:
    def __init__(self, obj : sympy.Symbol) -> None:
        self.constraints : List[Constraint] = []
        self.objective : Expr = obj

    def add_constraint(self, constraint : Constraint) -> None:
        self.constraints.append(constraint)
    

    def solve(self, relaxation_order: int = 1) -> float:
        """Solve the polynomial optimization problem using SDP relaxation.

        Args:
            relaxation_order (int): The order of relaxation in Lasserre hierarchy.
                Higher orders give better approximations but increase complexity.
                Defaults to 1.

        Returns:
            float: An upper bound on the optimal value of the objective function

        Example:
            >>> problem = Problem(x**2 + y**2)  # minimize x^2 + y^2
            >>> problem.add_constraint(Constraint(x**2 + y**2 - 1))  # subject to x^2 + y^2 >= 1
            >>> result = problem.solve(relaxation_order=2)
        """

        # 0. Separate constraint types 
        rules = Rule.of_constraints([
            constraint 
            for constraint in self.constraints 
            if constraint.substitution
        ])

        normal_constraints = [
            constraint 
            for constraint in self.constraints 
            if not constraint.substitution
        ]

        # 1. Build algebraic formulation

        all_constraint_polynomials = [c.polynom for c in self.constraints] + [self.objective]
        needed_symbols = momentmatrix.generate_needed_symbols(all_constraint_polynomials) 
        algebra = momentmatrix.AlgebraSDP(needed_symbols, self.objective, relaxation_order, rules)
        algebra.add_constraints(normal_constraints)

        # 2. Translate to SDP

        problemSDP = algebra_to_SDP(algebra)

        # 3. Solve the SDP

        return Solver.solve_cvxpy(problemSDP)


    def solve_old(self, relaxation_order: int = 1) -> float:
        """Solve the polynomial optimization problem using SDP relaxation.

        This function implements the Lasserre hierarchy to solve polynomial optimization
        problems through the following steps:
        1. Generate substitution rules from equality constraints
        2. Generate monomials for the moment matrix
        3. Build the moment matrix
        4. Construct constraint matrices for both equality and inequality constraints
        5. Linearize objective function
        6. Solve the resulting SDP problem

        Args:
            relaxation_order (int): The order of relaxation in Lasserre hierarchy.
                Higher orders give better approximations but increase complexity.
                Defaults to 1.

        Returns:
            float: The optimal value of the objective function

        Example:
            >>> problem = Problem(x**2 + y**2)  # minimize x^2 + y^2
            >>> problem.add_constraint(Constraint(x**2 + y**2 - 1))  # subject to x^2 + y^2 >= 1
            >>> result = problem.solve(relaxation_order=2)
        """
        # Step 1: Handle substitution rules
        rules = Rule.of_constraints([
            constraint 
            for constraint in self.constraints 
            if constraint.substitution
        ])

        # Step 2: Generate monomials
        all_symbols = list(self.objective.free_symbols)
        all_monomials : List[Expr] = [
            monom
            for monom in generate_monomials_commutative(
                all_symbols, relaxation_order
            )
            if monom not in rules
        ]

        # Step 3: Build moment matrix
        moment_matrix, variable_of_monomial = create_moment_matrix_cvxpy(
            all_monomials, rules
        )

        # Step 4: Build constraint matrices
        # 4a. Equality constraints
        constraint_maricies_equal = [
            create_constraints_matrix_cvxpy(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(relaxation_order - (total_degree(constraint.polynom) / 2)),
                ),
                constraint.polynom,
                rules,
            )
            for constraint in self.constraints
            if constraint.is_equality_constraint and not constraint.substitution
        ]

        # 4b. Inequality (positivity) constraints
        constraint_maricies_positive = [
            create_constraints_matrix_cvxpy(
                variable_of_monomial,
                generate_monomials_commutative(
                    self.objective.free_symbols,
                    int(relaxation_order - (total_degree(self.constraints[i].polynom) / 2)),
                ),
                self.constraints[i].polynom,
                rules,
            )
            for i in range(len(self.constraints))
            if not self.constraints[i].is_equality_constraint
        ]

        # Step 5: Linearize objective function
        poly_obj = polynom_linearized(
            variable_of_monomial, 
            self.objective, 
            rules
        )

        # Step 6: Solve SDP
        return Solver.solve_cvxpy(
            poly_obj,
            len(moment_matrix),
            moment_matrix,
            constraint_maricies_positive,
            constraint_maricies_equal,
        )