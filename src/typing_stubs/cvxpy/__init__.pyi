from _typeshed import Incomplete

from cvxpy.atoms.affine.binary_operators import matmul as matmul
from cvxpy.atoms.affine.binary_operators import multiply as multiply
from cvxpy.atoms.affine.binary_operators import outer as outer
from cvxpy.atoms.affine.binary_operators import scalar_product as scalar_product
from cvxpy.atoms.affine.binary_operators import vdot as vdot
from cvxpy.atoms.affine.bmat import bmat as bmat
from cvxpy.atoms.affine.broadcast_to import broadcast_to as broadcast_to
from cvxpy.atoms.affine.concatenate import concatenate as concatenate
from cvxpy.atoms.affine.conj import conj as conj
from cvxpy.atoms.affine.conv import conv as conv, convolve as convolve
from cvxpy.atoms.affine.cumsum import cumsum as cumsum
from cvxpy.atoms.affine.diag import diag as diag
from cvxpy.atoms.affine.diff import diff as diff
from cvxpy.atoms.affine.hstack import hstack as hstack
from cvxpy.atoms.affine.imag import imag as imag
from cvxpy.atoms.affine.kron import kron as kron
from cvxpy.atoms.affine.partial_trace import partial_trace as partial_trace
from cvxpy.atoms.affine.partial_transpose import partial_transpose as partial_transpose
from cvxpy.atoms.affine.promote import promote as promote
from cvxpy.atoms.affine.real import real as real
from cvxpy.atoms.affine.reshape import deep_flatten as deep_flatten, reshape as reshape
from cvxpy.atoms.affine.sum import sum as sum
from cvxpy.atoms.affine.trace import trace as trace
from cvxpy.atoms.affine.transpose import transpose as transpose
from cvxpy.atoms.affine.upper_tri import (
    upper_tri as upper_tri,
    vec_to_upper_tri as vec_to_upper_tri,
)
from cvxpy.atoms.affine.vec import vec as vec
from cvxpy.atoms.affine.vstack import vstack as vstack
from cvxpy.atoms.affine.wraps import (
    hermitian_wrap as hermitian_wrap,
    psd_wrap as psd_wrap,
    skew_symmetric_wrap as skew_symmetric_wrap,
    symmetric_wrap as symmetric_wrap,
)
from cvxpy.atoms.condition_number import condition_number as condition_number
from cvxpy.atoms.cummax import cummax as cummax
from cvxpy.atoms.cumprod import cumprod as cumprod
from cvxpy.atoms.cvar import cvar as cvar
from cvxpy.atoms.dist_ratio import dist_ratio as dist_ratio
from cvxpy.atoms.dotsort import dotsort as dotsort
from cvxpy.atoms.elementwise.abs import abs as abs
from cvxpy.atoms.elementwise.ceil import ceil as ceil, floor as floor
from cvxpy.atoms.elementwise.entr import entr as entr
from cvxpy.atoms.elementwise.exp import exp as exp
from cvxpy.atoms.elementwise.huber import huber as huber
from cvxpy.atoms.elementwise.inv_pos import inv_pos as inv_pos
from cvxpy.atoms.elementwise.kl_div import kl_div as kl_div
from cvxpy.atoms.elementwise.log import log as log
from cvxpy.atoms.elementwise.log1p import log1p as log1p
from cvxpy.atoms.elementwise.log_normcdf import log_normcdf as log_normcdf
from cvxpy.atoms.elementwise.loggamma import loggamma as loggamma
from cvxpy.atoms.elementwise.logistic import logistic as logistic
from cvxpy.atoms.elementwise.maximum import maximum as maximum
from cvxpy.atoms.elementwise.minimum import minimum as minimum
from cvxpy.atoms.elementwise.neg import neg as neg
from cvxpy.atoms.elementwise.pos import pos as pos
from cvxpy.atoms.elementwise.power import power as power
from cvxpy.atoms.elementwise.rel_entr import rel_entr as rel_entr
from cvxpy.atoms.elementwise.scalene import scalene as scalene
from cvxpy.atoms.elementwise.sqrt import sqrt as sqrt
from cvxpy.atoms.elementwise.square import square as square
from cvxpy.atoms.elementwise.xexp import xexp as xexp
from cvxpy.atoms.eye_minus_inv import (
    eye_minus_inv as eye_minus_inv,
    resolvent as resolvent,
)
from cvxpy.atoms.gen_lambda_max import gen_lambda_max as gen_lambda_max
from cvxpy.atoms.geo_mean import geo_mean as geo_mean
from cvxpy.atoms.gmatmul import gmatmul as gmatmul
from cvxpy.atoms.harmonic_mean import harmonic_mean as harmonic_mean
from cvxpy.atoms.inv_prod import inv_prod as inv_prod
from cvxpy.atoms.lambda_max import lambda_max as lambda_max
from cvxpy.atoms.lambda_min import lambda_min as lambda_min
from cvxpy.atoms.lambda_sum_largest import lambda_sum_largest as lambda_sum_largest
from cvxpy.atoms.lambda_sum_smallest import lambda_sum_smallest as lambda_sum_smallest
from cvxpy.atoms.length import length as length
from cvxpy.atoms.log_det import log_det as log_det
from cvxpy.atoms.log_sum_exp import log_sum_exp as log_sum_exp
from cvxpy.atoms.matrix_frac import MatrixFrac as MatrixFrac, matrix_frac as matrix_frac
from cvxpy.atoms.max import max as max
from cvxpy.atoms.min import min as min
from cvxpy.atoms.mixed_norm import mixed_norm as mixed_norm
from cvxpy.atoms.norm import norm as norm, norm2 as norm2
from cvxpy.atoms.norm1 import norm1 as norm1
from cvxpy.atoms.norm_inf import norm_inf as norm_inf
from cvxpy.atoms.norm_nuc import normNuc as normNuc
from cvxpy.atoms.one_minus_pos import (
    diff_pos as diff_pos,
    one_minus_pos as one_minus_pos,
)
from cvxpy.atoms.perspective import perspective as perspective
from cvxpy.atoms.pf_eigenvalue import pf_eigenvalue as pf_eigenvalue
from cvxpy.atoms.pnorm import Pnorm as Pnorm, pnorm as pnorm
from cvxpy.atoms.prod import Prod as Prod, prod as prod
from cvxpy.atoms.ptp import ptp as ptp
from cvxpy.atoms.quad_form import QuadForm as QuadForm, quad_form as quad_form
from cvxpy.atoms.quad_over_lin import quad_over_lin as quad_over_lin
from cvxpy.atoms.quantum_cond_entr import quantum_cond_entr as quantum_cond_entr
from cvxpy.atoms.quantum_rel_entr import quantum_rel_entr as quantum_rel_entr
from cvxpy.atoms.sigma_max import sigma_max as sigma_max
from cvxpy.atoms.sign import sign as sign
from cvxpy.atoms.stats import mean as mean, std as std, var as var
from cvxpy.atoms.sum_largest import sum_largest as sum_largest
from cvxpy.atoms.sum_smallest import sum_smallest as sum_smallest
from cvxpy.atoms.sum_squares import sum_squares as sum_squares
from cvxpy.atoms.total_variation import tv as tv
from cvxpy.atoms.tr_inv import tr_inv as tr_inv
from cvxpy.atoms.von_neumann_entr import von_neumann_entr as von_neumann_entr

