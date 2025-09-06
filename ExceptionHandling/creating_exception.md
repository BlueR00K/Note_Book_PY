# Creating Exceptions in Python

## 1. Syllabus

- Introduction to creating exceptions
- Why create custom exceptions?
- Syntax for defining custom exception classes
- Inheriting from built-in exception types
- Adding custom attributes and methods
- Best practices for custom exceptions
- Real-world use cases
- Advanced usage (exception hierarchies, multiple inheritance, etc.)
- Comparison with other languages
- Summary and key takeaways

---

## 2. Introduction

While Python provides many built-in exception types, creating your own custom exceptions is a powerful way to make your code more readable, maintainable, and robust. Custom exceptions allow you to signal domain-specific errors and handle them in a structured way.

---

## 3. Why Create Custom Exceptions?

- **Clarity:** Custom exceptions make your code self-documenting. When you see `raise InvalidUserInputError`, you immediately know what went wrong.
- **Separation of concerns:** Differentiate between different error types in your application logic.
- **Control:** Allow callers to catch and handle only the exceptions they care about.
- **Extensibility:** Build exception hierarchies for large projects.

---

## 4. Foundational Concepts

### What is a Custom Exception?

A custom exception is a class that inherits from Python's built-in `Exception` class (or one of its subclasses). You can add custom messages, attributes, and methods to provide more context about the error.

### Exception Inheritance

All exceptions in Python inherit from `BaseException`. Most user-defined exceptions should inherit from `Exception`.

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

---

## 5. Syntax for Defining Custom Exception Classes

### The Simplest Custom Exception

```python
class MyCustomError(Exception):
 pass

raise MyCustomError("Something went wrong!")
```

### Adding a Docstring

```python
class InvalidUserInputError(Exception):
 """Raised when user input is invalid."""
 pass
```

### Adding Custom Attributes

```python
class FileFormatError(Exception):
 def __init__(self, filename, message):
  super().__init__(message)
  self.filename = filename
  self.message = message

try:
 raise FileFormatError("data.csv", "Invalid CSV format")
except FileFormatError as e:
 print(f"Error in file {e.filename}: {e.message}")
```

---

## 6. Inheriting from Built-in Exception Types

You can inherit from any built-in exception type to create more specific errors:

```python
class NegativeAgeError(ValueError):
 pass

def set_age(age):
 if age < 0:
  raise NegativeAgeError("Age cannot be negative")
 print(f"Age set to {age}")

set_age(25)   # OK
set_age(-5)   # Raises NegativeAgeError
```

---

## 7. Best Practices for Custom Exceptions

- Inherit from `Exception` or a relevant built-in exception.
- Use descriptive names ending with `Error`.
- Add docstrings to explain the purpose of the exception.
- Include relevant attributes for context (e.g., filename, user_id).
- Avoid catching or raising `BaseException` directly.
- Group related exceptions in a hierarchy for large projects.

---

## 8. Real-World Use Cases

### Example 1: User Input Validation

```python
class InvalidEmailError(Exception):
 pass

def validate_email(email):
 if "@" not in email:
  raise InvalidEmailError(f"Invalid email: {email}")
 return True

try:
 validate_email("not-an-email")
except InvalidEmailError as e:
 print(e)
```

### Example 2: API Error Handling

```python
class APIError(Exception):
 def __init__(self, status_code, message):
  super().__init__(message)
  self.status_code = status_code

def fetch_data():
 # Simulate an API error
 raise APIError(404, "Resource not found")

try:
 fetch_data()
except APIError as e:
 print(f"API Error {e.status_code}: {e}")
```

### Example 3: Custom Exception Hierarchies

```python
class ApplicationError(Exception):
 pass

class DatabaseError(ApplicationError):
 pass

class ConnectionError(DatabaseError):
 pass

class QueryError(DatabaseError):
 pass

try:
 raise QueryError("Invalid SQL query")
except ApplicationError as e:
 print(f"Application error: {e}")
```

---

## 9. Advanced Usage

### Multiple Inheritance

You can use multiple inheritance for exceptions, but do so with care:

```python
class LoggingMixin:
 def log(self):
  print(f"Logging error: {self}")

class MyLoggedError(Exception, LoggingMixin):
 pass

try:
 raise MyLoggedError("Something to log!")
except MyLoggedError as e:
 e.log()
```

### Exception Chaining in Custom Exceptions

```python
class DataProcessingError(Exception):
 pass

def process_data(data):
 try:
  return int(data)
 except ValueError as e:
  raise DataProcessingError("Failed to process data") from e

try:
 process_data("not-a-number")
except DataProcessingError as e:
 print(f"Chained: {e}")
 print(f"Original: {e.__cause__}")
```

---

## 10. Comparison with Other Languages

