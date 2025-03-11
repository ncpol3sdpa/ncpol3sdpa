# ncpol3sdpa

## Development

To develop this package, you need to install the `uv` package. You can do this by running the following command:

```bash
pip install uv
# or
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

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

We use `ruff` to check for errors and formatting issues. You can install `ruff` VSCode extension by following the instructions [here](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

Then, you can check for errors by executing the following command:

```bash
uvx ruff check
```

### Formatting

Then, you can check for formatting issues by executing the following command:


```bash
uvx ruff format
```