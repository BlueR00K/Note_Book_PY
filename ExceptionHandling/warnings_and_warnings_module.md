# Warnings and the warnings Module in Python

## 1. Syllabus

- Introduction to warnings in Python
- Why use warnings instead of exceptions?
- The `warnings` module overview
- Basic usage: issuing warnings
- Warning categories (UserWarning, DeprecationWarning, etc.)
- Filtering and controlling warnings
- Custom warning classes
- Best practices for using warnings
- Real-world scenarios and advanced usage
- Comparison with exceptions and logging
- Summary and key takeaways

---

## 2. Introduction

Warnings in Python are a way to alert users and developers about conditions in code that are not necessarily errors, but may require attention. Unlike exceptions, warnings do not stop program execution by default. The `warnings` module provides a flexible framework for issuing, filtering, and managing warnings in Python applications.

---

## 3. Why Use Warnings Instead of Exceptions?

- **Non-fatal issues:** Warnings are for situations that are not severe enough to justify stopping the program.
- **Deprecation:** Alert users that a feature will be removed in the future.
- **Bad practices:** Warn about usage that is discouraged but not strictly wrong.
- **Performance:** Warn about slow code paths or resource usage.
- **Transition:** Help migrate users to new APIs without breaking existing code.

---

## 4. The `warnings` Module Overview

The `warnings` module is part of Python's standard library. It provides functions to issue, filter, and control warnings.

### Importing the Module

```python
import warnings
```

---

## 5. Basic Usage: Issuing Warnings

You can issue a warning using `warnings.warn()`:

```python
import warnings

def old_function():
 warnings.warn("old_function() is deprecated", DeprecationWarning)
 print("Running old_function")

old_function()
```

By default, some warnings (like DeprecationWarning) may not be shown. You can change this behavior (see filtering below).

---

## 6. Warning Categories

Python defines several built-in warning categories:

- `UserWarning`: Generic user code warnings (default)
- `DeprecationWarning`: Feature will be removed in the future
- `SyntaxWarning`: Suspicious syntax
- `RuntimeWarning`: Runtime issues (e.g., numeric overflow)
- `FutureWarning`: Feature will change in the future
- `ImportWarning`: Import-related issues
- `ResourceWarning`: Resource usage (e.g., unclosed files)

You can also define your own warning classes by subclassing `Warning`.

---

## 7. Filtering and Controlling Warnings

You can control which warnings are shown, ignored, or turned into errors using filters.

### Show All Warnings

```python
import warnings
warnings.simplefilter("always")
```

### Ignore Warnings

```python
warnings.filterwarnings("ignore", category=DeprecationWarning)
```

### Turn Warnings into Errors

```python
warnings.filterwarnings("error", category=UserWarning)

try:
 warnings.warn("This is a user warning", UserWarning)
except UserWarning:
 print("Warning was raised as an error!")
```

### Resetting Warning Filters

```python
warnings.resetwarnings()
```

---

## 8. Custom Warning Classes

You can define your own warning types for more specific messages:

```python
class MyCustomWarning(Warning):
 pass

warnings.warn("This is a custom warning", MyCustomWarning)
```

---

## 9. Best Practices for Using Warnings

- Use warnings for non-fatal, informational, or transitional issues.
- Always provide a clear, actionable message.
- Use the appropriate warning category.
- Document warnings in your code and API docs.
- Avoid overusing warnings; too many can be ignored by users.
- Consider turning important warnings into errors during testing.

---

## 10. Real-World Scenarios and Examples

### 10.1. Deprecating a Function

```python
def old_api():
 warnings.warn("old_api() will be removed in v2.0", DeprecationWarning)
 # ...
```

### 10.2. Warning About Bad Input

```python
def process_value(x):
 if x < 0:
  warnings.warn("Negative value encountered", UserWarning)
 return abs(x)

process_value(-5)
```

### 10.3. Warning in a Library

```python
def connect_to_server(url):
 if not url.startswith("https://"):
  warnings.warn("Insecure connection: use HTTPS", RuntimeWarning)
 # ...
```

### 10.4. Custom Warning with Extra Context

```python
class DataWarning(Warning):
 def __init__(self, message, row):
  super().__init__(message)
  self.row = row

def check_row(row):
 if not row.get("id"):
  warnings.warn(DataWarning("Missing 'id' field", row))

check_row({"name": "Alice"})
```

---

## 11. Comparison with Exceptions and Logging

- **Warnings**: Non-fatal, informational, do not stop execution.
- **Exceptions**: Fatal (unless caught), used for errors.
- **Logging**: For recording events, errors, and warnings to files or consoles.

Use warnings when you want to alert but not interrupt, exceptions for errors, and logging for persistent records.

---

## 12. Summary and Key Takeaways

- Warnings are for non-fatal, informational, or transitional issues.
- Use the `warnings` module to issue, filter, and control warnings.
- Choose the right warning category and message.
- Document and test your warning usage.

