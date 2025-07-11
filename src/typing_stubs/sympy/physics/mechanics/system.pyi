from _typeshed import Incomplete
from sympy.physics.mechanics.method import _Methods

__all__ = ['SymbolicSystem', 'System']

class System(_Methods):
    def __init__(self, frame: Incomplete | None = None, fixed_point: Incomplete | None = None) -> None: ...
    @classmethod
    def from_newtonian(cls, newtonian): ...
    @property
    def fixed_point(self): ...
    @property
    def frame(self): ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def z(self): ...
    @property
    def bodies(self): ...
    @bodies.setter
    def bodies(self, bodies) -> None: ...
    @property
    def joints(self): ...
    @joints.setter
    def joints(self, joints) -> None: ...
    @property
    def loads(self): ...
    @loads.setter
    def loads(self, loads) -> None: ...
    @property
    def actuators(self): ...
    @actuators.setter
    def actuators(self, actuators) -> None: ...
    @property
    def q(self): ...
    @property
    def u(self): ...
    @property
    def q_ind(self): ...
    @q_ind.setter
    def q_ind(self, q_ind) -> None: ...
    @property
    def q_dep(self): ...
    @q_dep.setter
    def q_dep(self, q_dep) -> None: ...
    @property
    def u_ind(self): ...
    @u_ind.setter
    def u_ind(self, u_ind) -> None: ...
    @property
    def u_dep(self): ...
    @u_dep.setter
    def u_dep(self, u_dep) -> None: ...
    @property
    def u_aux(self): ...
    @u_aux.setter
    def u_aux(self, u_aux) -> None: ...
    @property
    def kdes(self): ...
    @kdes.setter
    def kdes(self, kdes) -> None: ...
    @property
    def holonomic_constraints(self): ...
    @holonomic_constraints.setter
    def holonomic_constraints(self, constraints) -> None: ...
    @property
    def nonholonomic_constraints(self): ...
    @nonholonomic_constraints.setter
    def nonholonomic_constraints(self, constraints) -> None: ...
    @property
    def velocity_constraints(self): ...
    @velocity_constraints.setter
    def velocity_constraints(self, constraints) -> None: ...
    @property
    def eom_method(self): ...
    def add_coordinates(self, *coordinates, independent: bool = True) -> None: ...
    def add_speeds(self, *speeds, independent: bool = True) -> None: ...
    def add_auxiliary_speeds(self, *speeds) -> None: ...
    def add_kdes(self, *kdes) -> None: ...
    def add_holonomic_constraints(self, *constraints) -> None: ...
    def add_nonholonomic_constraints(self, *constraints) -> None: ...
    def add_bodies(self, *bodies) -> None: ...
    def add_loads(self, *loads) -> None: ...
    def apply_uniform_gravity(self, acceleration) -> None: ...
    def add_actuators(self, *actuators) -> None: ...
    def add_joints(self, *joints) -> None: ...
    def get_body(self, name): ...
    def get_joint(self, name): ...
    def form_eoms(self, eom_method=..., **kwargs): ...
    def rhs(self, inv_method: Incomplete | None = None): ...
    @property
    def mass_matrix(self): ...
    @property
    def mass_matrix_full(self): ...
    @property
    def forcing(self): ...
    @property
    def forcing_full(self): ...
    def validate_system(self, eom_method=..., check_duplicates: bool = False) -> None: ...

class SymbolicSystem:
    output_eqns: Incomplete
    def __init__(self, coord_states, right_hand_side, speeds: Incomplete | None = None, mass_matrix: Incomplete | None = None, coordinate_derivatives: Incomplete | None = None, alg_con: Incomplete | None = None, output_eqns={}, coord_idxs: Incomplete | None = None, speed_idxs: Incomplete | None = None, bodies: Incomplete | None = None, loads: Incomplete | None = None) -> None: ...
    @property
    def coordinates(self): ...
    @property
    def speeds(self): ...
    @property
    def states(self): ...
    @property
    def alg_con(self): ...
    @property
    def dyn_implicit_mat(self): ...
    @property
    def dyn_implicit_rhs(self): ...
    @property
    def comb_implicit_mat(self): ...
    @property
    def comb_implicit_rhs(self): ...
    def compute_explicit_form(self) -> None: ...
    @property
    def comb_explicit_rhs(self): ...
    @property
    def kin_explicit_rhs(self): ...
    def dynamic_symbols(self): ...
    def constant_symbols(self): ...
    @property
    def bodies(self): ...
    @property
    def loads(self): ...
