# ncpol3sdpa

## Description

This package is a Python library for solving polynomial optimization problems using Lassert hierarchical SDP relaxations. 

### Architecture

```
ncpol3sdpa
├─ __init__.py
├─ algebra_to_SDP.py         algebra_to_SDP
├─ funs.py
├─ main.py
├─ problem.py                Problem
├─ sos.py                    Sos
│
├─ resolution                The resolution of a problem
│  ├─ __init__.py            
│  ├─ algebra.py             AlgebraSDP 
│  ├─ constraints.py         Constraint
│  ├─ monomial.py
│  ├─ rules.py               Rule
│  └─ utils.py               generate_needed_symbols
│
├─ sdp_repr                  The structure of a problem
│  ├─ __init__.py
│  ├─ eq_constraint.py       EqConstraint
│  ├─ moment_matrix_SDP.py   MomentMatrixSDP
│  └─ problem_SDP.py         ProblemSDP
│
└─ solvers                   Implementation of the solvers
   ├─ __init__.py            AvailableSolvers
   ├─ cvxpy_solver.py
   ├─ mosek_solver.py
   └─ solver.py              Solver
```

## Development

To develop this package, you need to install the `uv` package. You can do this by running the following command:

```bash
pip install uv
# or
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

We also use `ruff` and `mypy` for error checking and formatting. These are installed as part of the `uv` package. You can install the VSCode extension for `ruff` by following the instructions [here](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) and for `mypy` by following the instructions [here](https://marketplace.visualstudio.com/items?itemName=matangover.mypy).

### Testing

You can run the tests by executing the following command:

```bash
uv run pytest
```

### Running scripts

You can run a file by executing the following command:

```bash
uv run hello.py
```

### Error Checking

We use `ruff` to check for errors and formatting issues. You can check for errors by executing the following command:

```bash
uvx ruff check
```

### Type Checking

We use `mypy` to check for typing errors. You can check for typing errors by executing the following command:

```bash
uv run mypy my_module.py
```
Or, you can check for typing errors in all files by executing the following command:

```bash
uv run mypy my_folder
```

### Formatting

Then, you can format the code by executing the following command:

```bash
uvx ruff format
```

### Pre-Commit

We use pre-commit hooks to ensure a automatically verify adherence to formatting, linting, typing and tests.To use pre-commit hooks you must install them like this:

```bash
uv sync
uv run pre-commit install --hook-type pre-commit --hook-type pre-push
```

You can run every hook with :

```bash
uv run pre-commit run --all-files && \
uv run pre-commit run --hook-stage pre-push
```

Pre-commit hooks are defined in the `.pre-commit-config.yaml` file. They are runs on every commit and every push. You can also run them manually with the command:

```bash
uv run pre-commit run --all-files && \
uv run pre-commit run --hook-stage pre-push
```

You can also ignore the pre-commit hooks for a specific commit by using the `--no-verify` option:

```bash
git commit -m "My commit message" --no-verify
```

To learn more about the details of pre-commit, the documentation is [here](https://pre-commit.com/).


## Documentation

### Build Documentation
<!-- You can install it by running the following command:

```bash
pip install sphinx
``` 
--> 

For the documentation, we use `sphinx`. You can build the documentation by executing the following command:

```bash
make html -C docs
make latexpdf -C docs
```

### Build Dependencies Graph

#### With `tach`

We use `tach` to build the dependencies graph of modules.

<!-- ```bash
uv run tach mod
uv run tach sync
``` -->

```bash
uv run tach show --web
```
```bash
uv run tach show -o docs/graphs/tach_graph.dot
uv run dot -Tpdf docs/graphs/tach_graph.dot -o docs/graphs/tach_graph.pdf
```

#### With `pydeps`

We use `pydeps` to build the dependencies graph of functions.

```bash
uv run pydeps src/ncpol3sdpa
```
