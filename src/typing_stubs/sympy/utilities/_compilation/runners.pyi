from .util import CompileError as CompileError, find_binary_of_command as find_binary_of_command, unique_list as unique_list
from _typeshed import Incomplete
from typing import Callable

class CompilerRunner:
    environ_key_compiler: str
    environ_key_flags: str
    environ_key_ldflags: str
    compiler_dict: dict[str, str]
    standards: tuple[None | str, ...]
    std_formater: dict[str, Callable[[str | None], str]]
    compiler_name_vendor_mapping: dict[str, str]
    sources: Incomplete
    out: Incomplete
    flags: Incomplete
    cwd: Incomplete
    compiler_binary: Incomplete
    compiler_vendor: Incomplete
    compiler_name: Incomplete
    define: Incomplete
    undef: Incomplete
    include_dirs: Incomplete
    libraries: Incomplete
    library_dirs: Incomplete
    std: Incomplete
    run_linker: Incomplete
    linkline: Incomplete
    def __init__(self, sources, out, flags: Incomplete | None = None, run_linker: bool = True, compiler: Incomplete | None = None, cwd: str = '.', include_dirs: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, std: Incomplete | None = None, define: Incomplete | None = None, undef: Incomplete | None = None, strict_aliasing: Incomplete | None = None, preferred_vendor: Incomplete | None = None, linkline: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def find_compiler(cls, preferred_vendor: Incomplete | None = None): ...
    def cmd(self): ...
    cmd_outerr: Incomplete
    cmd_returncode: Incomplete
    def run(self): ...

class CCompilerRunner(CompilerRunner):
    environ_key_compiler: str
    environ_key_flags: str
    compiler_dict: Incomplete
    standards: Incomplete
    std_formater: Incomplete
    compiler_name_vendor_mapping: Incomplete

class CppCompilerRunner(CompilerRunner):
    environ_key_compiler: str
    environ_key_flags: str
    compiler_dict: Incomplete
    standards: Incomplete
    std_formater: Incomplete
    compiler_name_vendor_mapping: Incomplete

class FortranCompilerRunner(CompilerRunner):
    environ_key_compiler: str
    environ_key_flags: str
    standards: Incomplete
    std_formater: Incomplete
    compiler_dict: Incomplete
    compiler_name_vendor_mapping: Incomplete
