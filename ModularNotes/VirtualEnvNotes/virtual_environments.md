# Python Virtual Environments: Complete Guide

## 1. Introduction

A **virtual environment** is an isolated Python environment that allows you to manage dependencies for a specific project without affecting other projects or the global Python installation. This is essential for reproducibility, avoiding conflicts, and following best practices in Python development.

---

## 2. Why Use Virtual Environments?

- **Isolation:** Each project has its own dependencies, independent of others.
- **Reproducibility:** Ensures consistent environments across machines and deployments.
- **Avoid Conflicts:** Prevents version clashes between packages required by different projects.
- **Safe Experimentation:** Test new packages or versions without risk to system Python or other projects.
- **Best Practice:** Recommended for all Python development.

---

## 3. Types of Virtual Environments

### 3.1. venv (Standard Library)
- Built-in since Python 3.3.
- Lightweight, no external dependencies.
- Command: `python -m venv venv`

### 3.2. virtualenv
- Third-party tool, supports older Python versions and more features.
- Can create environments for different Python versions.
- Command: `virtualenv venv`

### 3.3. conda Environments
- Provided by Anaconda/Miniconda.
- Manages both Python and non-Python dependencies (e.g., C libraries).
- Command: `conda create -n myenv python=3.11`

### 3.4. pipenv
- Combines virtual environment and dependency management.
- Uses `Pipfile` and `Pipfile.lock`.
- Command: `pipenv install requests`

### 3.5. Poetry
- Modern tool for dependency management and packaging.
- Handles virtual environments automatically.
- Command: `poetry shell`

### 3.6. PDM
- PEP 582 workflow, manages dependencies and environments.
- Command: `pdm venv create`

---

## 4. Creating and Managing Virtual Environments

### 4.1. Using venv

```sh
python -m venv venv
```
- Creates a `venv` directory with isolated Python binaries and libraries.

#### Activating the Environment
- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

#### Deactivating
- `deactivate`

#### Removing
- Delete the `venv` directory.

### 4.2. Using virtualenv

```sh
pip install virtualenv
virtualenv venv
```
- Same activation/deactivation as venv.

### 4.3. Using conda

```sh
conda create -n myenv python=3.11
conda activate myenv
conda deactivate
conda remove -n myenv --all
```

### 4.4. Using pipenv

```sh
pip install pipenv
pipenv install requests
pipenv shell
pipenv --rm
```

### 4.5. Using Poetry

```sh
pip install poetry
poetry shell
poetry add requests
poetry env remove python
```

### 4.6. Using PDM

```sh
pip install pdm
pdm venv create
pdm use -f venv
pdm venv remove
```

---

## 5. Practical Usage and Workflows

- **Per-Project Isolation:** Create a virtual environment in each project directory.
- **Requirements Management:** Use `requirements.txt`, `Pipfile`, or `pyproject.toml` to track dependencies.
- **Version Control:** Exclude the virtual environment directory (e.g., `venv/`) from git (`.gitignore`).
- **Reproducibility:** Share dependency files, not the environment itself.
- **Activation:** Always activate the environment before running or developing your project.
- **Deactivation:** Use `deactivate` (or tool-specific command) when done.

---

## 6. Advanced Topics

- **Multiple Python Versions:** Use `pyenv`, `conda`, or `virtualenv` to manage different Python versions.
- **Custom Environment Location:** Specify a path: `python -m venv /path/to/env`
- **Environment Variables:** Set project-specific variables in the environment.
- **Automated Activation:** Use tools like `direnv` or shell scripts for auto-activation.
- **System Site Packages:** Optionally allow access to global packages (not recommended): `python -m venv venv --system-site-packages`
- **Jupyter Integration:** Install `ipykernel` in the environment to use it in Jupyter Notebooks.

---

## 7. Best Practices

- Always use a virtual environment for every project.
- Never commit the environment directory to version control.
- Pin dependencies for reproducibility.
- Regularly update and audit dependencies.
- Document setup steps in your project README.
- Use modern tools (Poetry, pipenv, conda) for complex workflows.

---

## 8. Troubleshooting

- **Activation Fails:** Check your shell and permissions.
- **Wrong Python Version:** Specify the version when creating the environment.
- **Package Not Found:** Ensure the environment is activated.
- **Conflicting Packages:** Recreate the environment or use dependency management tools.
- **Environment Too Large:** Use lightweight tools or clean up unused packages.

---

## 9. Summary Table: Tools and Commands

| Tool        | Create           | Activate                | Deactivate | Remove                |
|-------------|------------------|-------------------------|------------|-----------------------|
| venv        | python -m venv venv | venv\Scripts\activate (Win) / source venv/bin/activate (Unix) | deactivate  | Delete venv dir        |
| virtualenv  | virtualenv venv  | Same as venv            | deactivate  | Delete venv dir        |
| conda       | conda create -n myenv python=3.11 | conda activate myenv         | conda deactivate | conda remove -n myenv --all |
| pipenv      | pipenv install   | pipenv shell            | exit/pipenv --rm | pipenv --rm           |
| poetry      | poetry shell     | poetry shell            | exit/poetry env remove | poetry env remove    |
| pdm         | pdm venv create  | pdm use -f venv         | deactivate  | pdm venv remove        |

---

## 10. References

- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [virtualenv docs](https://virtualenv.pypa.io/)
- [Conda docs](https://docs.conda.io/)
- [Pipenv docs](https://pipenv.pypa.io/)
- [Poetry docs](https://python-poetry.org/docs/)
- [PDM docs](https://pdm.fming.dev/)

---

*Next: Advanced and real-world examples will be added in the following step.*
