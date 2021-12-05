import subprocess
from pathlib import Path

SELF_PATH = Path(__file__).parent.absolute()


def syscmd(string):
    subprocess.call(string, shell=True)
    return True


def task_format():
    """makes code organized and pretty"""
    nparts = len(SELF_PATH.parts)
    for filepath in SELF_PATH.glob("**/*.py"):
        yield {
            "name": "/".join(filepath.parts[nparts:]),
            "actions": [
                lambda: syscmd(
                    (
                        "autoflake -i -r --expand-star-imports"
                        " --remove-all-unused-imports --remove-duplicate-keys"
                        " --remove-unused-variables %s"
                    )
                    % filepath
                ),
                lambda: syscmd("isort %s" % filepath),
                lambda: syscmd("black --line-length 79 %s" % filepath),
            ],
            "file_dep": [filepath],
            "verbosity": 2,
        }


def task_pytest():
    """run pytests under tests folder"""
    return {"actions": [lambda: syscmd("pytest tests/")], "verbosity": 2}
