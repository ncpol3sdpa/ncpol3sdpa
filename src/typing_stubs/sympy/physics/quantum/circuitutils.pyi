from _typeshed import Incomplete

__all__ = ['kmp_table', 'find_subcircuit', 'replace_subcircuit', 'convert_to_symbolic_indices', 'convert_to_real_indices', 'random_reduce', 'random_insert']

def kmp_table(word): ...
def find_subcircuit(circuit, subcircuit, start: int = 0, end: int = 0): ...
def replace_subcircuit(circuit, subcircuit, replace: Incomplete | None = None, pos: int = 0): ...
def convert_to_symbolic_indices(seq, start: Incomplete | None = None, gen: Incomplete | None = None, qubit_map: Incomplete | None = None): ...
def convert_to_real_indices(seq, qubit_map): ...
def random_reduce(circuit, gate_ids, seed: Incomplete | None = None): ...
def random_insert(circuit, choices, seed: Incomplete | None = None): ...
