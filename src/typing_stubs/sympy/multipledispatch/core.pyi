from .dispatcher import Dispatcher as Dispatcher, MethodDispatcher as MethodDispatcher, ambiguity_warn as ambiguity_warn
from typing import Any

global_namespace: dict[str, Any]

def dispatch(*types, namespace=..., on_ambiguity=...): ...
def ismethod(func): ...
