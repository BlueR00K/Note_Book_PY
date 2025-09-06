# try/except in Python

## 1. Introduction

The `try/except` statement is the foundation of exception handling in Python. It allows you to catch and handle errors gracefully, preventing your program from crashing unexpectedly. This section covers the syntax, usage, and best practices for `try/except` blocks.

---

## 2. Basic Syntax

The simplest form of a `try/except` block looks like this:

```python
try:
    # Code that might raise an exception
    risky_operation()
except SomeException:
    # Code to handle the exception
    handle_error()
```

- The code inside the `try` block is executed first.
- If an exception occurs, Python looks for a matching `except` block.
- If a match is found, the code in the `except` block runs.
- If no exception occurs, the `except` block is skipped.

---

## 3. Catching Specific Exceptions

You can catch specific exception types to handle different errors differently:

```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

---

## 4. Catching Multiple Exceptions

You can catch multiple exceptions in a single `except` block by using a tuple:

```python
try:
    # ...
except (TypeError, ValueError) as e:
    print(f"Caught an error: {e}")
```

---

## 5. The Exception Object

You can access the exception object using `as`:

```python
try:
    1 / 0
except ZeroDivisionError as e:
    print(f"Exception details: {e}")
```

---

## 6. The Bare except

A bare `except:` catches all exceptions, but is discouraged because it can hide bugs and make debugging difficult.

```python
try:
    # ...
except:
    print("An error occurred.")
```

**Best practice:** Always catch specific exceptions.

---

## 7. The Flow of try/except

- If no exception occurs, the `except` block is skipped.
- If an exception occurs and is not handled, it propagates up the call stack.
- You can have multiple `except` blocks for different exception types.

---

## 8. Example: Handling File Errors

```python
try:
    with open('data.txt') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("No permission to read the file.")
```

---

## 9. Summary

The `try/except` statement is a powerful tool for writing robust Python code. Use it to handle errors gracefully and keep your programs running smoothly.

---

## 10. Advanced Usage of try/except

### 10.1. Using else and finally

The `else` block runs if no exception occurs. The `finally` block always runs, even if an exception is raised or the function returns early.

```python
try:
    print("Trying...")
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Success: {result}")
finally:
    print("Cleanup actions (always runs)")
```

### 10.2. Nested try/except Blocks

You can nest `try/except` blocks for fine-grained error handling.

```python
try:
    try:
        x = int("not a number")
    except ValueError:
        print("Inner: ValueError")
        raise
except Exception as e:
    print(f"Outer: {type(e).__name__}")
```

### 10.3. Re-raising Exceptions

You can re-raise an exception using `raise` without arguments.

```python
try:
    1 / 0
except ZeroDivisionError:
    print("Logging error...")
    raise  # Re-raises the current exception
```

### 10.4. Exception Chaining

Use `raise ... from ...` to chain exceptions and preserve the original traceback.

```python
def parse_number(s):
    try:
        return int(s)
    except ValueError as e:
        raise RuntimeError("Failed to parse number") from e

try:
    parse_number("abc")
except RuntimeError as e:
    print(f"Chained: {e}")
    print(f"Original: {e.__cause__}")
```

---

## 11. Best Practices

- Catch only exceptions you can handle meaningfully.
- Avoid bare `except:` unless absolutely necessary.
- Keep `try` blocks as small as possible.
- Use `finally` for cleanup (closing files, releasing resources).
- Log exceptions in production code.
- Document expected exceptions in your code.

---

## 12. Anti-patterns

- Swallowing exceptions (empty except block):

  ```python
  try:
      risky()
  except:
      pass  # BAD: hides all errors
  ```

- Using exceptions for normal control flow:

  ```python
  # BAD: don't use exceptions for logic you can check
  try:
      value = dct[key]
  except KeyError:
      value = None
  # Better:
  value = dct.get(key)
  ```

---

## 13. Real-World Scenarios

### 13.1. File Operations

```python
def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("No permission.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

### 13.2. Network Operations

```python
import requests

try:
    r = requests.get("https://example.com")
    r.raise_for_status()
except requests.RequestException as e:
    print(f"Network error: {e}")
```

### 13.3. User Input Validation

```python
def get_int():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Try again.")
```

---

## 14. Professional Tips

- Use custom exception classes for domain-specific errors.
- Use logging instead of print for error reporting.
- Test exception handling with unit tests.
- Use context managers for resource management.
- Always clean up resources, even on error.

---

This expanded section provides advanced usage, best practices, anti-patterns, and real-world scenarios for `try/except` in Python. For even more depth, consider adding sections on exception handling in async code, multi-threading, and integration with third-party libraries.