from cvxpy.constraints import (
    Constraint as Constraint,
    Cone as Cone,
    PSD as PSD,
    SOC as SOC,
    NonPos as NonPos,
    NonNeg as NonNeg,
    Zero as Zero,
    PowCone3D as PowCone3D,
    PowConeND as PowConeND,
    ExpCone as ExpCone,
    OpRelEntrConeQuad as OpRelEntrConeQuad,
    RelEntrConeQuad as RelEntrConeQuad,
    FiniteSet as FiniteSet,
)
from cvxpy.error import (
    DCPError as DCPError,
    DGPError as DGPError,
    DPPError as DPPError,
    SolverError as SolverError,
    disable_warnings as disable_warnings,
    enable_warnings as enable_warnings,
    warnings_enabled as warnings_enabled,
)
from cvxpy.expressions.constants import (
    CallbackParam as CallbackParam,
    Constant as Constant,
    Parameter as Parameter,
)
from cvxpy.expressions.expression import Expression as Expression
from cvxpy.expressions.variable import Variable as Variable
from cvxpy.problems.objective import (
    Maximize as Maximize,
    Minimize as Minimize,
    Objective as Objective,
)
from cvxpy.problems.problem import Problem as Problem
from cvxpy.transforms import (
    linearize as linearize,
    partial_optimize as partial_optimize,
    suppfunc as suppfunc,
)
from cvxpy.reductions.solvers.defines import installed_solvers as installed_solvers
from cvxpy.settings import (
    CBC as CBC,
    CLARABEL as CLARABEL,
    COPT as COPT,
    CPLEX as CPLEX,
    CPP_CANON_BACKEND as CPP_CANON_BACKEND,
    CVXOPT as CVXOPT,
    DIFFCP as DIFFCP,
    ECOS as ECOS,
    ECOS_BB as ECOS_BB,
    GLOP as GLOP,
    GLPK as GLPK,
    GLPK_MI as GLPK_MI,
    GUROBI as GUROBI,
    INFEASIBLE as INFEASIBLE,
    INFEASIBLE_INACCURATE as INFEASIBLE_INACCURATE,
    MOSEK as MOSEK,
    NAG as NAG,
    OPTIMAL as OPTIMAL,
    OPTIMAL_INACCURATE as OPTIMAL_INACCURATE,
    OSQP as OSQP,
    DAQP as DAQP,
    PDLP as PDLP,
    PIQP as PIQP,
    PROXQP as PROXQP,
    ROBUST_KKTSOLVER as ROBUST_KKTSOLVER,
    RUST_CANON_BACKEND as RUST_CANON_BACKEND,
    SCIP as SCIP,
    SCIPY as SCIPY,
    SCIPY_CANON_BACKEND as SCIPY_CANON_BACKEND,
    SCS as SCS,
    SDPA as SDPA,
    SOLVER_ERROR as SOLVER_ERROR,
    UNBOUNDED as UNBOUNDED,
    UNBOUNDED_INACCURATE as UNBOUNDED_INACCURATE,
    USER_LIMIT as USER_LIMIT,
    XPRESS as XPRESS,
    HIGHS as HIGHS,
    get_num_threads as get_num_threads,
    set_num_threads as set_num_threads,
)

version: str
SOC_ATOMS: Incomplete
EXP_ATOMS: Incomplete
PSD_ATOMS: Incomplete
NONPOS_ATOMS: Incomplete
