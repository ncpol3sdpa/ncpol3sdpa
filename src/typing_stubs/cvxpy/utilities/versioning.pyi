from _typeshed import Incomplete

class Version:
    major: Incomplete
    minor: Incomplete
    micro: Incomplete
    v: Incomplete
    def __init__(self, v: str | tuple[int, int, int]) -> None: ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
