from cvxpy.reductions.solution import Solution as Solution

FREE: str
ZERO: str
NONNEG: str
EXP: str
DUAL_EXP: str
SOC: str
PSD: str
POW3D: str
DUAL_POW3D: str

class Dualize:
    @staticmethod
    def apply(problem): ...
    @staticmethod
    def invert(solution, inv_data): ...

class Slacks:
    @staticmethod
    def apply(prob, affine): ...
    @staticmethod
    def invert(solution, inv_data): ...
