
# `repr` and `str` Methods in Python

## 1. Syllabus

- Implementing both methods in a class
- Fallback behavior
- Using dataclasses for automatic `__repr__`
- Customizing for debugging and sensitive data
- Inheritance and nested representations
- Edge cases: recursion, logging, and default fallback

# `repr` and `str` Methods in Python

### Syllabus

1. Introduction to `repr` and `str`
2. Why Implement `__repr__` and `__str__`?
3. Differences Between `__repr__` and `__str__`
4. Syntax and Usage
5. Best Practices and Anti-Patterns
6. Advanced/Practical Examples
    - Implementing both methods in a class
    - Fallback behavior
    - Using dataclasses for automatic `__repr__`
    - Customizing for debugging and sensitive data
    - Inheritance and nested representations
    - Edge cases: recursion, logging, and default fallback
7. Summary and Key Takeaways

---
---

## 2. Introduction to `repr` and `str`

The `repr` and `str` methods are special (dunder) methods in Python that control how objects are represented as strings. Understanding and implementing these methods is crucial for debugging, logging, and creating user-friendly classes.

## 2. Why Implement `__repr__` and `__str__`?

Implementing `__repr__` and `__str__` in your classes is crucial for debugging, logging, and user-friendly display. These methods control how your objects are represented as strings, both for developers and end users.

---

## 3. Differences Between `__repr__` and `__str__`

- `__repr__` stands for "representation".
- Called by the built-in `repr()` function and in interactive sessions (e.g., the REPL, debugger, or logging).
- Should return a string that is a valid Python expression, ideally one that could be used to recreate the object.
- Main goal: unambiguous and detailed representation for developers.

### Example

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(1, 2)
print(repr(p))  # Point(x=1, y=2)
```

---

## 4. Syntax and Usage

### Example: `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(1, 2)
print(repr(p))  # Point(x=1, y=2)
```

### Example: `__str__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(str(p))  # (1, 2)
print(p)       # (1, 2)
```

---

## 5. Best Practices and Anti-Patterns

- `__str__` stands for "string".
- Called by the built-in `str()` function and by `print()`.
- Should return a readable, user-friendly string representation of the object.
- Main goal: concise and clear for end users.

### Example

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(str(p))  # (1, 2)
print(p)       # (1, 2)
```

---

## 5. Differences Between `__repr__` and `__str__`

| Feature         | `__repr__`                        | `__str__`                  |
|----------------|------------------------------------|----------------------------|
| Purpose        | Developer/debugging representation | User-friendly display      |
| Called by      | `repr()`, interactive shell        | `str()`, `print()`         |
| Fallback       | Used if `__str__` is missing       | Falls back to `__repr__`   |
| Format         | Unambiguous, detailed              | Readable, concise          |

---

## 6. Best Practices

- Always implement `__repr__` for custom classes, especially for debugging and logging.
- If `__str__` is not defined, Python uses `__repr__` as a fallback.
- `__repr__` should, if possible, return a string that could be used to recreate the object (or at least be unambiguous).
- `__str__` should be readable and user-oriented.
- Use f-strings for clarity and performance.
- For complex objects, include all relevant attributes in `__repr__`.
- Use `dataclasses` for automatic `__repr__` generation when appropriate.

---

## 6. Advanced/Practical Examples

### 6.1. Implementing Both `__repr__` and `__str__` in a Class

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __repr__(self):
        return f"User(username={self.username!r}, email={self.email!r})"
    def __str__(self):
        return f"{self.username} <{self.email}>"

u = User("alice", "alice@example.com")
print(repr(u))  # User(username='alice', email='alice@example.com')
print(str(u))   # alice <alice@example.com>
print(u)        # alice <alice@example.com>
```

### 6.2. Fallback Behavior: Only `__repr__` Defined

```python
class Product:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Product({self.name!r})"

p = Product("Book")
print(str(p))   # Product('Book')
print(repr(p))  # Product('Book')
```

### 6.3. Using `dataclasses` for Automatic `__repr__`

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print(repr(p))  # Point(x=3, y=4)
print(str(p))   # Point(x=3, y=4)
```

### 6.4. Customizing `__repr__` for Debugging Complex Objects

```python
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
    def __repr__(self):
        return f"Order(order_id={self.order_id!r}, items={self.items!r})"

o = Order(123, ["apple", "banana"])
print(repr(o))  # Order(order_id=123, items=['apple', 'banana'])
```

### 6.5. Handling Large or Sensitive Data in `__repr__`

```python
class Secret:
    def __init__(self, token):
        self.token = token
    def __repr__(self):
        return f"Secret(token=<hidden>)"

s = Secret("supersecret")
print(repr(s))  # Secret(token=<hidden>)
```

### 6.6. `__repr__` and `__str__` in Inheritance

```python
class Animal:
    def __repr__(self):
        return "Animal()"

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Dog(name={self.name!r})"
    def __str__(self):
        return f"Dog: {self.name}"

d = Dog("Rex")
print(repr(d))  # Dog(name='Rex')
print(str(d))   # Dog: Rex
```

### 6.7. Using `!r` and `!s` in f-strings for Nested Representations

```python
class Box:
    def __init__(self, content):
        self.content = content
    def __repr__(self):
        return f"Box(content={self.content!r})"
    def __str__(self):
        return f"Box of {self.content!s}"

b = Box([1, 2, 3])
print(repr(b))  # Box(content=[1, 2, 3])
print(str(b))   # Box of [1, 2, 3]
```

### 6.8. Edge Case: Recursive Objects

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f"Node(value={self.value!r}, next={repr(self.next)})"

n1 = Node(1)
n2 = Node(2)
n1.next = n2
n2.next = n1  # Circular reference
print(repr(n1))  # Will cause RecursionError if not handled carefully
```

### 6.9. Using `__repr__` for Logging and Debugging

```python
import logging
class User:
    def __init__(self, username):
        self.username = username
    def __repr__(self):
        return f"User({self.username!r})"

u = User("bob")
logging.basicConfig(level=logging.DEBUG)
logging.debug("User info: %r", u)
```

### 6.10. Fallback to Default `__repr__`/`__str__`

```python
class Empty:
    pass

e = Empty()
print(repr(e))  # <__main__.Empty object at 0x...>
print(str(e))   # <__main__.Empty object at 0x...>
```

---

## 7. Summary and Key Takeaways

- Always implement `__repr__` for debugging and logging
- Use `__str__` for user-friendly display
- Understand fallback behavior and edge cases
- Use dataclasses for automatic representations when appropriate

- Always implement `__repr__` for debugging and logging
- Use `__str__` for user-friendly display
- Understand fallback behavior and edge cases
- Use dataclasses for automatic representations when appropriate

---
