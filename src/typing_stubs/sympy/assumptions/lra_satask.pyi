from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q
from sympy.assumptions.assume import AppliedPredicate as AppliedPredicate, global_assumptions as global_assumptions
from sympy.assumptions.cnf import CNF as CNF, EncodedCNF as EncodedCNF
from sympy.core.kind import NumberKind as NumberKind
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.logic.algorithms.lra_theory import ALLOWED_PRED as ALLOWED_PRED, UnhandledInput as UnhandledInput
from sympy.logic.inference import satisfiable as satisfiable
from sympy.matrices.kind import MatrixKind as MatrixKind

def lra_satask(proposition, assumptions: bool = True, context=...): ...

WHITE_LIST: Incomplete

def check_satisfiability(prop, _prop, factbase): ...

pred_to_pos_neg_zero: Incomplete

def get_all_pred_and_expr_from_enc_cnf(enc_cnf): ...
def extract_pred_from_old_assum(all_exprs): ...
