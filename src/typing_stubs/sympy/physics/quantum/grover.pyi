from _typeshed import Incomplete
from sympy.core.basic import Atom
from sympy.physics.quantum.gate import Gate

__all__ = ['OracleGate', 'WGate', 'superposition_basis', 'grover_iteration', 'apply_grover']

def superposition_basis(nqubits): ...

class OracleGateFunction(Atom):
    def __new__(cls, function): ...
    def __call__(self, *args): ...

class OracleGate(Gate):
    gate_name: str
    gate_name_latex: str
    @property
    def search_function(self): ...
    @property
    def targets(self): ...

class WGate(Gate):
    gate_name: str
    gate_name_latex: str
    @property
    def targets(self): ...

def grover_iteration(qstate, oracle): ...
def apply_grover(oracle, nqubits, iterations: Incomplete | None = None): ...
