from __future__ import annotations
from sympy import Expr


class Constraint:
    def __init__(
        self, is_equality_constraint: bool, polynomial: Expr, substitution: bool = False
    ) -> None:
        """
        is_equality_constraint : boolean indicating whether the constraint is >= or ==
        polynomial : sympy polynomial
        """
        self.is_equality_constraint: bool = (
            is_equality_constraint  # is the constraint an equality or not ?
        )
        self.polynomial: Expr = polynomial  # the constraint has the form p >= 0 or p = 0
        self.substitution: bool = (
            substitution  # do we use substitution technique for this constraint ?
        )

    @classmethod
    def EqualityConstraint(
        cls, polynomial: Expr, substitution: bool = False
    ) -> Constraint:
        return cls(True, polynomial, substitution)

    @classmethod
    def InequalityConstraint(
        cls, polynomial: Expr, substitution: bool = False
    ) -> Constraint:
        return cls(False, polynomial, substitution)
