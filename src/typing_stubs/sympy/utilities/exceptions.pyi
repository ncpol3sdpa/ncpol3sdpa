from _typeshed import Incomplete
from collections.abc import Generator

class SymPyDeprecationWarning(DeprecationWarning):
    message: Incomplete
    deprecated_since_version: Incomplete
    active_deprecations_target: Incomplete
    full_message: Incomplete
    def __init__(self, message, *, deprecated_since_version, active_deprecations_target) -> None: ...
    def __eq__(self, other): ...
    def __reduce__(self): ...

def sympy_deprecation_warning(message, *, deprecated_since_version, active_deprecations_target, stacklevel: int = 3) -> None: ...
def ignore_warnings(warningcls) -> Generator[None]: ...
