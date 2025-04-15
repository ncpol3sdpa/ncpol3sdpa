import abc
from _typeshed import Incomplete

class ParamProb(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_mixed_integer(self) -> bool: ...
    @abc.abstractmethod
    def apply_parameters(self, id_to_param_value: Incomplete | None = None, zero_offset: bool = False, keep_zeros: bool = False): ...
