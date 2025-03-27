from __future__ import annotations
from sympy import Expr


class Constraint:
    def __init__(
        self, is_equality_constraint: bool, polynom: Expr, substitution: bool = False
    ) -> None:
        """
        is_equality_constraint : boolean indicating whether the constraint is >= or ==
        polynom : sympy polynom
        """
        self.is_equality_constraint: bool = (
            is_equality_constraint  # is the constraint an equality or not ?
        )
        self.polynom: Expr = polynom  # the constraint has the form p >= 0 or p = 0
        self.substitution: bool = (
            substitution  # do we use substitution technique for this constraint ?
        )

    @classmethod
    def EqualityConstraint(
        cls, polynom: Expr, substitution: bool = False
    ) -> Constraint:
        return cls(True, polynom, substitution)

    @classmethod
    def InequalityConstraint(
        cls, polynom: Expr, substitution: bool = False
    ) -> Constraint:
        return cls(False, polynom, substitution)
