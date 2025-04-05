__all__ = ['_NamedMixin']

class _NamedMixin:
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, name: str) -> None: ...
