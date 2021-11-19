### Quickstart:
    cookiecutter https://github.com/nicolasCavalcante/cookiecutter-general.git
Or:

    python -m cookiecutter https://github.com/nicolasCavalcante/cookiecutter-general.git

#### If you said "No" to "setup_project":

Create Git repository:

    git init
    git add *
    git commit -m 'Inital commit'

Install and launch enviroment:

    pipenv install --dev
    pipenv shell


Run tests and formating, [Doit]:

    doit



------------
## Features

* [Pipenv] for managing packages and virtualenvs in a modern way.
* Code quality: [black], [isort], and [autoflake] already installed.
* Modern CLI with [Typer].
* [Pytest] for testing.
* [Doit] for automation.
* [Mkdocs] (optional) for documentation.

## Directory structure

This is our your new project will look like:

    ├── .gitignore                <- GitHub's excellent Python .gitignore customized for this project
    ├── AUTHORS.md                <- Project Authors
    ├── dodo.py                   <- doit dodo script for linting and tests
    ├── LICENSE                   <- Your project's license.
    ├── Pipfile                   <- The Pipfile for reproducing the analysis environment
    ├── README.md                 <- The top-level README for developers using this project.
    ├── setup.py                  <- makes project pip installable (pip install -e .) so <repo_name> can be imported
    │
    ├── notebooks                 <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                the creator's initials, and a short `_` delimited description, e.g.
    │                                `01_cp_exploratory_data_analysis.ipynb`.
    │
    ├───tests                     <- All project tests
    │
    ├── docs                      <- MkDocs data files
    ├── mkdocs.yml                <- MkDocs config file
    │
    └───<repo_name>
        └───cli.py                <- Entry point, acessible by <repo_name> <args> using typer

#### References:
https://github.com/drivendata/cookiecutter-data-science

https://github.com/crmne/cookiecutter-modern-datascience

https://github.com/sourcery-ai/python-best-practices-cookiecutter

https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Pipenv]: https://pipenv.pypa.io/en/latest/
[black]: https://github.com/psf/black
[isort]: https://github.com/timothycrosley/isort
[autoflake]: https://github.com/myint/autoflake
[Pytest]: https://docs.pytest.org/en/latest/
[Typer]: https://typer.tiangolo.com/
[Doit]: https://pydoit.org/
[Mkdocs]: https://www.mkdocs.org/
