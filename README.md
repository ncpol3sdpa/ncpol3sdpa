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

### Formatting

Then, you can check for formatting issues by executing the following command:


```bash
uvx ruff format
```