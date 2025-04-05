from ..agca.extensions import FiniteExtension as FiniteExtension
from ..factortools import dup_factor_list as dup_factor_list
from ..polyroots import roots as roots
from ..polytools import Poly as Poly
from ..rootoftools import CRootOf as CRootOf
from .domainmatrix import DomainMatrix as DomainMatrix
from sympy.core.symbol import Dummy as Dummy

def dom_eigenvects(A, l=...): ...
def dom_eigenvects_to_sympy(rational_eigenvects, algebraic_eigenvects, Matrix, **kwargs): ...
