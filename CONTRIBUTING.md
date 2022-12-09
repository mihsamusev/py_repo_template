## Dev environment setup
Ready to contribute? Here’s how to set up pyswarms for local development.

Fork the repo on GitHub.

Clone your fork locally:

```bash
$ git clone git@github.com:your_name_here/pyswarms.git
```

Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

```bash
mkvirtualenv pyswarms
cd pyswarms/
python setup.py develop
```

Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```
Now you can make your changes locally.

When you’re done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox. In addition, ensure that your code is formatted using black:

```bash
flake8 pyswarms tests
black pyswarms tests
python setup.py test or py.test
tox
```

To get flake8, black, and tox, just pip install them into your virtualenv. If you wish, you can add pre-commit hooks for both flake8 and black to make all formatting easier.

Install pre-commit and the pre-commit hook from `.pre-commit-config.yaml`

```bash
pip install pre-commit
pre-commit install
```

Alternatively, trigger it on save using you favourite editor, here is an example config for VSCode
