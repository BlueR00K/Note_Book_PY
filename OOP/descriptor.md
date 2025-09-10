
# Descriptors in Python

## Syllabus

1. Introduction: What are descriptors and why are they important?
2. What is a descriptor?
    - Definition and motivation
    - Comparison to properties and other attribute management
3. The descriptor protocol:
    - `__get__`, `__set__`, `__delete__` methods
    - How Python invokes these methods
4. Types of descriptors:
    - Data vs non-data descriptors
    - Precedence rules and attribute lookup
5. How Python uses descriptors internally:
    - Properties, methods, static/class methods
    - Built-in and user-defined descriptors
6. Creating custom descriptors:
    - Step-by-step implementation
    - Storing data per-instance vs on the descriptor
7. Use cases and motivation:
    - Type checking, validation, computed attributes, caching, logging, etc.
8. Best practices and common pitfalls:
    - Private attribute storage
    - Avoiding shared state
    - Documentation and intended use
9. Advanced and practical examples:
    - Type-checked, read-only, write-once, cached, logging, and shared descriptors
    - Anti-patterns and fixes
10. Further reading and resources
11. Summary and key takeaways

## 1. Introduction

Descriptors are a powerful, low-level protocol in Python that allow you to customize attribute access, storage, and management in classes. They are the foundation for properties, methods, static/class methods, and many advanced patterns in Python. Mastering descriptors enables you to create reusable, declarative, and efficient attribute management systems.

---

## 2. What is a Descriptor?

- A descriptor is any object that implements at least one of the methods: `__get__`, `__set__`, or `__delete__`.
- Descriptors are used to manage the attributes of other classes.
- They are the mechanism behind properties, methods, static methods, and class methods.

### Comparison: Descriptors vs Properties and Other Attribute Management

- **Descriptors:** Low-level protocol for attribute access; reusable and customizable; used to build properties, methods, and more.
- **Properties:** High-level, built-in descriptor for managed attributes; created with `@property` decorator; easier for simple use cases.
- **Other approaches:** Direct attribute access, `__getattr__`, `__setattr__`, and metaclasses for advanced customization.

---

## 3. The Descriptor Protocol: `__get__`, `__set__`, `__delete__`

- `__get__(self, instance, owner)`: Called to retrieve an attribute.
- `__set__(self, instance, value)`: Called to set an attribute.
- `__delete__(self, instance)`: Called to delete an attribute.

---

## 4. Types of Descriptors: Data vs Non-Data

- **Data descriptor:** Implements both `__get__` and `__set__` (or `__delete__`).
- **Non-data descriptor:** Implements only `__get__`.
- Data descriptors take precedence over instance attributes; non-data descriptors do not.

---

## 5. How Python Uses Descriptors Internally

- Functions, methods, `@property`, `@staticmethod`, and `@classmethod` are all implemented using descriptors.
- Example: `property` creates a data descriptor; functions are non-data descriptors.

---

## 6. Creating Custom Descriptors

**Important:** For per-instance data, always store values on the instance (e.g., `instance._attr`) rather than on the descriptor itself. This avoids shared state between objects and subtle bugs. See the anti-pattern and best practice examples below.

```python
class UpperCase:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value.upper()

class Person:
    name = UpperCase()
    def __init__(self, name):
        self.name = name

p = Person('alice')
print(p.name)  # ALICE
```

---

## 7. Use Cases and Motivation

- Type checking and validation
- Computed or derived attributes
- Lazy evaluation and caching
- Logging or auditing attribute access
- Implementing read-only or write-once fields

---

## 8. Best Practices and Common Pitfalls

- Always use a private attribute (e.g., `_name`) to store data to avoid recursion.
- Document the descriptor's behavior and intended usage.
- Be careful with inheritance and descriptor sharing between classes.
- Avoid side effects in `__get__`/`__set__` unless intentional.

---

## 9. Advanced & Practical Examples: Descriptors

### 1. Type-Checked Descriptor

```python
class Typed:
    def __init__(self, name, typ):
        self.name = '_' + name
        self.typ = typ
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if not isinstance(value, self.typ):
            raise TypeError(f"Expected {self.typ}")
        setattr(instance, self.name, value)

class Person:
    age = Typed('age', int)
    def __init__(self, age):
        self.age = age

p = Person(30)
# p.age = 'thirty'  # Raises TypeError
```

---

### 2. Read-Only Descriptor

```python
class ReadOnly:
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        raise AttributeError("Read-only attribute")

class Config:
    version = ReadOnly('1.0.0')

c = Config()
print(c.version)  # 1.0.0
# c.version = '2.0.0'  # Raises AttributeError
```

---

### 3. Write-Once Descriptor (Immutable After Set)

```python
class WriteOnce:
    def __init__(self, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if hasattr(instance, self.name):
            raise AttributeError("Attribute is write-once")
        setattr(instance, self.name, value)

class User:
    id = WriteOnce('id')
    def __init__(self, id):
        self.id = id

u = User(42)
# u.id = 99  # Raises AttributeError
```

---

### 4. Cached/Computed Property Descriptor

```python
class CachedSquare:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if not hasattr(instance, '_square'):
            instance._square = instance.value ** 2
        return instance._square

class Number:
    def __init__(self, value):
        self.value = value
    square = CachedSquare()

n = Number(5)
print(n.square)  # 25
n.value = 10
print(n.square)  # Still 25 (cached)
```

---

### 5. Logging/Auditing Descriptor

```python
class Logged:
    def __init__(self, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        value = getattr(instance, self.name)
        print(f"Accessed {self.name} = {value}")
        return value
    def __set__(self, instance, value):
        print(f"Set {self.name} = {value}")
        setattr(instance, self.name, value)

class Account:
    balance = Logged('balance')
    def __init__(self, balance):
        self.balance = balance

a = Account(100)
a.balance += 50  # Logs access and set
```

---

### 6. Descriptor for Class-Level Data Sharing

```python
class Shared:
    _value = None
    def __get__(self, instance, owner):
        return Shared._value
    def __set__(self, instance, value):
        Shared._value = value

class A:
    x = Shared()
class B:
    x = Shared()

A.x = 10
print(B.x)  # 10
```

---

### 7. Anti-Pattern: Storing Data on the Descriptor Instance

```python
class Bad:
    def __init__(self):
        self.value = None
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = value

class Demo:
    x = Bad()
    y = Bad()

d1 = Demo()
d2 = Demo()
d1.x = 1
d2.x = 2
print(d1.x, d2.x)  # Both print 2! (shared state)
```

---

### 8. Best Practice: Use Instance Storage for Per-Instance Data

Store data on the instance, not the descriptor, to avoid shared state between objects.

---

### 10. Further Reading

- [Python docs: Descriptors](https://docs.python.org/3/howto/descriptor.html)
- [PEP 487: Simpler customisation of class creation](https://peps.python.org/pep-0487/)
- [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)

---

## 11. Summary and Key Takeaways

- Descriptors provide a powerful, reusable protocol for customizing attribute access in Python.
- Use descriptors for validation, computed attributes, caching, logging, and more.
- Always store per-instance data on the instance, not the descriptor, to avoid shared state.
- Properties are a high-level, built-in descriptor for common managed attribute use cases.
- Document and test your descriptors for robust, maintainable code.
