from cvxpy.atoms.elementwise.abs import abs as abs
from cvxpy.atoms.elementwise.power import power as power
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.eliminate_pwl.canonicalizers.abs_canon import abs_canon as abs_canon
from cvxpy.reductions.qp2quad_form.canonicalizers.power_canon import power_canon as power_canon

def huber_canon(expr, args): ...
