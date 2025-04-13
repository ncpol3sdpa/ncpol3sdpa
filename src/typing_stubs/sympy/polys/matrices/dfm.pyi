from ._dfm import DFM as DFM
from sympy.external.gmpy import GROUND_TYPES as GROUND_TYPES

class DFM_dummy:
    def __init__(*args, **kwargs) -> None: ...
DFM = DFM_dummy
