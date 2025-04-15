from cvxpy.atoms.elementwise.power import power as power
from cvxpy.constraints.exponential import ExpCone as ExpCone
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dcp2cone.canonicalizers.power_canon import power_canon as power_canon

def xexp_canon(expr, args): ...
