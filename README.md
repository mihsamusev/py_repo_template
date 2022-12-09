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
```
https://betterprogramming.pub/a-pyproject-toml-developers-cheat-sheet-5782801fb3ed
https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/
Adding tools to the pyproject.toml
- flake8 https://pypi.org/project/Flake8-pyproject/
- black
    - https://github.com/ljvmiranda921/pyswarms/blob/master/pyproject.toml
    - https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#where-black-looks-for-the-file
    - https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#where-black-looks-for-the-file

## CI pipeline
https://github.com/pypa/sampleproject/blob/main/pyproject.toml

https://tox.wiki/en/latest/user_guide.html

Tox as a pre-commit hook to combine the `black`,`flake8`,`test` and `coverage` in the same way as CI would?
https://github.com/pypa/sampleproject/blob/main/tox.ini

packaging for pypi?