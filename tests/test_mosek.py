from mosek import *
from typing import Any

def func() -> Any:

    with Task() as task:                          # Create Task
        task.appendvars(1)                          # 1 variable x
        task.putcj(0, 1.0)                          # c_0 = 1.0
        task.putvarbound(0, boundkey.ra, 2.0, 3.0)  # 2.0 <= x <= 3.0
        task.putobjsense(objsense.minimize)         # minimize

        task.optimize()                           # Optimize

        return task.getxx(soltype.itr)               # Get solution
    

def test_func() -> None:
    assert (func() == 2 or func() == 2.0)


if __name__ == '__main__':
    print(f"x = {func()}")