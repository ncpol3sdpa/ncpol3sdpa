import sympy
from ncpol3sdpa import monomial

def calculate_number_from_list(l, k):
	res = 0
	base = 1
	for digit in l:
		res += digit * base
		base *= k
	return res

def list_increment_on_test_inputs(l, k):
	assert(isinstance(k,int))
	for digit in l:
		assert(isinstance(digit, int))
		assert(0 <= digit and digit < k)
	l2 = l.copy()
	overflow = monomial.list_increment(l2, k)
	if l == [k-1 for _ in l]:
		assert(overflow)
	else:
		assert(not overflow) 
		assert(calculate_number_from_list(l,k) +1 == calculate_number_from_list(l2, k))

def test_list_increment():
	list_increment_on_test_inputs([9,2,2,2,1,3,5], 10)
	list_increment_on_test_inputs([2,2,2,2,2], 10)
	list_increment_on_test_inputs([9,9,9,9], 10)

	# random tests TODO

def test_generate_monomials_commutative():
	x,y,z = sympy.symbols("x y z")

	assert([1] == monomial.generate_monomials_commutative([x], 0))
	assert([1] == monomial.generate_monomials_commutative([x, y], 0))
	assert([1] == monomial.generate_monomials_commutative([x, y, z], 0))

	assert([1, x, x**2] == monomial.generate_monomials_commutative([x], 2))

	xy1 = monomial.generate_monomials_commutative([x,y], 1)
	assert(len(xy1) == 3)
	assert(1 in xy1)
	assert(x in xy1)
	assert(y in xy1)

	xyz1 = monomial.generate_monomials_commutative([x,y,z], 1)
	assert(len(xyz1) == 4)
	assert(1 in xyz1)
	assert(x in xyz1)
	assert(y in xyz1)
	assert(z in xyz1)

	xy2 = monomial.generate_monomials_commutative([x,y], 2)
	assert(len(xy2) == 6)
	assert(1 in xy2)
	assert(x in xy2)
	assert(y in xy2)
	assert(y**2 in xy2)
	assert(x**2 in xy2)
	assert(x*y in xy2)
