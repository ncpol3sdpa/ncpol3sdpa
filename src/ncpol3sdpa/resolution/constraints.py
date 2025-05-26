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
        self,
        constraint_type: ConstraintType,
        polynomial: Expr | Poly,
        substitution: bool = False,
    ) -> None:
        """
        constraint_type : ConstraintType
        polynomial : sympy polynomial
        """
        self.constraint_type: ConstraintType = constraint_type
        self.polynomial: Expr = (
            polynomial.as_expr()  # the constraint has the form p >= 0 or p = 0
        )
        self.substitution: bool = (
            substitution  # do we use substitution technique for this constraint ?
        )

    @classmethod
    def EqualityConstraint(
        cls, polynomial: Expr | Poly, substitution: bool = False
    ) -> Constraint:
        return cls._create(ConstraintType.EQUALITY, polynomial, substitution)

    @classmethod
    def InequalityConstraint(
        cls, polynomial: Expr, substitution: bool = False
    ) -> Constraint:
        return cls._create(ConstraintType.INEQUALITY, polynomial, substitution)

    @classmethod
    def LocalInequalityConstraint(
        cls, polynomial: Expr, substitution: bool = False
    ) -> Constraint:
        return cls._create(ConstraintType.LOCAL_INEQUALITY, polynomial, substitution)