---

---

## 13. Advanced Usage and Edge Cases

### 13.1. Custom Warning Filters

You can write custom filters to control how warnings are handled in different parts of your application.

```python
import warnings

# Only show warnings from a specific module
warnings.filterwarnings("always", module="^my_module$")

# Ignore warnings with a specific message
warnings.filterwarnings("ignore", message=".*deprecated.*")
```

### 13.2. Warnings in Packages and Libraries

If you are writing a library, use warnings to communicate with users without breaking their code.

```python
# In your library code
def new_feature():
  warnings.warn("This feature is experimental", UserWarning, stacklevel=2)

def deprecated_func():
  warnings.warn("deprecated_func() is deprecated", DeprecationWarning, stacklevel=2)
```

### 13.3. Logging Warnings

You can redirect warnings to the logging system for persistent records.

```python
import logging
import warnings

logging.basicConfig(level=logging.INFO)
def warning_to_log(message, category, filename, lineno, file=None, line=None):
  logging.warning(f"{filename}:{lineno}: {category.__name__}: {message}")

warnings.showwarning = warning_to_log
warnings.warn("This will be logged!", UserWarning)
```

### 13.4. Warnings in Async Code

Warnings work in async code just like in sync code, but be careful with filters in concurrent environments.

```python
import asyncio
import warnings

async def async_func():
  warnings.warn("Async warning!", RuntimeWarning)

asyncio.run(async_func())
```

### 13.5. Warnings in Testing

Testing frameworks like pytest can check for warnings:

```python
import warnings
import pytest

def test_warns():
  with pytest.warns(UserWarning):
    warnings.warn("Test warning!", UserWarning)
```

### 13.6. Suppressing Warnings Temporarily

Use `warnings.catch_warnings()` to suppress or control warnings in a specific block of code.

```python
import warnings

with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  warnings.warn("This will not be shown", UserWarning)
```

### 13.7. Custom Warning Formatting

You can customize how warnings are displayed by overriding `warnings.formatwarning`.

```python
import warnings

def custom_format(message, category, filename, lineno, line=None):
  return f"[CUSTOM WARNING] {filename}:{lineno}: {category.__name__}: {message}\n"

warnings.formatwarning = custom_format
warnings.warn("Custom formatted warning!", UserWarning)
```

### 13.8. Warnings in Jupyter Notebooks

Jupyter may suppress some warnings by default. Use `warnings.simplefilter('always')` to ensure they are shown.

```python
import warnings
warnings.simplefilter('always')
warnings.warn("This will show in Jupyter", UserWarning)
```

### 13.9. Anti-patterns and What to Avoid

- Overusing warnings for trivial issues
- Using warnings for fatal errors (use exceptions instead)
- Not documenting warnings in your API
- Ignoring important warnings in production

**Example:**

```python
# BAD: Using warnings for real errors
def divide(a, b):
  if b == 0:
    warnings.warn("Division by zero!", UserWarning)
    return None
  return a / b

# Better: raise an exception
def divide_strict(a, b):
  if b == 0:
    raise ZeroDivisionError("Division by zero!")
  return a / b
```

---

## 14. Real-World Patterns and Scenarios

### 14.1. Deprecating a Class or Method

```python
class OldClass:
  def __init__(self):
    warnings.warn("OldClass is deprecated", DeprecationWarning, stacklevel=2)

class NewClass:
  pass

obj = OldClass()
```

### 14.2. Warning About Resource Usage

```python
def open_file(filename):
  f = open(filename)
  warnings.warn("Remember to close the file!", ResourceWarning)
  return f

f = open_file("data.txt")
f.close()
```

### 14.3. Warning in Data Science Pipelines

```python
def normalize(data):
  if max(data) == 0:
    warnings.warn("All data is zero!", UserWarning)
  return [x / max(data) if max(data) else 0 for x in data]

normalize([0, 0, 0])
```

### 14.4. Warning in Configuration Files

```python
def load_config(cfg):
  if "debug" in cfg and cfg["debug"]:
    warnings.warn("Debug mode is enabled", UserWarning)
  # ...

load_config({"debug": True})
```

### 14.5. Warning in Package Initialization

```python
# __init__.py
import warnings
warnings.warn("This package is experimental", UserWarning)
```

---

## 15. Documenting and Testing Warnings

- Always document warnings in your API docs and docstrings.
- Use testing frameworks to ensure warnings are issued as expected.
- Consider using type hints and static analysis for reliability.

**Example docstring:**

```python
def old_func():
  """This function is deprecated.

  .. warning::
    This function will be removed in a future version.
  """
  warnings.warn("old_func() is deprecated", DeprecationWarning)
```

---

## 16. Summary and Final Thoughts

- Warnings are a flexible tool for non-fatal issues, transitions, and developer communication.
- Use the warnings module responsibly and document all warnings.
- Integrate warnings with logging, testing, and custom filters for professional results.

---
