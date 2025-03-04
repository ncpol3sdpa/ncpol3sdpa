import sympy as sp
from functools import cmp_to_key

class Monomial:

    def __init__(self): ...

    def __add__(self, other): ...

    def simplify(self): ...

def list_increment(l, k):
	""" increment l as a base k number. returns True if overflows, False otherwirse """
	for i in range(len(l)):
		if l[i] < k -1:
			l[i] += 1
			return False
		else:
			assert(l[i] == k - 1)
			l[i] = 0
	return True

def generate_monomials_commutative(symbols : list, k : int):
	""" returns a list of all monomials that have degree less than k"""
	current_degres = [0 for _ in symbols]
	n = len(symbols)
	res  = []
	
	continue_loop_flag = True
	while(continue_loop_flag):
		expr = 1
		for i, symbol in enumerate(symbols):
			expr *= symbol**current_degres[i]
		if sp.total_degree(expr) <= k:
			res.append(expr)

		continue_loop_flag = not list_increment(current_degres, k+1)
	# sort by degree
	return sorted(res, key=cmp_to_key(lambda item1, item2: sp.total_degree(item1) - sp.total_degree(item2)))
	