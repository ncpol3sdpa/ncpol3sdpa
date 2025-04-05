from _typeshed import Incomplete
from sympy.physics.quantum.gate import OneQubitGate

__all__ = ['CircuitPlot', 'circuit_plot', 'labeller', 'Mz', 'Mx', 'CreateOneQubitGate', 'CreateCGate']

class CircuitPlot:
    scale: float
    fontsize: float
    linewidth: float
    control_radius: float
    not_radius: float
    swap_delta: float
    labels: list[str]
    inits: dict[str, str]
    label_buffer: float
    circuit: Incomplete
    ngates: Incomplete
    nqubits: Incomplete
    def __init__(self, c, nqubits, **kwargs) -> None: ...
    def update(self, kwargs) -> None: ...
    def one_qubit_box(self, t, gate_idx, wire_idx) -> None: ...
    def two_qubit_box(self, t, gate_idx, wire_idx) -> None: ...
    def control_line(self, gate_idx, min_wire, max_wire) -> None: ...
    def control_point(self, gate_idx, wire_idx) -> None: ...
    def not_point(self, gate_idx, wire_idx) -> None: ...
    def swap_point(self, gate_idx, wire_idx) -> None: ...

def circuit_plot(c, nqubits, **kwargs): ...
def labeller(n, symbol: str = 'q'): ...

class Mz(OneQubitGate):
    measurement: bool
    gate_name: str
    gate_name_latex: str

class Mx(OneQubitGate):
    measurement: bool
    gate_name: str
    gate_name_latex: str

class CreateOneQubitGate(type):
    def __new__(mcl, name, latexname: Incomplete | None = None): ...

def CreateCGate(name, latexname: Incomplete | None = None): ...
