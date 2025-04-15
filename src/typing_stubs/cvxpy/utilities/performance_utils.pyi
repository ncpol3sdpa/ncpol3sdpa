from cvxpy.utilities import scopes as scopes
from typing import Callable, TypeVar

R = TypeVar('R')
T = TypeVar('T')

def lazyprop(func): ...
def compute_once(func: Callable[[T], R]) -> Callable[[T], R]: ...
