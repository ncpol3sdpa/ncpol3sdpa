# ncpol3sdpa

## Description

This package is a Python library for solving polynomial optimization problems using Lasserre hierarchical SDP relaxations.

We solve the following problem:  
$$\begin{align*}
\max_{x_1, \ldots, x_n} &\quad f(x_1, \ldots, x_n) \\
\text{s.t.} &\quad g_i(x_1, \ldots, x_n) \leq 0 \quad \forall i \in [1, C]
\end{align*}$$

where $f,g_i \in \mathbb K [x_1,\ldots,x_n]$.

This library is a successor to the [ncpol2sdpa library](https://ncpol2sdpa.readthedocs.io/en/stable/index.html).

### About

This package is developed by Alain, Thomas, Nazar, Mathis and Yann, under the supervision of Peter J Brown, at Telecom Paris, during the 2025 Artishow project.

The documentation is available at [ncpol3sdpa github](https://yruellan.github.io/ncpol3sdpa).

## Development

To develop this package, you need to install the [`uv` package manager](https://docs.astral.sh/uv/). 

We also use [`ruff`](https://docs.astral.sh/ruff/) and [`mypy`](https://mypy.readthedocs.io/en/stable/#) for error checking and formatting. These are installed by `uv sync` package.  
You can install the VSCode extension for `ruff` by following the instructions [here](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) and for `mypy` by following the instructions [here](https://marketplace.visualstudio.com/items?itemName=matangover.mypy).

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

We use pre-commit hooks to format the code, check for lint or type errors and run tests. To use pre-commit hooks you must install them like this:

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

For the documentation, we use `sphinx`. You can build the documentation by executing the following command in the `docs` folder:

```bash
make html -C docs
make latexpdf -C docs
```

### Build Dependencies Graph

<!-- 
#### With `tach`

We use `tach` to build the dependencies graph of modules.

```bash
uv run tach mod
uv run tach sync
``` 


```bash
uv run tach show --web
```
```bash
uv run tach show -o docs/graphs/tach_graph.dot
uv run dot -Tpdf docs/graphs/tach_graph.dot -o docs/graphs/tach_graph.pdf
``` 

#### With `pydeps`
-->

We use `pydeps` to build the dependencies graph of functions.

```bash
uv run pydeps src/ncpol3sdpa
```
