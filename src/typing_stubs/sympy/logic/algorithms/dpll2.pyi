from _typeshed import Incomplete
from sympy.assumptions.cnf import EncodedCNF as EncodedCNF
from sympy.core.sorting import ordered as ordered
from sympy.logic.algorithms.lra_theory import LRASolver as LRASolver

def dpll_satisfiable(expr, all_models: bool = False, use_lra_theory: bool = False): ...

class SATSolver:
    var_settings: Incomplete
    heuristic: Incomplete
    is_unsatisfied: bool
    update_functions: Incomplete
    INTERVAL: Incomplete
    symbols: Incomplete
    heur_calculate: Incomplete
    heur_lit_assigned: Incomplete
    heur_lit_unset: Incomplete
    heur_clause_added: Incomplete
    add_learned_clause: Incomplete
    compute_conflict: Incomplete
    levels: Incomplete
    num_decisions: int
    num_learned_clauses: int
    original_num_clauses: Incomplete
    lra: Incomplete
    def __init__(self, clauses, variables, var_settings, symbols: Incomplete | None = None, heuristic: str = 'vsids', clause_learning: str = 'none', INTERVAL: int = 500, lra_theory: Incomplete | None = None) -> None: ...

class Level:
    decision: Incomplete
    var_settings: Incomplete
    flipped: Incomplete
    def __init__(self, decision, flipped: bool = False) -> None: ...
