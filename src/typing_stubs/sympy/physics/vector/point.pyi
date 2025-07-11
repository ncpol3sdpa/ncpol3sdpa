from _typeshed import Incomplete

__all__ = ['Point']

class Point:
    name: Incomplete
    def __init__(self, name) -> None: ...
    def a1pt_theory(self, otherpoint, outframe, interframe): ...
    def a2pt_theory(self, otherpoint, outframe, fixedframe): ...
    def acc(self, frame): ...
    def locatenew(self, name, value): ...
    def pos_from(self, otherpoint): ...
    def set_acc(self, frame, value) -> None: ...
    def set_pos(self, otherpoint, value) -> None: ...
    def set_vel(self, frame, value) -> None: ...
    def v1pt_theory(self, otherpoint, outframe, interframe): ...
    def v2pt_theory(self, otherpoint, outframe, fixedframe): ...
    def vel(self, frame): ...
    def partial_velocity(self, frame, *gen_speeds): ...
