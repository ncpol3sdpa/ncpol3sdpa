from cvxpy.expressions.expression import Expression as Expression

def sum_signs(exprs: list['Expression']) -> tuple[bool, bool]: ...
def mul_sign(lh_expr: Expression, rh_expr: Expression) -> tuple[bool, bool]: ...
