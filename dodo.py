import platform
import subprocess
from pathlib import Path

SEP = "&" if platform.system() == "Windows" else ";"
SELF_PATH = Path(__file__).parent.absolute()


def syscmd(string):
    subprocess.call(string, shell=True)
    return True


def task_format():
    """makes code organized and pretty"""
    nparts = len(SELF_PATH.parts)
    for filepath in SELF_PATH.glob("**/*.py"):
        if str(filepath).find("{{") != -1:
            continue
        yield {
            "name": "/".join(filepath.parts[nparts:]),
            "actions": [
                (
                    "autoflake -i --expand-star-imports"
                    + " --remove-all-unused-imports"
                    + " --remove-duplicate-keys --remove-unused-variables %s"
                    + " %s isort %s %s black --line-length 79 %s"
                )
                % (filepath, SEP, filepath, SEP, filepath)
            ],
            "file_dep": [filepath],
            "verbosity": 2,
        }


def task_pytest():
    """run pytests under tests folder"""
    return {"actions": [lambda: syscmd("pytest tests/")], "verbosity": 2}
