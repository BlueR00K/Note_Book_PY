# Modular Programming in Python

## 1. Introduction

Modular programming is a software design technique that emphasizes separating a program into independent, reusable, and organized pieces called modules. In Python, modularity is achieved through files, packages, and the import system.

---

## 2. What is a Module?

### Example

```python
# my_utils.py
PI = 3.14159
def area_circle(r):
    return PI * r * r
```

---

## 2a. What is a Script?

- A **script** is a Python file intended to be executed directly (e.g., `python my_script.py`).
- Scripts often contain code that performs a task, runs a workflow, or acts as a command-line tool.
- Scripts may use the `if __name__ == "__main__":` idiom to separate runnable code from importable definitions.
- Scripts can import modules, but are not usually imported themselves.
- Good scripts are modular: they import and use reusable modules for logic.

### Example

```python
# my_script.py
from my_utils import area_circle
print("Area:", area_circle(5))
```

---

## 2b. Module vs. Script vs. Package vs. Library

| Term      | What is it? | Typical Use | Example |
|-----------|-------------|-------------|---------|
| Module    | Any `.py` file with code, functions, classes | Reusable code, logic | `math.py`, `my_utils.py` |
| Script    | `.py` file meant to be run directly | Automation, CLI, tasks | `run_analysis.py` |
| Package   | Directory with `__init__.py` and modules | Group related modules | `requests/`, `myapp/` |
| Library   | Collection of modules/packages for reuse | Provide features to other code | `numpy`, `pandas` |
| Framework | Large library with conventions, structure, and extensibility | Build apps, enforce patterns | `Django`, `Flask` |

---

## 2c. What is a Framework? (In Detail)

- A **framework** is a large, opinionated library that provides structure, conventions, and extensibility for building applications.
- Frameworks often include:
  - Project scaffolding (directory structure, config files)
  - Built-in modules for common tasks (routing, database, templates, etc.)
  - Extension/plugin systems
  - Inversion of control: the framework calls your code ("Don't call us, we'll call you")
- Frameworks enforce best practices and patterns, reducing boilerplate and decision fatigue.
- Examples: Django (web), Flask (micro web), FastAPI (web APIs), Pytest (testing), Click (CLI apps)
- Difference from library: You call a library, but a framework calls your code.

---

## 2d. The **init**.py File: Content and Suggestions

- `__init__.py` marks a directory as a Python package.
- Can be empty, but often used to:
  - Expose selected submodules or objects (via `__all__`)
  - Set up package-level variables or imports
  - Perform package initialization logic
  - Import submodules for easier access (e.g., `from .utils import *`)
- Good practices:
  - Keep it minimal—avoid heavy logic or side effects
  - Use `__all__` to control what is exported
  - Add docstrings to describe the package
  - Import only what is needed for the public API

### Example

```python
# __init__.py
"""My package for advanced math utilities."""
from .utils import area_circle, area_square
__all__ = ["area_circle", "area_square"]
```

---

---

## 3. Importing Modules

- Use `import module_name` to bring in a module.
- Use `from module_name import name` to import specific objects.
- Use `as` to alias modules or objects.
- Imports can be absolute or relative (within packages).

### Example

```python
import math
from my_utils import area_circle as area
print(area(5))
```

---

## 4. The Python Module Search Path

- Python searches for modules in:
  - The current directory
  - Directories in `sys.path`
  - Installed packages (site-packages)
- You can modify `sys.path` at runtime.

---

## 5. Packages and **init**.py

- A **package** is a directory containing an `__init__.py` file (can be empty) and other modules or subpackages.
- Packages allow for hierarchical structuring of modules.
- Submodules are accessed with dot notation: `package.submodule`.

### Example

```
my_package/
    __init__.py
    utils.py
    data/
        __init__.py
        loader.py
```

---

## 6. Absolute vs. Relative Imports

- **Absolute import**: `from my_package import utils`
- **Relative import**: `from . import utils`, `from ..data import loader`
- Relative imports only work within packages.

---

## 7. The `if __name__ == "__main__":` Idiom

- Code under this block runs only when the file is executed directly, not when imported.
- Useful for test code, scripts, or CLI entry points.

### Example

```python
def main():
    print("This runs as a script!")
if __name__ == "__main__":
    main()
```

---

## 8. Organizing Large Projects

- Use packages and subpackages to group related modules.
- Place reusable code in modules, not scripts.
- Use a clear directory structure and naming conventions.
- Separate code, tests, and data.

---

## 9. The `__all__` Variable

- Define `__all__` in a module to control what is imported with `from module import *`.
- Example: `__all__ = ["foo", "Bar"]`

---

## 10. Dynamic Imports

- Use `importlib` to import modules dynamically at runtime.
- Useful for plugins, extensibility, or loading user-specified modules.

### Example

```python
import importlib
mod = importlib.import_module('math')
print(mod.sqrt(16))
```

---

## 11. Module Caching and Reloading

- Imported modules are cached in `sys.modules`.
- Use `importlib.reload(module)` to reload a module (for development, not production).

---

## 12. Best Practices

- Keep modules small and focused.
- Avoid circular imports.
- Use explicit imports, not `import *`.
- Document modules and functions.
- Use packages for large projects.
- Test modules independently.

---

## 13. Real-World Use Cases

- Building libraries and frameworks
- Plugin systems
- Code sharing and reuse
- Clean separation of concerns
- Scalable, maintainable codebases

---

## Advanced & Real-World Examples

### 1. Building a Reusable Utility Module

Create a module for temperature conversion and use it in multiple scripts:

```python
# temp_utils.py
def c_to_f(c):
    return c * 9/5 + 32
def f_to_c(f):
    return (f - 32) * 5/9
```

```python
# weather_report.py
from temp_utils import c_to_f
print(f"20°C is {c_to_f(20)}°F")
```

---

### 2. Creating a Package with Submodules

Organize a math package with geometry and algebra submodules:

```
mathlib/
    __init__.py
    geometry.py
    algebra.py
```

```python
# mathlib/geometry.py
def area_triangle(b, h):
    return 0.5 * b * h
```

```python
# mathlib/algebra.py
def solve_linear(a, b):
    return -b / a
```

```python
# mathlib/__init__.py
from .geometry import area_triangle
from .algebra import solve_linear
__all__ = ["area_triangle", "solve_linear"]
```

```python
# main.py
from mathlib import area_triangle, solve_linear
print(area_triangle(10, 5))
print(solve_linear(2, -4))
```

---

### 3. Plugin System with Dynamic Imports

Load plugins at runtime using importlib:

```python
# plugins/hello.py
def run():
    print("Hello from plugin!")
```

```python
# main.py
import importlib
plugin_name = 'plugins.hello'
plugin = importlib.import_module(plugin_name)
plugin.run()
```

---

### 4. Avoiding Circular Imports

Refactor code to avoid circular dependencies:

```python
# a.py
# from b import func_b  # BAD: can cause circular import
def func_a():
    print("A")

# b.py
# from a import func_a  # BAD
def func_b():
    print("B")

# main.py
from a import func_a
from b import func_b
func_a()
func_b()
```

---

### 5. Fun: Modular Game Engine Skeleton

Design a simple, extensible game engine using packages and modules:

```
game/
    __init__.py
    engine.py
    entities.py
    plugins/
        __init__.py
        powerups.py
```

```python
# game/engine.py
def run():
    print("Game running!")
```

```python
# game/plugins/powerups.py
def activate():
    print("Power-up activated!")
```

```python
# main.py
from game.engine import run
from game.plugins import powerups
run()
powerups.activate()
```

---
