# py_repo_template
Minimal github repository template configuration for python library development

CI Status: [![build](https://github.com/mihsamusev/py_repo_template/actions/workflows/ci.yaml/badge.svg)](https://github.com/mihsamusev/py_repo_template/actions/workflows/ci.yaml)

## Minimal installation
Required `pip >= 22.1.3` 
Using the modern way of [`pyproject.toml`](https://pip.pypa.io/en/latest/reference/build-system/pyproject-toml/?highlight=pyproject) to specify the dependencies + dev / test dependencies for the development and CI.

```bash
pip install .
# or dev
pip install .[dev]

# test its working
python -c "from goodstuff.module import Example"
```


## How about caching with poetry?
https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#caching-packages

## TODOS:
- [ ] examples of single branch development vs multiple branch development with CI
- [ ] add caching
- [ ] can extract names of tags like `release/<name>`