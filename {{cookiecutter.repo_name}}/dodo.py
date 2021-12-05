import subprocess
from pathlib import Path

SELF_PATH = Path(__file__).parent.absolute()
NBS_PATH = SELF_PATH / "notebooks"
DOIT_CONFIG = {"default_tasks": ["format", "formatnb"]}


def syscmd(string):
    subprocess.call(string, shell=True)
    return True


def task_format():
    """makes code organized and pretty"""
    nparts = len(SELF_PATH.parts)
    for filepath in SELF_PATH.glob("**/*.py"):
        yield {
            "name":
            "/".join(filepath.parts[nparts:]),
            "actions": [
                lambda: syscmd(
                    ("autoflake -i -r --expand-star-imports"
                     " --remove-all-unused-imports --remove-duplicate-keys"
                     " --remove-unused-variables %s") % filepath),
                lambda: syscmd("isort %s" % filepath),
                lambda: syscmd("black --line-length 79 %s" % filepath)
            ],
            "file_dep": [filepath],
            "verbosity":
            2,
        }

{% if cookiecutter.add_notebook == 'Yes' -%}
def task_formatnb():
    """makes notebooks organized and pretty"""
    nparts = len(NBS_PATH.parts)
    for filepath in NBS_PATH.glob("*.ipynb"):
        filename = f'"{filepath.as_posix()}"'
        yield {
            "name": "/".join(filepath.parts[nparts:]),
            "actions": [
                lambda: syscmd(
                    (
                        "nbqa autoflake %s --in-place --remove-duplicate-keys "
                        "--remove-unused-variables --remove-all-unused-imports "
                        "--expand-star-imports"
                    )
                    % filename
                ),
                lambda: syscmd("nbqa isort %s" % filename),
                lambda: syscmd("nbqa black %s" % filename),
            ],
            "file_dep": [filepath.as_posix()],
            "verbosity": 2,
        }
{% endif %}

def task_pytest():
    """run pytests under tests folder"""
    return {"actions": [lambda: syscmd("pytest tests/")], "verbosity": 2}


def instalation_config(action_str):
    return {
        "actions": [lambda: syscmd(action_str)],
        "verbosity": 2,
    }


def task_devinstall():
    """install development packages"""
    return instalation_config('pip install -e "' + str(SELF_PATH) + '"')


def task_install():
    """install package"""
    return instalation_config('pip install "' + str(SELF_PATH) + '"')


def task_uninstall():
    """uninstall package"""
    return {
        "actions": [
            lambda: syscmd("pip uninstall {{cookiecutter.repo_name}} -y")
        ],
        "verbosity": 2,
    }
