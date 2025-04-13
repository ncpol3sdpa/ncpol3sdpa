from ..predicates.matrices import ComplexElementsPredicate as ComplexElementsPredicate, DiagonalPredicate as DiagonalPredicate, FullRankPredicate as FullRankPredicate, IntegerElementsPredicate as IntegerElementsPredicate, InvertiblePredicate as InvertiblePredicate, LowerTriangularPredicate as LowerTriangularPredicate, OrthogonalPredicate as OrthogonalPredicate, PositiveDefinitePredicate as PositiveDefinitePredicate, RealElementsPredicate as RealElementsPredicate, SquarePredicate as SquarePredicate, SymmetricPredicate as SymmetricPredicate, UnitaryPredicate as UnitaryPredicate, UpperTriangularPredicate as UpperTriangularPredicate
from sympy.assumptions import Q as Q, ask as ask
from sympy.assumptions.handlers import test_closed_group as test_closed_group
from sympy.core import Basic as Basic
from sympy.core.logic import fuzzy_and as fuzzy_and
from sympy.logic.boolalg import conjuncts as conjuncts
from sympy.matrices import MatrixBase as MatrixBase
from sympy.matrices.expressions import BlockDiagMatrix as BlockDiagMatrix, BlockMatrix as BlockMatrix, Determinant as Determinant, DiagMatrix as DiagMatrix, DiagonalMatrix as DiagonalMatrix, HadamardProduct as HadamardProduct, Identity as Identity, Inverse as Inverse, MatAdd as MatAdd, MatMul as MatMul, MatPow as MatPow, MatrixExpr as MatrixExpr, MatrixSlice as MatrixSlice, MatrixSymbol as MatrixSymbol, OneMatrix as OneMatrix, Trace as Trace, Transpose as Transpose, ZeroMatrix as ZeroMatrix
from sympy.matrices.expressions.blockmatrix import reblock_2x2 as reblock_2x2
from sympy.matrices.expressions.factorizations import Factorization as Factorization
from sympy.matrices.expressions.fourier import DFT as DFT
from sympy.utilities.iterables import sift as sift

def _(expr, assumptions): ...
def BM_elements(predicate, expr, assumptions): ...
def MS_elements(predicate, expr, assumptions): ...
def MatMul_elements(matrix_predicate, scalar_predicate, expr, assumptions): ...
