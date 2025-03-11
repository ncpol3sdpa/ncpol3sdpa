

class Constraint:
    def __init__(self, equal_constraint, polynom):
    	""" 
    	equal_constraint : boolean indicating whether the constraint is >= or ==
    	polynom : sympy polynom
    	"""

        self.equal_constraint = equal_constraint  # is the constraint an equality or not ?
        self.polynom = polynom  # the constraint has the form p >= 0 or p = 0
        
        
