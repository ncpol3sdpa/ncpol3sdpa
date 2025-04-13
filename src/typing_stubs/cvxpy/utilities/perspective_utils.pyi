from cvxpy import Variable as Variable
from cvxpy.constraints.constraint import Constraint as Constraint
from cvxpy.constraints.exponential import ExpCone as ExpCone
from cvxpy.constraints.nonpos import NonNeg as NonNeg
from cvxpy.constraints.power import PowCone3D as PowCone3D
from cvxpy.constraints.psd import PSD as PSD
from cvxpy.constraints.second_order import SOC as SOC
from cvxpy.constraints.zero import Zero as Zero

def form_cone_constraint(z: Variable, constraint: Constraint) -> Constraint: ...
