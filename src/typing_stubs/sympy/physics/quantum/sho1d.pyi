from _typeshed import Incomplete
from sympy.core.numbers import I as I, Integer as Integer
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.physics.quantum.cartesian import Px as Px, X as X
from sympy.physics.quantum.constants import hbar as hbar
from sympy.physics.quantum.hilbert import ComplexSpace as ComplexSpace
from sympy.physics.quantum.matrixutils import matrix_zeros as matrix_zeros
from sympy.physics.quantum.operator import Operator as Operator
from sympy.physics.quantum.qexpr import QExpr as QExpr
from sympy.physics.quantum.state import Bra as Bra, Ket as Ket, State as State

class SHOOp(Operator): ...
class RaisingOp(SHOOp): ...
class LoweringOp(SHOOp): ...
class NumberOp(SHOOp): ...
class Hamiltonian(SHOOp): ...

class SHOState(State):
    @property
    def n(self): ...

class SHOKet(SHOState, Ket):
    @classmethod
    def dual_class(self): ...

class SHOBra(SHOState, Bra):
    @classmethod
    def dual_class(self): ...

ad: Incomplete
a: Incomplete
H: Incomplete
N: Incomplete
omega: Incomplete
m: Incomplete
