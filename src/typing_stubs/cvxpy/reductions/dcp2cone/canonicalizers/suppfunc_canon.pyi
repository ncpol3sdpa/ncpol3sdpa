from cvxpy import SOC as SOC, Variable as Variable, hstack as hstack
from cvxpy.constraints.exponential import ExpCone as ExpCone
from cvxpy.reductions.solvers.conic_solvers.scs_conif import scs_psdvec_to_psdmat as scs_psdvec_to_psdmat

def suppfunc_canon(expr, args): ...
