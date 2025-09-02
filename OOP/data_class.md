# Data Classes in Python

## 1. Introduction and Syllabus

Data classes, introduced in Python 3.7 via the `dataclasses` module, provide a decorator and functions for automatically adding special methods to user-defined classes. They are designed to make class-based data structures concise, readable, and less error-prone, while supporting type hints and default values.

### Syllabus

- What is a data class?
- Motivation and benefits
- The `@dataclass` decorator
- Basic usage and syntax
- Field types, default values, and default factories
- Comparison, hashing, and immutability
- Post-init processing (`__post_init__`)
- Inheritance and data classes
- Best practices and common pitfalls
- Real-world examples and advanced usage

---

## 2. What is a Data Class?

- A data class is a regular Python class decorated with `@dataclass` that automatically generates special methods like `__init__`, `__repr__`, `__eq__`, and more.
- Designed for classes that primarily store data and have little custom behavior.

---

## 3. Motivation and Benefits

- Reduces boilerplate code for data containers.
- Improves readability and maintainability.
- Supports type hints, default values, and field customization.
- Integrates with standard library features (e.g., typing, collections).

---

## 4. The `@dataclass` Decorator

- Import from the standard library:

```python
from dataclasses import dataclass
```

- Apply to a class to auto-generate methods:

```python
@dataclass
class Point:
    x: int
    y: int
```

---

## 5. Basic Usage and Syntax

- Define fields with type annotations.
- Default values are supported.
- Example:

```python
@dataclass
class Person:
    name: str
    age: int = 0
```

---

## 6. Field Types, Default Values, and Default Factories

- Use `field()` for advanced options:

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Group:
    members: List[str] = field(default_factory=list)
```

---

## 7. Comparison, Hashing, and Immutability

- Data classes can auto-generate `__eq__`, `__lt__`, `__hash__`, etc.
- Use `frozen=True` for immutable data classes.

```python
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int
```

---

## 8. Post-init Processing (`__post_init__`)

- Use `__post_init__` for validation or computed fields after `__init__` runs.

```python
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0
    def __post_init__(self):
        self.area = self.width * self.height
```

---

## 9. Inheritance and Data Classes

- Data classes support inheritance, but field order and init logic require care.
- Use `init=False` for fields not set by the constructor.

---

## 10. Best Practices and Common Pitfalls

- Always use type annotations for fields.
- Avoid mutable default arguments (use `default_factory`).
- Be careful with inheritance and field order.
- Use `frozen=True` for hashable/immutable objects.
- Document the intended use and limitations.

---

## 11. Real-World Examples and Advanced Usage

---

## 12. Advanced & Practical Examples: Data Classes

### 1. Data Class with Validation and Computed Fields

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1
    total: float = field(init=False)
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price must be non-negative")
        self.total = self.price * self.quantity

p = Product('Book', 10.0, 3)
print(p.total)  # 30.0
```

---

### 2. Immutable and Hashable Data Class

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
print(hash(p1))
# p1.x = 10  # Raises FrozenInstanceError
```

---

### 3. Data Class Inheritance and Field Customization

```python
from dataclasses import dataclass, field

@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str = 'Unknown'
    tricks: list = field(default_factory=list)

d = Dog('Fido', breed='Labrador')
print(d)
```

---

### 4. Using `field` for Metadata and Default Factories

```python
from dataclasses import dataclass, field

@dataclass
class Config:
    options: dict = field(default_factory=dict, metadata={'description': 'Config options'})

c = Config()
c.options['debug'] = True
print(Config.__dataclass_fields__['options'].metadata)
```

---

### 5. Data Class as a Record Type (Serialization)

```python
from dataclasses import dataclass, asdict, astuple

@dataclass
class User:
    id: int
    name: str

u = User(1, 'Alice')
print(asdict(u))   # {'id': 1, 'name': 'Alice'}
print(astuple(u))  # (1, 'Alice')
```

---

### 6. Comparison: Data Class vs NamedTuple vs Classic Class

```python
from dataclasses import dataclass
from collections import namedtuple

@dataclass
class DataPoint:
    x: int
    y: int

PointNT = namedtuple('PointNT', ['x', 'y'])

class ClassicPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(DataPoint(1,2))
print(PointNT(1,2))
print(ClassicPoint(1,2))
```

---

### 7. Anti-Pattern: Mutable Default Arguments

```python
from dataclasses import dataclass, field

@dataclass
class Bad:
    items: list = []  # BAD: All instances share the same list!

b1 = Bad()
b2 = Bad()
b1.items.append(1)
print(b2.items)  # [1]

# Correct way:
@dataclass
class Good:
    items: list = field(default_factory=list)
```

---

### 8. Best Practice: Use Type Annotations and Default Factories

Always use type annotations for all fields and use `default_factory` for mutable defaults.

---

### 9. Further Reading

- [Python docs: dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [PEP 557: Data Classes](https://peps.python.org/pep-0557/)
- [Data Classes vs NamedTuple](https://realpython.com/python-data-classes/#data-classes-vs-namedtuple)
