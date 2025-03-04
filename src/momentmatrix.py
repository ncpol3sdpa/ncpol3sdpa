
from monomial import *
from typing import List

# return a list of monomials without the monom that lead the equality rules 
# ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
def needed_monomials(monomials, rules):
        needed_mono = [monomial for monomial in monomials if monomial not in rules.keys()]
        return needed_mono

class MomentMatrix:

    def __init__(self): ...

    def __mul__(self, other): ...

    def __repr__(self): ...

    def _method1(self): ...

    
