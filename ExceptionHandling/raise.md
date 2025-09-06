# The raise Statement in Python

## 1. Syllabus

- Introduction to the raise statement
- Syntax and usage
- Raising built-in exceptions
- Raising custom exceptions
- Re-raising exceptions
- Exception chaining with raise ... from ...
- Use cases and motivations
- Best practices and common pitfalls
- Real-world scenarios
- Advanced usage (dynamic exception creation, context, etc.)
- Comparison with other languages
- Summary and key takeaways

---

## 2. Introduction

The `raise` statement in Python is used to trigger exceptions intentionally. It is a fundamental tool for error signaling, custom error handling, and enforcing program correctness. Understanding how to use `raise` effectively is essential for writing robust and professional Python code.

---

## 3. Why Use raise?

### Motivations

- **Signal errors:** When your code detects an invalid state or input, you can use `raise` to signal an error to the caller.
- **Enforce contracts:** Use `raise` to enforce preconditions, postconditions, and invariants in your functions and classes.
- **Custom error handling:** Create and raise your own exception types to provide meaningful error messages and control program flow.
- **Propagate errors:** Re-raise exceptions to escalate errors up the call stack for centralized handling.

### Historical Context

The concept of raising exceptions is present in many programming languages (e.g., Java, C++, Ruby). Python's `raise` statement is inspired by these languages but is designed to be simple and readable.

---

## 4. Foundational Concepts

### What is an Exception?

An exception is an object that represents an error or unexpected event. When an exception is raised, Python stops normal execution and looks for a handler.

### Exception Hierarchy

All exceptions inherit from `BaseException`. Most user-defined and built-in exceptions inherit from `Exception`.

```python
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
   ├── ValueError
   ├── TypeError
   ├── RuntimeError
   └── ...
```

### Raising vs. Handling

- **Raising:** Use `raise` to signal an error.
- **Handling:** Use `try/except` to catch and respond to errors.

---

## 5. When Should You Use raise?

### Common Use Cases

- Input validation (e.g., raise ValueError if input is invalid)
- Enforcing business rules (e.g., raise PermissionError if user lacks access)
- Stopping execution in critical failures
- Creating APIs that communicate errors to callers
- Wrapping lower-level exceptions with more meaningful messages

### Example: Input Validation

```python
def set_age(age):
 if age < 0:
  raise ValueError("Age cannot be negative")
 print(f"Age set to {age}")

set_age(25)   # OK
set_age(-5)   # Raises ValueError
```

---

## 6. The Philosophy of raise in Python

Python encourages explicit error signaling. Rather than returning error codes or None, use `raise` to make errors visible and force the caller to handle them.

### EAFP Principle

Pythonic code often follows the EAFP (Easier to Ask Forgiveness than Permission) principle:

```python
def get_item(dct, key):
 try:
  return dct[key]
 except KeyError:
  raise KeyError(f"Key '{key}' not found!")
```

---

## 7. Types of Exceptions You Can Raise

You can raise any exception that inherits from `BaseException`, but you should usually raise exceptions that inherit from `Exception`.

### Built-in Exceptions

- ValueError
- TypeError
- IndexError
- KeyError
- RuntimeError
- AssertionError
- NotImplementedError
- OSError
- ImportError
- ZeroDivisionError

### Custom Exceptions

Define your own exception classes for domain-specific errors:

```python
class MyCustomError(Exception):
 pass

raise MyCustomError("Something went wrong!")
```

---

## 8. Anatomy of the raise Statement

### Basic Syntax

```python
raise ExceptionType("Error message")
```

### Raising the Current Exception

Inside an except block, you can use `raise` with no arguments to re-raise the current exception:

```python
try:
 1 / 0
except ZeroDivisionError:
 print("About to re-raise...")
 raise
```

### Exception Chaining

Use `raise ... from ...` to chain exceptions and preserve the original cause:

```python
try:
 int("not a number")
except ValueError as e:
 raise RuntimeError("Failed to parse input") from e
```

