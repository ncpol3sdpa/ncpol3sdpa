import sympy as sp
from functools import cmp_to_key
from typing import List, Dict, Any

class Monomial:

    def __init__(self): ...

    def __add__(self, other): ...

    def simplify(self): ...

def list_increment(degrees : List[int], k : int) -> bool:
    """ increment l as a base k number. returns True if overflows, False otherwirse """
    
    for i,x in enumerate(degrees):
        if x < k - 1:
            degrees[i] += 1
            return False
        else:
            assert(x == k - 1)
            degrees[i] = 0
    return True

def generate_monomials_commutative(symbols : List[Any], relaxation_order : int) -> List[Any]:
    """ returns a list of all monomials that have degree less or equal to k"""
    current_degres = [0 for _ in symbols]
    res  = []
    

    while(True):

        expr = 1
        for i, symbol in enumerate(symbols):
            expr *= symbol**current_degres[i]
        if sp.total_degree(expr) <= relaxation_order:
            res.append(expr)

        if list_increment(current_degres, relaxation_order+1): 
            break
        
    return sorted(
        res, 
        key=cmp_to_key(lambda item1, item2: sp.total_degree(item1) - sp.total_degree(item2))
    )

def create_backward_dictionary(monomials: List[Any]) -> Dict[Any, int]:
    """from a list int -> monomal, create a backwards dictionary monomail -> int, that is the inverse.
        forall i in [| 0..len(monomials) |[, list[dictionary[i]] = i
        and
        forall monomial in monomials, dictionary[list[monomial]] = monomial"""
    res = {}
    for i, monomial in enumerate(monomials):
        res[monomial] = i
    return res
