from typing import List

from sympy import Expr
import sympy

from ncpol3sdpa.solvers import AvailableSolvers, Solver, SolverRegistry
from ncpol3sdpa.resolution import (
    Rules,
    RulesCommutative,
    RulesNoncommutative,
    Constraint,
    create_AlgebraSDP,
    generate_needed_symbols,
)
from ncpol3sdpa.algebra_to_SDP import algebra_to_SDP


class Problem:
    """A class representing a polynomial optimization problem.

    This class allows the definition of polynomial optimization problems with various constraints
    and supports solving them using SDP relaxations via the Lasserre hierarchy.

    Examples
    --------
    >>> from sympy import symbols
    >>> from ncpol3sdpa import Problem, Constraint
    >>> x, y = symbols('x y')
    >>> problem = Problem(x**2 + y**2)  # Minimize x^2 + y^2
    >>> problem.add_constraint(Constraint.InequalityConstraint(x + y - 1))
    >>> problem.add_constraint(Constraint.EqualityConstraint(x - y))
    >>> result = problem.solve(relaxation_order=2)
    >>> print(result)  # Prints an upper bound on the optimal value of the objective function
    """

    def __init__(
        self,
        obj: sympy.Expr,
        is_commutative: bool = True,
        is_real: bool = True,
        commute_variables: List[List[Expr]] = [],
    ) -> None:
        """
        Initialize the Problem instance.

        Parameters
        ----------
        obj : sympy.Expr
            The objective function to be optimized.
        obj : sympy.Expr
            The objective function to be optimized.
        is_commutative : bool, optional
            Flag indicating if the variables in the problem are commutative.
            Default is True.
        is_real : bool, optional
            Flag indicating if the variables in the problem are real-valued.
            Default is True.

        Notes
        -----
        The problem is initialized with an empty list of constraints. Constraints
        can be added later using the `add_constraint` method.
        """
        self.constraints: List[Constraint] = []
        self.objective: Expr = obj
        self.is_commutative = is_commutative
        self.is_real = is_real
        self.rules: Rules = (
            RulesCommutative() if is_commutative else RulesNoncommutative()
        )
        self.commute_variables = commute_variables

    def add_rule(self, old: Expr, new: Expr) -> None:
        """
        Add a substitution rule to the problem.

        When this rule is added, all occurrences of the `old` monomial will be replaced by the `new` monomial
        during the moment matrix generation process. This is a variation of the constraint `old = new`.

        Parameters
        ----------
        old : sympy.Expr
            The monomial to be replaced.
        new : sympy.Expr
            The monomial to replace `old` with.

        Raises
        ------
        AssertionError
            If `old` or `new` are not monomials.

        Notes
        -----
        This method is a special case of constraint.
        """
        # TODO: assert that old and new are monomials
        self.rules.add_rule(old, new)

    def add_constraint(self, constraint: Constraint) -> None:
        """
        Add a constraint to the problem.

        This method appends the given constraint to the list of constraints in the problem.

        Parameters
        ----------
        constraint : Constraint
            The constraint object to be added to the problem.

        Examples
        --------
        >>> problem = Problem()
        >>> constraint = Constraint.InequalityConstraint(x + y - 1)
        >>> problem.add_constraint(constraint)
        """
        self.constraints.append(constraint)

    def add_constraints(self, constraints: List[Constraint]) -> None:
        """
        Add multiple constraints to the optimization problem.

        Parameters
        ----------
        constraints : List[Constraint]
            A list of constraints to be added to the problem.

        Examples
        --------
        >>> problem = Problem()
        >>> constraints = [Constraint.InequalityConstraint(x - 1), Constraint.EqualityConstraint(x*y - 2)]
        >>> problem.add_constraints(constraints)

        See Also
        --------
        add_constraint : Add a single constraint to the optimization problem.
        """
        for c in constraints:
            self.add_constraint(c)

    def solve(
        self,
        relaxation_order: int = 1,
        solver: Solver | AvailableSolvers = AvailableSolvers.CVXPY,
        verbose: bool = False,
    ) -> float:
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

        normal_constraints = self.constraints

        # 1. Build algebric formulation
        if verbose:
            print("Build the algebric formulation")

        all_constraint_polynomials = [c.polynomial for c in self.constraints] + [
            self.objective
        ]
        needed_symbols = self.commute_variables
        if not self.commute_variables:
            needed_symbols = [generate_needed_symbols(all_constraint_polynomials)]

        algebraSDP = create_AlgebraSDP(
            needed_symbols,  # type: ignore
            self.objective,
            relaxation_order,
            self.rules,
            self.is_commutative,
            self.is_real,
        )
        algebraSDP.add_constraints(normal_constraints)

        # 2. Translate to SDP
        if verbose:
            print("Translate to SDP")

        problemSDP = algebra_to_SDP(algebraSDP)
        if not self.is_real:
            problemSDP = problemSDP.complex_to_realSDP()

        # 3. Solve the SDP
        if verbose:
            print("Solve the SDP")
        if isinstance(solver, AvailableSolvers):
            return SolverRegistry.get_solver(solver).solve(problemSDP, verbose=verbose)
        elif isinstance(solver, Solver):
            return solver.solve(problemSDP, verbose=verbose)
        else:
            raise TypeError(
                f"Solver must be of type {Solver} or {AvailableSolvers}, not {type(solver)}"
            )
