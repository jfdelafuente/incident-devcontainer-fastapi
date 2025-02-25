# Developing in Python with Dev Containers

## Task 1. Project Setup

1. Open `WSL` and make sure you’re using `Ubuntu`
2. Press `Shift+Ctrl+P` and start typing dev, then select `Add Dev Container Configuration Files`.
3. Customisations
4. postCreateCommand

Make sure you have `Docker Desktop` running and press `Shift+Ctrl+P` and select `Reopen in Container`.

## Task 2. FastAPI project with Step Debugging

1. Install FastAPI and the Uvicorn ASGI server using pip:

```bash
pip install fastapi "uvicorn[standard]"
pip freeze > requirements.txt
```

2. Press `Shift+Ctrl+P` and start typing `debug` and select `Add Configuration > Python Debugger > FastAPI`. This will add a .vscode folder with a launch.json


## Task 3. Guide to TDD with pytest and FastAPI

1. Environment Files. Create a new file in .devcontainer called devcontainer.env

Add these two environment variables to this file:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONBUFFERED=1
```

To ensure these are created when we spin up our dev container, we need to inject this file into the dev container at runtime via our devcontainer.json file. Add the following runArgs line:

```json
{
 "name": "Python 3",
 "runArgs": ["--env-file",".devcontainer/devcontainer.env"],
 "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bullseye",
 "postCreateCommand": "bash .devcontainer/post-create.sh"
}
```

2. Project Restructure. Creamos un dir para el `api` y otro para los `tests`.

3. pytest Configuration. Add conftest.py file

4. Edit requirements-dev.txt and add these two packages: pytest y pytest-coverage

5. Now you can rebuild your container — press `Ctrl+Shift+P` and type rebuild and then select `Rebuild Container Without Cache`.

6. VSCode Test Suite Configuration. Click Configure `Python Tests > pytest > tests`.

7. Complete setup.cfg


## Task 4. Docker, Visual Studio Code and GitHub setup and integration

0. Before you begin, make sure you’re signed in to `GitHub` in a browser

1. Open the VSC Terminal and configure your default Git settings:

```bash
git config --global user.name "JFdelaFuente"
git config --global user.email josefcodelafuente@gmail.com
git config --global init.defaultBranch main
```

2. Git

```bash
git init
```

3. Let’s commit our changes to git using the Source Control panel in VSC.


