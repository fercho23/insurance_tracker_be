# README Insurance Tracker BE #

# General steps:
How to make the Backend work?

    1. Install Dependencies.

    2. Install pre-commit.

    3. Create file `.env` based on `.env.example`.
        - Remember to complete the file with the necessary information.

    4. Database options (Choose what is best for you):
        - Use the Sample Database as is.
        - Create Database, run migrations and run seed file.

    5. (Optional) Run Test Command

    6. Import and use Postman collection.

    7. Run application.
        - The default port is 5000, so the default URL is http://localhost:5000.

---
---

## 1 - Install Dependencies:
Below are some options on how to handle the process

### 1.1 - [Poetry](https://python-poetry.org/) option: (**RECOMMENDED**)
Poetry is a tool for dependency management and packaging in Python.
```bash
python -m pip install poetry
```

#### 1.1.1 - Install all dependecies with Poetry:
Inside the project where is the file "pyproject.toml"
```bash
poetry install
```

#### 1.1.2 - Add dependency:
```bash
poetry add dependency_name
```

#### 1.1.3 - Remove dependency:
```bash
poetry remove dependency_name
```

#### 1.1.4 - View outdated dependencies:
```bash
poetry show -o
```

#### 1.1.5 - Get requirements.txt:
```bash
poetry export --without-hashes --format=requirements.txt > requirements-pip.txt
```

### 1.2 - virtualenv option:

#### 1.2.1 - Install pip and dependecies:
```bash
python -m pip install --upgrade pip wheel setuptools virtualenv
```

#### 1.2.2 - Create virtualenv:
```bash
python -m virtualenv venv
```

#### 1.2.3 - Activate virtual env:
```bash
venv\Scripts\activate

source venv/bin/activate
```

#### 1.2.4 - Install: (Activated venv)
```bash
python -m pip install -r requirements-pip.txt
```

---

## 2 - Install [pre-commit](https://pre-commit.com/):
This automatically helps correct errors in file formatting.

```bash
python -m pip install pre-commit
```

Inside the project where is the file ".pre-commit-config.yaml"
```bash
pre-commit install
```

---

### 3 - Run the application
The default port is 5000, so the default URL is http://localhost:5000.
```bash
python run.py
```
```bash
poetry run run.py
```
---

### 4 - Run the Database commands

#### 4.1 - Create Initial databse
```bash
flask db init
```
```bash
poetry run flask db init
```

#### 4.2 - Create Migration
```bash
flask db migrate
```
```bash
poetry run flask db migrate
```

#### 4.3 - Run Migrations
```bash
flask db upgrade
```
```bash
poetry run flask db upgrade
```

#### 4.4 - Run seed.py to populate the Database
```bash
python seed.py
```
```bash
poetry run seed.py
```


---

### 5 - Run Tests:
All must be run in the root of the project.
#### 5.1 - All Tests:
```bash
pytest
```
```bash
poetry run pytest
```

#### 5.2 - By mark:
```bash
pytest -m user
```
```bash
poetry run pytest -m user
```

#### 5.3 - By folder:
```bash
pytest tests/test_user
```
```bash
poetry run pytest tests/test_user
```

#### 5.4 - By Fail Fast
```bash
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures
```
```bash
poetry run pytest --maxfail=2  # stop after two failures
poetry run pytest -x           # stop after first failure
```

#### 5.5 - Run with coverage:
#### 5.5.1 - Run with coverage and get command report:

```bash
pytest --cov
```
```bash
poetry run pytest --cov
```

---

## 6 - Others commands
### 6.1 - ruff: (style files)
```bash
python ruff .
```
```bash
poetry run ruff .
```

---

## 7 - Other configurations:

### 7.1 - env file:
Below each of the variables within the `.env` file.

| Variable name        | Variable Type | Description                                                              |
| :------------------- | :-----------: | :----------------------------------------------------------------------: |
| ENVIRONMENT          | String        | The type of environment, the recommended ones are: dev, staging, qa prod |
| SECRET_KEY           | String        | Secret key of the application                                            |
| ANTHROPIC_MODEL      | String        | The model used by Anthropic. Claude in this case.                        |
| ANTHROPIC_MAX_TOKENS | Number        | Anthropic max tokens. Default: 1000                                      |
| ANTHROPIC_SYSTEM     | String        | DB Host                                                                  |
| ANTHROPIC_API_KEY    | Number        | DB Port. Default: 5432                                                   |

### 7.2 - Postman:
Import the Postman collection from the `postman/` directory.


#### 7.3 - Anthropic:
The Anthropic Python library provides convenient access to the REST API using Claude.
Anthropic (https://www.anthropic.com/)
Anthropic docs (https://docs.anthropic.com/en/api/getting-started)


---

## 8 - Dependency Lists:
* [Anthropic](https://github.com/anthropics/anthropic-sdk-python)
* [flask](https://flask.palletsprojects.com/en/stable/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [flask-sqlalchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)
* [marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [environs](https://pypi.org/project/environs/)
* [Postman](https://www.postman.com/)
* [Pytest](https://docs.pytest.org/)