- In Java, custom exceptions must extend `Exception` or `RuntimeException`.
- In C++, exceptions can be any type, but classes are preferred.
- Python's custom exceptions are simple, flexible, and encourage clear error signaling.

---

## 11. More Advanced Scenarios and Edge Cases

### 11.1. Exception Hierarchies in Large Projects

For large applications, group related exceptions in modules or packages:

```python
# errors.py
class MyAppError(Exception):
  """Base class for all app errors."""
  pass

class ConfigError(MyAppError):
  pass

class AuthError(MyAppError):
  pass

class AuthTokenExpired(AuthError):
  pass

class AuthPermissionDenied(AuthError):
  pass
```

### 11.2. Integrating with Logging

Custom exceptions can be logged for debugging and monitoring:

```python
import logging

class PaymentError(Exception):
  pass

def process_payment(amount):
  if amount <= 0:
    raise PaymentError("Amount must be positive")

try:
  process_payment(-100)
except PaymentError as e:
  logging.error(f"Payment failed: {e}")
```

### 11.3. Custom Exceptions in Async Code

```python
import asyncio

class AsyncTimeoutError(Exception):
  pass

async def fetch_data():
  await asyncio.sleep(0.1)
  raise AsyncTimeoutError("Request timed out")

async def main():
  try:
    await fetch_data()
  except AsyncTimeoutError as e:
    print(f"Caught async error: {e}")

# asyncio.run(main())
```

### 11.4. Custom Exceptions in Testing

```python
import pytest

class CustomTestError(Exception):
  pass

def buggy_func():
  raise CustomTestError("Test error!")

def test_buggy_func():
  with pytest.raises(CustomTestError):
    buggy_func()
```

### 11.5. Exceptions with Additional Context

```python
class HTTPError(Exception):
  def __init__(self, status_code, url, message):
    super().__init__(message)
    self.status_code = status_code
    self.url = url

try:
  raise HTTPError(404, "https://example.com", "Not Found")
except HTTPError as e:
  print(f"HTTP {e.status_code} for {e.url}: {e}")
```

### 11.6. Anti-patterns and What to Avoid

- Catching or raising `BaseException` (catches system-exiting exceptions)
- Using generic names like `Error` or `Exception` for custom classes
- Not providing a message or context
- Overusing custom exceptions for trivial cases

**Example:**

```python
# BAD: Don't do this
class Error(Exception):
  pass

try:
  raise Error()
except Exception:
  print("Too generic!")
```

---

## 12. Custom Exception Patterns in Real-World Applications

### 12.1. Web Frameworks (e.g., Flask, Django)

```python
class HTTP400Error(Exception):
  pass

def handle_request(data):
  if not data:
    raise HTTP400Error("Bad Request: No data provided")

try:
  handle_request("")
except HTTP400Error as e:
  print(f"Web error: {e}")
```

### 12.2. Data Science and ETL

```python
class DataValidationError(Exception):
  pass

def validate_row(row):
  if not isinstance(row, dict):
    raise DataValidationError("Row must be a dict")
  if "id" not in row:
    raise DataValidationError("Missing 'id' field")

try:
  validate_row([1,2,3])
except DataValidationError as e:
  print(f"Data error: {e}")
```

### 12.3. CLI Tools

```python
class CLIError(Exception):
  pass

def parse_args(args):
  if "--help" in args:
    raise CLIError("Help requested")

try:
  parse_args(["--help"])
except CLIError as e:
  print(f"CLI error: {e}")
```

### 12.4. Security and Permissions

```python
class PermissionDenied(Exception):
  pass

def access_resource(user):
  if not user.get("is_admin"):
    raise PermissionDenied("Admin access required")

try:
  access_resource({"username": "bob", "is_admin": False})
except PermissionDenied as e:
  print(f"Security error: {e}")
```

### 12.5. Internationalization (i18n)

```python
class LocalizedError(Exception):
  def __init__(self, message, lang="en"):
    super().__init__(message)
    self.lang = lang

try:
  raise LocalizedError("Erreur inconnue", lang="fr")
except LocalizedError as e:
  print(f"Error in {e.lang}: {e}")
```

---

## 13. Documenting and Testing Custom Exceptions

- Always document custom exceptions in your API docs and docstrings.
- Write unit tests to ensure exceptions are raised and handled as expected.
- Use type hints and static analysis tools to improve reliability.

**Example docstring:**

```python
class MyCustomError(Exception):
  """Raised when a custom error occurs.

  Args:
    message (str): Description of the error.
  """
  pass
```

---

## 14. Summary and Final Thoughts

- Custom exceptions are a best practice for robust, maintainable Python code.
- Use them to clarify, document, and control error handling in your projects.
- Integrate with logging, testing, and async code for professional results.

---
