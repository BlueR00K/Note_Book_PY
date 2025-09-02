# Creating Context Managers Using Classes in Python

## 1. Introduction and Syllabus

Context managers are a core feature in Python that allow you to allocate and release resources precisely when you want. They are most commonly used with the `with` statement for resource management (e.g., files, locks, network connections). Creating your own context managers using classes gives you fine-grained control over setup and teardown logic.

### Syllabus

- What is a context manager?
- The context management protocol: `__enter__` and `__exit__`
- Using context managers with the `with` statement
- Creating a basic context manager class
- Exception handling in context managers
- Reusable and parameterized context managers
- Nesting and stacking context managers
- Best practices and common pitfalls
- Real-world examples and advanced usage

---

## 2. What is a Context Manager?

- A context manager is an object that defines runtime context to be established and cleaned up.
- Used with the `with` statement to ensure resources are properly managed.
- Common use cases: file I/O, database connections, locks, temporary changes to state.

---

## 3. The Context Management Protocol: `__enter__` and `__exit__`

- `__enter__(self)`: Called at the start of the `with` block. Returns the resource or self.
- `__exit__(self, exc_type, exc_value, traceback)`: Called at the end of the block, even if an exception occurs. Handles cleanup.

---

## 4. Using Context Managers with the `with` Statement

```python
with open('file.txt', 'r') as f:
    data = f.read()
# File is automatically closed here
```

---

## 5. Creating a Basic Context Manager Class

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('Hello, world!')
# File is closed automatically
```

---

## 6. Exception Handling in Context Managers

- `__exit__` can suppress exceptions by returning `True`.
- If `__exit__` returns `False` (or None), exceptions are propagated.

```python
class IgnoreErrors:
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # Suppress all exceptions

with IgnoreErrors():
    1 / 0  # No error raised
```

---

## 7. Reusable and Parameterized Context Managers

- Context managers can accept parameters and be reused for different resources.
- Example: managing database connections, temporary files, etc.

---

## 8. Nesting and Stacking Context Managers

- Multiple context managers can be nested or stacked using `with ... as ... , ... as ...` syntax.

```python
with open('a.txt') as fa, open('b.txt') as fb:
    ...
```

---

## 9. Best Practices and Common Pitfalls

- Always ensure resources are released in `__exit__`, even on error.
- Avoid side effects in `__enter__`/`__exit__` unless intentional.
- Document the context manager's behavior and usage.
- Use contextlib for simpler cases (see advanced section).

---

## 10. Real-World Examples and Advanced Usage

---

## 11. Advanced & Practical Examples: Context Managers Using Classes

### 1. Resource Locking (Threading)

```python
import threading

class Locked:
    def __init__(self, lock):
        self.lock = lock
    def __enter__(self):
        self.lock.acquire()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock.release()

lock = threading.Lock()
with Locked(lock):
    print("Critical section")
```

---

### 2. Temporary Environment Variable

```python
import os

class TempEnvVar:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.old = None
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.old is None:
            del os.environ[self.key]
        else:
            os.environ[self.key] = self.old

with TempEnvVar('MY_VAR', '42'):
    print(os.environ['MY_VAR'])  # 42
```

---

### 3. Nested Context Managers and Error Handling

```python
class ResourceA:
    def __enter__(self):
        print('Enter A')
        return 'A'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit A')

class ResourceB:
    def __enter__(self):
        print('Enter B')
        return 'B'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit B')

with ResourceA() as a, ResourceB() as b:
    print(a, b)
```

---

### 4. Reentrant Context Manager

```python
class Reentrant:
    def __init__(self):
        self.count = 0
    def __enter__(self):
        self.count += 1
        print(f"Entered {self.count} times")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting {self.count} times")
        self.count -= 1

r = Reentrant()
with r:
    with r:
        pass
```

---

### 5. Timing and Profiling Context Manager

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.4f} seconds")

with Timer():
    time.sleep(1)
```

---

### 6. Using contextlib for Class-Based and Function-Based Context Managers

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print('Setup')
    yield 'resource'
    print('Cleanup')

with managed_resource() as res:
    print(res)
```

---

### 7. Anti-Pattern: Not Releasing Resources on Exception

```python
class BadManager:
    def __enter__(self):
        print('Acquired')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Released')
        # BAD: Does not release on exception!

# Always release resources in __exit__, regardless of exceptions.
```

---

### 8. Best Practice: Always Release Resources

Ensure `__exit__` always releases resources, even if an exception occurs.

---

### 9. Further Reading

- [Python docs: Context Manager Types](https://docs.python.org/3/library/stdtypes.html#typecontextmanager)
- [contextlib module](https://docs.python.org/3/library/contextlib.html)
- [PEP 343: The "with" Statement](https://peps.python.org/pep-0343/)
