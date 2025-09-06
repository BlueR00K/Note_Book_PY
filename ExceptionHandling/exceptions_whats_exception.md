# What's an Exception in Python?

## 1. Introduction and Syllabus

Exception handling is a core part of robust Python programming. Understanding what exceptions are, how they differ from errors, and how Python's exception system works is essential for writing safe, maintainable, and professional code. This section covers the fundamentals of exceptions, errors, and their similarities and differences.

### Syllabus

- What is an exception?
- What is an error?
- Exception vs Error: similarities and differences
- The role of exceptions in Python
- Built-in exception hierarchy
- Checked vs unchecked exceptions (Python vs other languages)
- Raising and catching exceptions (overview)
- Exception objects and traceback
- Best practices and common pitfalls
- Real-world examples and advanced usage

---

## 2. What is an Exception?

- An exception is an event that disrupts the normal flow of a program's execution.
- In Python, exceptions are objects that represent errors or unexpected conditions.
- When an exception occurs, Python creates an exception object and "raises" it.
- If not handled, the program terminates and prints a traceback.

---

## 3. What is an Error?

- In Python, the term "error" is often used informally to refer to any problem that occurs during execution.
- Technically, all errors in Python are represented as exceptions (instances of `BaseException`).
- Some errors are unrecoverable (e.g., `SystemExit`, `KeyboardInterrupt`), while most can be caught and handled.

---

## 4. Exception vs Error: Similarities and Differences

- **Similarity:** Both represent problems during execution and are instances of exception classes.
- **Difference:**
  - "Exception" is the technical term for Python's error-handling objects.
  - "Error" is a general term; in Python, specific error types are subclasses of `Exception` (e.g., `ValueError`, `TypeError`).
  - Some exceptions (like `SystemExit`, `KeyboardInterrupt`) are not considered "errors" in the usual sense.
- In other languages (e.g., Java), "error" and "exception" may have stricter distinctions (checked vs unchecked).

---

## 5. The Role of Exceptions in Python

- Exceptions provide a structured way to signal and handle errors.
- They allow separation of normal logic from error-handling logic.
- Used for both expected and unexpected conditions (e.g., file not found, invalid input).

---

## 6. Built-in Exception Hierarchy

- All exceptions inherit from `BaseException`.
- Common base classes:
  - `Exception`: Most user-defined and built-in exceptions
  - `ArithmeticError`, `LookupError`, `EnvironmentError`, etc.
- Special exceptions:
  - `SystemExit`, `KeyboardInterrupt`, `GeneratorExit` (not usually caught)
- Example hierarchy:

```python
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      └── ...
```

---

## 7. Checked vs Unchecked Exceptions (Python vs Other Languages)

- Python does not have checked exceptions (unlike Java).
- All exceptions are unchecked: you are not required to catch or declare them.
- This makes Python code more flexible but requires discipline in error handling.

---

## 8. Raising and Catching Exceptions (Overview)

- Exceptions are raised with the `raise` statement.
- They are caught using `try`/`except` blocks.
- Example:

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Caught: {e}")
```

---

## 9. Exception Objects and Traceback

- Exception objects carry information about the error (type, message, context).
- Tracebacks show the call stack at the point where the exception occurred.
- Useful for debugging and logging.

---

## 10. Best Practices and Common Pitfalls

- Catch only exceptions you can handle meaningfully.
- Avoid bare `except:` (catches everything, including `SystemExit` and `KeyboardInterrupt`).
- Use specific exception types in `except` blocks.
- Always clean up resources (use `finally` or context managers).
- Document expected exceptions in your code.

---

## 11. Real-World Examples and Advanced Usage

(Advanced/practical examples will be added in the next step.)
