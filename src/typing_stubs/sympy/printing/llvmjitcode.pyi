from _typeshed import Incomplete
from sympy.core.singleton import S as S
from sympy.external import import_module as import_module
from sympy.printing.printer import Printer as Printer
from sympy.tensor.indexed import IndexedBase as IndexedBase
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on

llvmlite: Incomplete
ll: Incomplete
llvm: Incomplete
__doctest_requires__: Incomplete

class LLVMJitPrinter(Printer):
    func_arg_map: Incomplete
    fp_type: Incomplete
    module: Incomplete
    builder: Incomplete
    fn: Incomplete
    ext_fn: Incomplete
    tmp_var: Incomplete
    def __init__(self, module, builder, fn, *args, **kwargs) -> None: ...
    def emptyPrinter(self, expr) -> None: ...

class LLVMJitCallbackPrinter(LLVMJitPrinter):
    def __init__(self, *args, **kwargs) -> None: ...

exe_engines: Incomplete
link_names: Incomplete
current_link_suffix: int

class LLVMJitCode:
    signature: Incomplete
    fp_type: Incomplete
    module: Incomplete
    fn: Incomplete
    llvm_arg_types: Incomplete
    llvm_ret_type: Incomplete
    param_dict: Incomplete
    link_name: str
    def __init__(self, signature) -> None: ...

class LLVMJitCodeCallback(LLVMJitCode):
    def __init__(self, signature) -> None: ...

class CodeSignature:
    ret_type: Incomplete
    arg_ctypes: Incomplete
    input_arg: int
    ret_arg: Incomplete
    def __init__(self, ret_type) -> None: ...

def llvm_callable(args, expr, callback_type: Incomplete | None = None): ...
