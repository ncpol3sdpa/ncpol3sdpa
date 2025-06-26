from __future__ import annotations
from enum import Enum, auto

from sympy import Expr, Poly

from .utils import NoPublicConstructor


class ConstraintType(Enum):
    """Enum class for specifying types of constraints in polynomial optimization problems.

    These constraint types help in properly formulating and solving polynomial optimization
    problems by distinguishing between different mathematical constraint forms.
    """

    EQUALITY = auto()
    """
    EQUALITY: Represents an equality constraint of the form:

    .. math::
        f(x) = 0
    """
    INEQUALITY = auto()
    """
    INEQUALITY: Represents an inequality constraint of the form:

    .. math::
       f(x) \\succcurlyeq 0

    In the commutative case, this means that the polynomial is non-negative.
    In the non-commutative case, this means that the polynomial is positive semi-definite.
    """
    LOCAL_INEQUALITY = auto()
    """
    LOCAL_INEQUALITY: Represents a local inequality constraint of the form:

    .. math::
       \\text{Tr}(\\rho f(x)) \\ge 0
    """


class Constraint(metaclass=NoPublicConstructor):
    def __init__(
        self, constraint_type: ConstraintType, polynomial: Expr | Poly
    ) -> None:
        """Initialize a Constraint object.

        Parameters
        ----------
        constraint_type : ConstraintType
            The type of constraint (EQUALITY, INEQUALITY, or LOCAL_INEQUALITY).
        polynomial : Expr | Poly
            The sympy expression or polynomial that defines the constraint.
            Will be converted to an expression if it's a polynomial.
        """
        self.constraint_type: ConstraintType = constraint_type
        self.polynomial: Expr = polynomial.as_expr()

    @classmethod
    def EqualityConstraint(cls, polynomial: Expr | Poly) -> Constraint:
        """Create an equality constraint

        Parameters
        ----------
        polynomial : Expr | Poly
            The sympy expression or polynomial that should equal zero.

        Returns
        -------
        Constraint
            A new equality constraint object.
        """
        return cls._create(ConstraintType.EQUALITY, polynomial)

    @classmethod
    def InequalityConstraint(cls, polynomial: Expr) -> Constraint:
        """Create an inequality constraint

        Parameters
        ----------
        polynomial : Expr
            The sympy expression that should be constrained.

        Returns
        -------
        Constraint
            A new inequality constraint object.

        Notes
        -----
        * In the commutative case: The constraint is `polynomial ≥ 0`
        * In the non-commutative case: The constraint is that `polynomial` is positive semi-definite
        """
        return cls._create(ConstraintType.INEQUALITY, polynomial)

    @classmethod
    def LocalInequalityConstraint(cls, polynomial: Expr) -> Constraint:
        """Create a local inequality constraint specific to the non-commutative case

        Parameters
        ----------
        polynomial : Expr
            The sympy expression that should be constrained.

        Returns
        -------
        Constraint
            A new local inequality constraint object.

        Notes
        -----
        * In the non-commutative case: The constraint is `Tr(ρ polynomial) ≥ 0`
        """
        return cls._create(ConstraintType.LOCAL_INEQUALITY, polynomial)
