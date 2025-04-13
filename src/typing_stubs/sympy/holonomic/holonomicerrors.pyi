from _typeshed import Incomplete

class BaseHolonomicError(Exception):
    def new(self, *args) -> None: ...

class NotPowerSeriesError(BaseHolonomicError):
    holonomic: Incomplete
    x0: Incomplete
    def __init__(self, holonomic, x0) -> None: ...

class NotHolonomicError(BaseHolonomicError):
    m: Incomplete
    def __init__(self, m) -> None: ...

class SingularityError(BaseHolonomicError):
    holonomic: Incomplete
    x0: Incomplete
    def __init__(self, holonomic, x0) -> None: ...

class NotHyperSeriesError(BaseHolonomicError):
    holonomic: Incomplete
    x0: Incomplete
    def __init__(self, holonomic, x0) -> None: ...