---

## 9. The Role of raise in Robust Python Code

- Promotes clear, maintainable error handling
- Makes bugs easier to find and fix
- Encourages defensive programming
- Supports custom error hierarchies for large projects

---

## 10. Summary

The `raise` statement is a core part of Python's error handling philosophy. It allows you to signal, propagate, and chain errors in a clear and explicit way. Mastering `raise` is essential for writing professional, reliable Python code.

---

## 11. Advanced Usage

### 11.1. Dynamic Exception Creation

You can raise exceptions dynamically based on runtime conditions:

```python
def check_value(x):
  if not isinstance(x, int):
    raise TypeError(f"Expected int, got {type(x).__name__}")
  if x < 0:
    raise ValueError("Value must be non-negative")
  return x
```

### 11.2. Raising Exceptions in Loops and Comprehensions

```python
for i in range(5):
  if i == 3:
    raise RuntimeError("Loop interrupted at i=3")
  print(i)
```

### 11.3. Raising Exceptions in Class Methods and Properties

```python
class Person:
  def __init__(self, name, age):
    if not name:
      raise ValueError("Name cannot be empty")
    if age < 0:
      raise ValueError("Age cannot be negative")
    self.name = name
    self.age = age

  @property
  def is_adult(self):
    if self.age < 0:
      raise ValueError("Invalid age")
    return self.age >= 18
```

### 11.4. Raising Exceptions in Context Managers

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
  print("Resource acquired")
  try:
    yield
  except Exception as e:
    print(f"Exception in context: {e}")
    raise
  finally:
    print("Resource released")

try:
  with managed_resource():
    raise RuntimeError("Something went wrong!")
except RuntimeError as e:
  print(f"Caught: {e}")
```

---

## 12. Best Practices and Common Pitfalls

- Raise exceptions only for truly exceptional conditions.
- Use built-in exception types when appropriate.
- Create custom exceptions for domain-specific errors.
- Always provide a clear, descriptive error message.
- Avoid raising generic Exception or BaseException.
- Never use raise to control normal program flow.
- Document exceptions in your function/class docstrings.

**Anti-pattern:**

```python
def find_index(lst, value):
  try:
    return lst.index(value)
  except ValueError:
    raise  # Good: propagate real error

def bad_find_index(lst, value):
  if value not in lst:
    raise Exception("Value not found")  # BAD: too generic
  return lst.index(value)
```

---

## 13. Real-World Scenarios

### 13.1. File Operations

```python
def read_positive_integer(filename):
  try:
    with open(filename) as f:
      value = int(f.read())
      if value < 0:
        raise ValueError("File contains a negative number")
      return value
  except FileNotFoundError:
    raise FileNotFoundError(f"File '{filename}' not found")
  except ValueError as e:
    raise ValueError(f"Invalid data in file: {e}")
```

### 13.2. API and Web Development

```python
def get_user(user_id):
  if not isinstance(user_id, int):
    raise TypeError("user_id must be an integer")
  # Simulate database lookup
  if user_id != 1:
    raise LookupError("User not found")
  return {"id": 1, "name": "Alice"}
```

### 13.3. Data Validation in Libraries

```python
def validate_email(email):
  if "@" not in email:
    raise ValueError("Invalid email address")
  return True
```

---

## 14. Comparison with Other Languages

- In Java, C++, and C#, exceptions are raised with throw; in Python, use raise.
- Python's raise is simpler and more flexible, allowing dynamic exception creation and chaining.
- Python encourages explicit, readable error signaling.

---

## 15. Key Takeaways

- Use raise to signal, propagate, and chain errors.
- Prefer specific, meaningful exception types.
- Never use raise for normal control flow.
- Document and test your exception handling logic.

---

This comprehensive guide covers every aspect of the raise statement in Python, with advanced usage, best practices, anti-patterns, and real-world scenarios. For even more depth, add sections on async code, multi-threading, and integration with third-party libraries as needed.
