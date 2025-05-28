from __future__ import annotations
from enum import Enum, auto

from sympy import Expr, Poly

from .utils import NoPublicConstructor


class ConstraintType(Enum):
    EQUALITY = auto()  # Represents an equality constraint (p = 0)
    INEQUALITY = auto()  # Represents an inequality constraint (p >= 0)
    LOCAL_INEQUALITY = auto()  # Represents a local inequality constraint (p > 0)


class Constraint(metaclass=NoPublicConstructor):
    def __init__(
        self, constraint_type: ConstraintType, polynomial: Expr | Poly
    ) -> None:
        """
        constraint_type : ConstraintType
        polynomial : sympy polynomial
        """
        self.constraint_type: ConstraintType = constraint_type
        self.polynomial: Expr = (
            polynomial.as_expr()  # the constraint has the form p >= 0 or p = 0
        )

    @classmethod
    def EqualityConstraint(cls, polynomial: Expr | Poly) -> Constraint:
        """Equal to zero constraint: `polynomial = 0`"""
        return cls._create(ConstraintType.EQUALITY, polynomial)

    @classmethod
    def InequalityConstraint(cls, polynomial: Expr) -> Constraint:
        """Inequality constraint
        * In the commutative case: `polynomial >= 0`
        * In the non-commutative case: `polynomial` is positive semi-definite
        """
        return cls._create(ConstraintType.INEQUALITY, polynomial)

    @classmethod
    def LocalInequalityConstraint(cls, polynomial: Expr) -> Constraint:
        """Constraint specific to the non-commutative case
        * In the non-commutative case: `Trace(\\rho polynomial) >= 0`
        """
        return cls._create(ConstraintType.LOCAL_INEQUALITY, polynomial)
