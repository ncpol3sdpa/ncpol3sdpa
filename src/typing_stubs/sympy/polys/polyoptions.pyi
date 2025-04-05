from _typeshed import Incomplete

__all__ = ['Options', 'Options']

class Option:
    option: str | None
    is_Flag: bool
    requires: list[str]
    excludes: list[str]
    after: list[str]
    before: list[str]
    @classmethod
    def default(cls) -> None: ...
    @classmethod
    def preprocess(cls, option) -> None: ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Flag(Option):
    is_Flag: bool

class BooleanOption(Option):
    @classmethod
    def preprocess(cls, value): ...

class OptionType(type):
    def __init__(cls, *args, **kwargs) -> None: ...

class Options(dict):
    __order__: Incomplete
    __options__: dict[str, type[Option]]
    def __init__(self, gens, args, flags: Incomplete | None = None, strict: bool = False) -> None: ...
    def clone(self, updates={}): ...
    def __setattr__(self, attr, value) -> None: ...
    @property
    def args(self): ...
    @property
    def options(self): ...
    @property
    def flags(self): ...

class Expand(BooleanOption, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...

class Gens(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, gens): ...

class Wrt(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def preprocess(cls, wrt): ...

class Sort(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, sort): ...

class Order(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, order): ...

class Field(BooleanOption, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete

class Greedy(BooleanOption, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete

class Composite(BooleanOption, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls) -> None: ...
    requires: list[str]
    excludes: Incomplete

class Domain(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete
    after: Incomplete
    @classmethod
    def preprocess(cls, domain): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Split(BooleanOption, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def postprocess(cls, options) -> None: ...

class Gaussian(BooleanOption, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def postprocess(cls, options) -> None: ...

class Extension(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def preprocess(cls, extension): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Modulus(Option, metaclass=OptionType):
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def preprocess(cls, modulus): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Symmetric(BooleanOption, metaclass=OptionType):
    option: str
    requires: Incomplete
    excludes: Incomplete

class Strict(BooleanOption, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...

class Auto(BooleanOption, Flag, metaclass=OptionType):
    option: str
    after: Incomplete
    @classmethod
    def default(cls): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Frac(BooleanOption, Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...

class Formal(BooleanOption, Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...

class Polys(BooleanOption, Flag, metaclass=OptionType):
    option: str

class Include(BooleanOption, Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...

class All(BooleanOption, Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...

class Gen(Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, gen): ...

class Series(BooleanOption, Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...

class Symbols(Flag, metaclass=OptionType):
    option: str
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, symbols): ...

class Method(Flag, metaclass=OptionType):
    option: str
    @classmethod
    def preprocess(cls, method): ...
