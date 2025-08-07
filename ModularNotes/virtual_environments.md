# Python Virtual Environments: Complete Guide with Practical Examples

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

### 3.2. conda Environments

- Provided by Anaconda/Miniconda.
- Manages both Python and non-Python dependencies (e.g., C libraries).
- Command: `conda create -n myenv python=3.11`

### 3.3. pipenv

- Combines virtual environment and dependency management.
- Uses `Pipfile` and `Pipfile.lock`.
- Command: `pipenv install requests`

### 3.4. Poetry

- Modern tool for dependency management and packaging.
- Handles virtual environments automatically.
- Command: `poetry shell`

### 3.5. PDM

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

### 4.2. Using conda

```sh
conda create -n myenv python=3.11
conda activate myenv
conda deactivate
conda remove -n myenv --all
```

### 4.3. Using pipenv

```sh
pip install pipenv
pipenv install requests
pipenv shell
pipenv --rm
```

### 4.4. Using Poetry

```sh
pip install poetry
poetry shell
poetry add requests
poetry env remove python
```

### 4.5. Using PDM

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

- **Multiple Python Versions:** Use `pyenv`, `conda`, or `venv` to manage different Python versions.
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
| conda       | conda create -n myenv python=3.11 | conda activate myenv         | conda deactivate | conda remove -n myenv --all |
| pipenv      | pipenv install   | pipenv shell            | exit/pipenv --rm | pipenv --rm           |
| poetry      | poetry shell     | poetry shell            | exit/poetry env remove | poetry env remove    |
| pdm         | pdm venv create  | pdm use -f venv         | deactivate  | pdm venv remove        |

---

## 10. References

- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [Conda docs](https://docs.conda.io/)
- [Pipenv docs](https://pipenv.pypa.io/)
- [Poetry docs](https://python-poetry.org/docs/)
- [PDM docs](https://pdm.fming.dev/)

---

# Advanced & Real-World Examples

## 1. Creating and Activating a venv (Standard Library)

```sh
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

---

## 2. Installing Packages and Freezing Requirements

```sh
pip install requests flask
pip freeze > requirements.txt
```

---

## 3. Reproducing an Environment on Another Machine

```sh
python -m venv venv
# Activate as above
pip install -r requirements.txt
```

---

## 4. Managing Environments with conda

```sh
conda create -n dataenv python=3.10 numpy pandas
conda activate dataenv
conda list
conda deactivate
conda remove -n dataenv --all
```

---

## 5. Using pipenv for Dependency Management

```sh
pip install pipenv
pipenv install requests flask
pipenv shell
pipenv lock  # generates Pipfile.lock
pipenv --rm  # remove environment
```

---

## 6. Using Poetry for Modern Projects

```sh
pip install poetry
poetry new myproject
cd myproject
poetry add requests
poetry shell
poetry export -f requirements.txt --output requirements.txt
```

---

## 7. Using PDM for PEP 582 Workflow

```sh
pip install pdm
pdm init
pdm add requests
pdm venv create
pdm use -f venv
```

---

## 8. Jupyter Notebook Integration

```sh
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
# Now select 'Python (myenv)' in Jupyter
```

---

## 9. Auto-Activating Environments with direnv

1. Install [direnv](https://direnv.net/)
2. Add `.envrc` file to project:

   ```sh
   layout python3
   ```

3. Allow direnv: `direnv allow`

---

## 10. Cleaning Up Unused Environments

- **venv:** Delete the environment directory.
- **conda:** `conda env list` and `conda remove -n envname --all`
- **pipenv:** `pipenv --rm`
- **poetry:** `poetry env list` and `poetry env remove <env>`
- **pdm:** `pdm venv remove`

---

## 11. Troubleshooting Example: Fixing Activation Issues

- **Problem:** `activate` script not found or not executable.
- **Solution:**
  - Ensure the environment was created successfully.
  - Check your shell (e.g., PowerShell, bash) and use the correct activation command.
  - On Windows, try running `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell.

---

## 12. Best Practices in Action

- Always add `venv/` or equivalent to `.gitignore`:

  ```
  venv/
  .env/
  .venv/
  __pycache__/
  *.pyc
  ```

- Document environment setup in your `README.md`:

  ```md
  ## Setup
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

---

## 13. Using Multiple Python Versions with pyenv (Advanced)

```sh
# Install pyenv (see https://github.com/pyenv/pyenv)
pyenv install 3.8.12
pyenv install 3.11.4
pyenv virtualenv 3.8.12 myenv38
pyenv activate myenv38
```

---

## 14. Environment Variables for Project Configuration

```sh
# .env file (used by pipenv, dotenv, etc.)
SECRET_KEY=supersecret
DEBUG=True
```

---

*This guide covers all major tools, workflows, and practical examples for Python virtual environments in one place.*
