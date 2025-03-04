
from monomial import *
from typing import List

# return a list of monomials without the monom that lead the equality rules 
# ex: needed_monomials([x, x**2], {x : ...}) = [x**2]
def needed_monomials(monomials, rules):
        needed_mono = [monomial for monomial in monomials if monomial not in rules.keys()]
        return needed_mono


def convert_polynome_to_list(P,k):     # P: polynome of the problem
     
     
     

def create_matrix(L):       # L list of all the monomials used in the moment matrix
    n = len(L)
    M = []
    for i in range (n):
        P = [0] * n
        M.append(P)   
        
    for i in range(n):
        for j in range(n):
            M[i][j] = L[i] * L[j]
    return M


     
class MomentMatrix:

    def __init__(self): ...


    def __mul__(self, other): ...

    def __repr__(self): ...

    def _method1(self): ...

    
