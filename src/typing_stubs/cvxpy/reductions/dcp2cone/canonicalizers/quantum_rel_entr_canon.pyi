from cvxpy import Variable as Variable
from cvxpy.atoms.affine.kron import kron as kron
from cvxpy.constraints import OpRelEntrConeQuad as OpRelEntrConeQuad

def quantum_rel_entr_canon(expr, args): ...
