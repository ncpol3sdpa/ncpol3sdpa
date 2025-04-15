# ncpol3sdpa

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

We use `ruff` to check for errors and formatting issues.

Then, you can check for errors by executing the following command:

```bash
uvx ruff check
```

### Type Checking

We use `mypy` to check for typing errors.

Then, you can check for typing errors by executing the following command:

```bash
uv run mypy my_module.py
```
Or, you can check for typing errors in all files by executing the following command:

```bash
uv run mypy my_folder
```

### Formatting

Then, you can check for formatting issues by executing the following command:


```bash
uvx ruff format
```

### Build Documentation

For the documentation, we use `sphinx`. You can install it by running the following command:

```bash
pip install sphinx
```

Then, you can build the documentation by executing the following command:

```bash
make html -C docs
make latexpdf -C docs
```

### Build Dependencies Graph

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

We use `pydeps` to build the dependencies graph of functions.

```bash
uv run pydeps src/ncpol3sdpa
````

### Pre-Commit

We use pre-commit hooks to ensure a automatically verify adherence to formatting, linting, typing and tests.To use pre-commit hooks you must install them like this:

```
uv sync # Make sure uv virtual environment is up to date
uv run pre-commit install --hook-type pre-commit --hook-type pre-push
```

You can run every hook with :

```
uv run pre-commit run --all-files && \
uv run pre-commit run --hook-stage pre-push
```

To learn more about the details of pre-commit, the documentation is here : https://pre-commit.com/
