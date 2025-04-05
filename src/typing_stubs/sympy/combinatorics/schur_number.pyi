from sympy.core import S as S
from sympy.core.basic import Basic as Basic
from sympy.core.function import Function as Function
from sympy.core.numbers import Integer as Integer

class SchurNumber(Function):
    @classmethod
    def eval(cls, k): ...
    def lower_bound(self): ...

def schur_partition(n): ...
