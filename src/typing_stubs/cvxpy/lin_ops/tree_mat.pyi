def mul(lin_op, val_dict, is_abs: bool = False): ...
def tmul(lin_op, value, is_abs: bool = False): ...
def sum_dicts(dicts): ...
def op_mul(lin_op, args): ...
def op_abs_mul(lin_op, args): ...
def op_tmul(lin_op, value): ...
def op_abs_tmul(lin_op, value): ...
def conv_mul(lin_op, rh_val, transpose: bool = False, is_abs: bool = False): ...
def get_constant(lin_op): ...
def get_constr_constant(constraints): ...
def prune_constants(constraints): ...
def prune_expr(lin_op) -> bool: ...
