from _typeshed import Incomplete

class State:
    name: Incomplete
    transitions: Incomplete
    state_machine: Incomplete
    state_type: Incomplete
    rh_rule: Incomplete
    def __init__(self, name, state_machine, state_type: Incomplete | None = None, rh_rule: Incomplete | None = None) -> None: ...
    def add_transition(self, letter, state) -> None: ...

class StateMachine:
    name: Incomplete
    automaton_alphabet: Incomplete
    states: Incomplete
    def __init__(self, name, automaton_alphabet) -> None: ...
    def add_state(self, state_name, state_type: Incomplete | None = None, rh_rule: Incomplete | None = None) -> None: ...
