from cvxpy.atoms.affine.kron import kron as kron
from cvxpy.atoms.affine.partial_trace import partial_trace as partial_trace
from cvxpy.atoms.affine.wraps import hermitian_wrap as hermitian_wrap
from cvxpy.atoms.quantum_rel_entr import quantum_rel_entr as quantum_rel_entr
from cvxpy.expressions.expression import Expression as Expression

def quantum_cond_entr(rho: Expression, dim: list[int], sys: int | None = 0): ...
