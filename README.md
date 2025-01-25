# mu_pipelines_driver

## Features


## Tools

### (Lint)
```
pipenv run flake8
pipenv run mypy
pipenv run black .
pipenv run isort .

```

### (Unit Tests)
```
pipenv run pytest --cov --cov-fail-under=100
```

### Pre-Commit Hooks

#### Install the hook
```
pipenv run pre-commit install
```