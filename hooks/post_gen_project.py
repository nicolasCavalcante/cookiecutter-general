"""Script that runs after the project generation phase."""
import shutil
import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{cookiecutter.open_source_license}}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

if "{{cookiecutter.add_docs}}" == "No":
    shutil.rmtree(PROJECT_DIRECTORY / "docs")
    (PROJECT_DIRECTORY / "mkdocs.yml").unlink()

if "{{cookiecutter.setup_project}}" == "Yes - select this":
    subprocess.call(["git", "init"])
    subprocess.call(["pipenv", "install", "--dev", "--skip-lock"])
    subprocess.call(["pipenv", "run", "pre-commit", "install"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(["pipenv", "run", "pre-commit", "run", "--all-files"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(["pipenv", "run", "git", "commit", "-m", "Initial commit"])
    subprocess.call(["pipenv", "shell"])
