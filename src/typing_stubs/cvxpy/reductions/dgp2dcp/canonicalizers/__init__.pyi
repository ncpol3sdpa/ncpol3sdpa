from _typeshed import Incomplete
from cvxpy.atoms.affine.add_expr import AddExpression as AddExpression
from cvxpy.atoms.affine.binary_operators import DivExpression as DivExpression, MulExpression as MulExpression, multiply as multiply
from cvxpy.atoms.affine.sum import Sum as Sum
from cvxpy.atoms.affine.trace import trace as trace
from cvxpy.atoms.cumprod import cumprod as cumprod
from cvxpy.atoms.elementwise.exp import exp as exp
from cvxpy.atoms.elementwise.log import log as log
from cvxpy.atoms.elementwise.maximum import maximum as maximum
from cvxpy.atoms.elementwise.minimum import minimum as minimum
from cvxpy.atoms.elementwise.power import power as power
from cvxpy.atoms.elementwise.xexp import xexp as xexp
from cvxpy.atoms.eye_minus_inv import eye_minus_inv as eye_minus_inv
from cvxpy.atoms.geo_mean import geo_mean as geo_mean
from cvxpy.atoms.gmatmul import gmatmul as gmatmul
from cvxpy.atoms.max import max as max
from cvxpy.atoms.min import min as min
from cvxpy.atoms.norm1 import norm1 as norm1
from cvxpy.atoms.norm_inf import norm_inf as norm_inf
from cvxpy.atoms.one_minus_pos import one_minus_pos as one_minus_pos
from cvxpy.atoms.pf_eigenvalue import pf_eigenvalue as pf_eigenvalue
from cvxpy.atoms.pnorm import Pnorm as Pnorm
from cvxpy.atoms.prod import Prod as Prod
from cvxpy.atoms.quad_form import quad_form as quad_form
from cvxpy.atoms.quad_over_lin import quad_over_lin as quad_over_lin
from cvxpy.constraints.finite_set import FiniteSet as FiniteSet
from cvxpy.expressions.constants.constant import Constant as Constant
from cvxpy.expressions.constants.parameter import Parameter as Parameter
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.reductions.dgp2dcp.canonicalizers.add_canon import add_canon as add_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.constant_canon import constant_canon as constant_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.cumprod_canon import cumprod_canon as cumprod_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.div_canon import div_canon as div_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.exp_canon import exp_canon as exp_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.eye_minus_inv_canon import eye_minus_inv_canon as eye_minus_inv_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.finite_set_canon import finite_set_canon as finite_set_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.geo_mean_canon import geo_mean_canon as geo_mean_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.gmatmul_canon import gmatmul_canon as gmatmul_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.log_canon import log_canon as log_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.mul_canon import mul_canon as mul_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.mulexpression_canon import mulexpression_canon as mulexpression_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.norm1_canon import norm1_canon as norm1_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.norm_inf_canon import norm_inf_canon as norm_inf_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.one_minus_pos_canon import one_minus_pos_canon as one_minus_pos_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.pf_eigenvalue_canon import pf_eigenvalue_canon as pf_eigenvalue_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.pnorm_canon import pnorm_canon as pnorm_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.power_canon import power_canon as power_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.prod_canon import prod_canon as prod_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.quad_form_canon import quad_form_canon as quad_form_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.quad_over_lin_canon import quad_over_lin_canon as quad_over_lin_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.sum_canon import sum_canon as sum_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.trace_canon import trace_canon as trace_canon
from cvxpy.reductions.dgp2dcp.canonicalizers.xexp_canon import xexp_canon as xexp_canon

CANON_METHODS: Incomplete

class DgpCanonMethods(dict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __getitem__(self, key): ...
    def variable_canon(self, variable, args): ...
    def parameter_canon(self, parameter, args): ...
