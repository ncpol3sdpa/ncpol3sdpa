from typing import List, Dict, Any

from sympy import Expr
import sympy

from ncpol3sdpa.solvers import Solver, SolverList, SolverFactory
from ncpol3sdpa.resolution import (
    Rules,
    RulesCommutative,
    RulesNoncommutative,
    Constraint,
    create_AlgebraSDP,
    generate_needed_symbols,
)
from ncpol3sdpa.algebra_to_SDP import algebra_to_SDP
from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.sos import SosDecomposition, compute_sos_decomposition


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
        commute_variables: List[
            List[Expr]
        ] = [],  # if a variable commute with every variables,
        # use [x], not all_commutative_variables if you have to also use commute_variables
        more_monomials: List[Expr] = [],
        all_commute_variables: List[Expr] = [],  # Used only in the non-commutative case
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
        self.solution: Solution_SDP[Any] | None = None
        self.rules: Rules = (
            RulesCommutative() if is_commutative else RulesNoncommutative()
        )
        self.commute_variables = commute_variables
        self.more_monomials = more_monomials
        self.all_commute_variables = all_commute_variables

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
        solver: Solver | SolverList = SolverList.CVXPY,
        **solver_config: Dict[str, Any],
    ) -> float | None:
        """Solve the polynomial optimization problem using SDP relaxation.

        Args:
            relaxation_order (int): The order of relaxation in Lasserre hierarchy.
                Higher orders give better approximations but increase complexity.
                Defaults to 1.
            solver (Solver | SolverList): The solver to use for solving the SDP.
            solver_config (Dict[str, Any]): Additional configuration parameters for the solver.
                Like `verbose`, which controls the verbosity of the solver output.

        Returns:
            float: An upper bound on the optimal value of the objective function

        Example:
            >>> problem = Problem(x**2 + y**2)  # minimize x^2 + y^2
            >>> problem.add_constraint(Constraint(x**2 + y**2 - 1))  # subject to x^2 + y^2 >= 1
            >>> result = problem.solve(relaxation_order=2)
        """

        normal_constraints = self.constraints

        # 1. Build algebric formulation
        # if verbose:
        #     print("Build the algebric formulation")

        all_constraint_polynomials = [c.polynomial for c in self.constraints] + [
            self.objective
        ]
        needed_symbols = self.commute_variables
        if not self.commute_variables:
            needed_symbols = [generate_needed_symbols(all_constraint_polynomials)]  # type: ignore

        if self.all_commute_variables and not self.commute_variables:
            new_symbols = [[x] for x in self.all_commute_variables]
            temp = []
            for x in needed_symbols[0]:
                if x not in self.all_commute_variables:
                    temp.append(x)
            new_symbols.append(temp)
            needed_symbols = new_symbols

        algebraSDP = create_AlgebraSDP(
            needed_symbols,  # type: ignore
            self.objective,
            relaxation_order,
            self.rules,
            self.is_commutative,
            self.is_real,
            self.more_monomials,
        )
        self.algebraSDP = algebraSDP
        algebraSDP.add_constraints(normal_constraints)
        # print(algebraSDP.moment_matrix)

        # 2. Translate to SDP
        # if verbose:
        #     print("Translate to SDP")

        problemSDP = algebra_to_SDP(algebraSDP)
        if not self.is_real:
            problemSDP = problemSDP.complex_to_realSDP()
        # print(problemSDP)

        # 3. Solve the SDP
        if isinstance(solver, SolverList):
            solver = SolverFactory.create_solver(solver)
        if isinstance(solver, Solver):
            self.solution = solver.solve(problemSDP, **solver_config)
        else:
            raise TypeError(f"Solver must be of type {Solver}, not {type(solver)}")

        if self.solution is not None:
            return self.solution.primal_objective_value
        else:
            return None

    def solve_unchecked(
        self,
        relaxation_order: int = 1,
        solver: Solver | SolverList = SolverList.CVXPY,
    ) -> float:
        """Same as solve, but will raise an exception if there was no solution"""
        res = self.solve(relaxation_order=relaxation_order, solver=solver)
        assert res is not None, "Could not find solution"
        return res

    def compute_sos_decomposition(self) -> SosDecomposition:
        """Returns a Sum of Squares decomposition of (lambda - objective).
        See sos_duality_derivation.md for more details.
        The `solve` function must be called and must have succeeded before this function can be called.
        """

        assert self.solution is not None, (
            "Solution not found: `solve` was not called or a solution was not found"
        )
        assert self.algebraSDP is not None, "Could not find algebra"

        return compute_sos_decomposition(
            solution=self.solution, problem_algebra=self.algebraSDP
        )
