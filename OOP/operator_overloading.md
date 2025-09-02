# Operator Overloading in Python

## 1. Introduction and Syllabus

Operator overloading allows you to define custom behavior for Python's built-in operators (such as `+`, `-`, `*`, `==`, etc.) in your own classes. By implementing special (dunder) methods, you can make your objects interact naturally with operators, enabling expressive, readable, and Pythonic code. Mastering operator overloading is essential for building custom data types, mathematical objects, and domain-specific languages.

### Syllabus

- What is operator overloading? (definition, motivation, and real-world analogy)
- Special (dunder) methods for operator overloading
- Arithmetic operators (`__add__`, `__sub__`, `__mul__`, etc.)
- Comparison operators (`__eq__`, `__lt__`, `__gt__`, etc.)
- In-place and reflected operators (`__iadd__`, `__radd__`, etc.)
- Type checking and best practices
- Operator overloading for custom data types (e.g., vectors, matrices)
- Common pitfalls and anti-patterns
- Real-world examples and advanced usage

---

## 2. What is Operator Overloading?

- Operator overloading lets you define how operators behave for your own classes.
- Achieved by implementing special methods (e.g., `__add__`, `__eq__`).
- Makes custom objects behave like built-in types.

**Real-world analogy:** Think of operator overloading as teaching a robot how to interpret the `+` sign for different objects: adding numbers, concatenating strings, or merging lists.

---

## 3. Special (Dunder) Methods for Operator Overloading

- Python uses special methods (double underscores, or "dunder" methods) to implement operator behavior.
- Examples: `__add__` for `+`, `__eq__` for `==`, `__str__` for `str()`.

---

## 4. Arithmetic Operators

- `__add__(self, other)` for `+`
- `__sub__(self, other)` for `-`
- `__mul__(self, other)` for `*`
- `__truediv__(self, other)` for `/`
- `__floordiv__(self, other)` for `//`
- `__mod__(self, other)` for `%`
- `__pow__(self, other)` for `**`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # (4, 6)
```

---

## 5. Comparison Operators

- `__eq__(self, other)` for `==`
- `__ne__(self, other)` for `!=`
- `__lt__(self, other)` for `<`
- `__le__(self, other)` for `<=`
- `__gt__(self, other)` for `>`
- `__ge__(self, other)` for `>=`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
```

---

## 6. In-Place and Reflected Operators

- In-place: `__iadd__` for `+=`, `__isub__` for `-=`, etc.
- Reflected: `__radd__` for right-hand `+`, `__rmul__` for right-hand `*`, etc.

```python
class Counter:
    def __init__(self, value):
        self.value = value
    def __iadd__(self, other):
        self.value += other
        return self

c = Counter(5)
c += 3
print(c.value)  # 8
```

---

## 7. Type Checking and Best Practices

- Always check the type of `other` in operator methods.
- Return `NotImplemented` if the operation is not supported for the given type.
- Avoid overloading operators in ways that surprise users.
- Document operator behavior in class docstrings.

---

## 8. Operator Overloading for Custom Data Types

- Useful for vectors, matrices, complex numbers, units, and domain-specific objects.
- Enables natural, mathematical syntax for custom types.

---

## 9. Common Pitfalls and Anti-Patterns

- Not returning `NotImplemented` for unsupported types.
- Overloading operators inconsistently or illogically.
- Forgetting to implement `__str__` or `__repr__` for readable output.
- Using operator overloading for non-obvious or confusing behaviors.

---

## 10. Real-World Examples and Advanced Usage

(Advanced/practical examples will be added in the next step.)

### 1. Vector Class with Full Arithmetic and Comparison Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # (4, 6)
print(v2 - v1)      # (2, 2)
print(v1 * 3)       # (3, 6)
print(2 * v2)       # (6, 8)
print(v1 == Vector(1, 2))  # True
```

---

### 2. In-Place Operator Overloading with Type Checking

```python
class Counter:
    def __init__(self, value):
        self.value = value
    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.value += other
        return self

c = Counter(10)
c += 5
print(c.value)  # 15
```

---

### 3. Overloading Comparison for Custom Sorting

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __lt__(self, other):
        return self.grade < other.grade
    def __str__(self):
        return f"{self.name}: {self.grade}"

students = [Student("Alice", 90), Student("Bob", 85), Student("Charlie", 95)]
students.sort()
for s in students:
    print(s)
# Output:
# Bob: 85
# Alice: 90
# Charlie: 95
```

---

### 4. Edge Case: Returning NotImplemented

```python
class Foo:
    def __add__(self, other):
        return NotImplemented

f = Foo()
# print(f + 1)  # TypeError: unsupported operand type(s) for +: 'Foo' and 'int'
```

---

### 5. Best Practice: Documenting Operator Behavior

```python
class Money:
    """Represents an amount of currency. Supports +, -, ==, and str."""
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)
    def __str__(self):
        return f"${self.amount:.2f}"

m1 = Money(10)
m2 = Money(5)
print(m1 + m2)  # $15.00
```

---

*These advanced examples show how to use operator overloading for expressive, robust, and Pythonic custom types. Mastering operator overloading is key to building natural and maintainable APIs in Python.*
