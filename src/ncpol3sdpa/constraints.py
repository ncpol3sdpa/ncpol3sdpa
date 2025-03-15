from __future__ import annotations
import sympy as sp

class Constraint:
    def __init__(
            self, 
            is_equality_constraint : bool, 
            polynom : sp.Poly, 
            substitution : bool = False
        ) -> None:
        """ 
        is_equality_constraint : boolean indicating whether the constraint is >= or ==
        polynom : sympy polynom
        """
        self.is_equality_constraint = is_equality_constraint  # is the constraint an equality or not ?
        self.polynom = polynom  # the constraint has the form p >= 0 or p = 0
        self.substitution = substitution  # do we use substitution technique for this constraint ?


    @classmethod
    def EqualityConstraint(
        cls, 
        polynom : sp.Poly,
        substitution : bool = False
    ) -> Constraint:
        return cls(True, polynom, substitution)
    
    @classmethod
    def InequalityConstraint(
        cls, 
        polynom : sp.Poly,
        substitution : bool = False
    ) -> Constraint:
        return cls(False, polynom, substitution)