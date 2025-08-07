# Python Virtual Environments: Advanced & Real-World Examples

---

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

## 4. Using virtualenv for Custom Python Version

```sh
pip install virtualenv
virtualenv -p python3.9 venv39
venv39\Scripts\activate  # Windows
source venv39/bin/activate  # macOS/Linux
```

---

## 5. Managing Environments with conda

```sh
conda create -n dataenv python=3.10 numpy pandas
conda activate dataenv
conda list
conda deactivate
conda remove -n dataenv --all
```

---

## 6. Using pipenv for Dependency Management

```sh
pip install pipenv
pipenv install requests flask
pipenv shell
pipenv lock  # generates Pipfile.lock
pipenv --rm  # remove environment
```

---

## 7. Using Poetry for Modern Projects

```sh
pip install poetry
poetry new myproject
cd myproject
poetry add requests
poetry shell
poetry export -f requirements.txt --output requirements.txt
```

---

## 8. Using PDM for PEP 582 Workflow

```sh
pip install pdm
pdm init
pdm add requests
pdm venv create
pdm use -f venv
```

---

## 9. Jupyter Notebook Integration

```sh
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
# Now select 'Python (myenv)' in Jupyter
```

---

## 10. Auto-Activating Environments with direnv

1. Install [direnv](https://direnv.net/)
2. Add `.envrc` file to project:
   ```sh
   layout python3
   ```
3. Allow direnv: `direnv allow`

---

## 11. Cleaning Up Unused Environments

- **venv/virtualenv:** Delete the environment directory.
- **conda:** `conda env list` and `conda remove -n envname --all`
- **pipenv:** `pipenv --rm`
- **poetry:** `poetry env list` and `poetry env remove <env>`
- **pdm:** `pdm venv remove`

---

## 12. Troubleshooting Example: Fixing Activation Issues

- **Problem:** `activate` script not found or not executable.
- **Solution:**
  - Ensure the environment was created successfully.
  - Check your shell (e.g., PowerShell, bash) and use the correct activation command.
  - On Windows, try running `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell.

---

## 13. Best Practices in Action

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

## 14. Using Multiple Python Versions with pyenv (Advanced)

```sh
# Install pyenv (see https://github.com/pyenv/pyenv)
pyenv install 3.8.12
pyenv install 3.11.4
pyenv virtualenv 3.8.12 myenv38
pyenv activate myenv38
```

---

## 15. Environment Variables for Project Configuration

```sh
# .env file (used by pipenv, dotenv, etc.)
SECRET_KEY=supersecret
DEBUG=True
```

---

*These examples cover practical, advanced, and real-world usage of Python virtual environments across all major tools and workflows.*
