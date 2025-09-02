# Limiting Attributes Using `__slots__` in Python

## 1. Introduction and Syllabus

The `__slots__` mechanism in Python allows you to explicitly declare a fixed set of attributes for your class, preventing the creation of arbitrary new attributes and saving memory by avoiding the per-instance `__dict__`. Mastering `__slots__` is important for writing memory-efficient, high-performance classes, especially in large-scale or resource-constrained applications.

### Syllabus

- What is `__slots__`? (definition, motivation, and real-world analogy)
- How attribute storage works in Python objects
- Declaring `__slots__` in a class
- Effects of `__slots__` on memory usage and performance
- Attribute access, assignment, and errors with `__slots__`
- Inheritance and `__slots__`
- Limitations and caveats of `__slots__`
- Best practices for using `__slots__`
- Common pitfalls and anti-patterns
- Real-world examples and advanced usage

---

## 2. What is `__slots__`?

- `__slots__` is a class attribute that defines a fixed list of attribute names for instances.
- Prevents the creation of a per-instance `__dict__` (unless explicitly included).
- Restricts instances to only the attributes listed in `__slots__`.

**Real-world analogy:** Think of `__slots__` as a fixed set of labeled bins in a toolbox—only those bins can be used, and you can't add new ones.

---

## 3. How Attribute Storage Works in Python Objects

- By default, each instance has a `__dict__` for dynamic attribute storage.
- This allows adding new attributes at runtime, but uses more memory per object.
- `__slots__` replaces the `__dict__` with a static structure (like a tuple or array).

---

## 4. Declaring `__slots__` in a Class

- Define `__slots__` as a tuple or list of attribute names at the class level.

```python
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 5. Effects of `__slots__` on Memory Usage and Performance

- Reduces memory usage for large numbers of instances.
- Can speed up attribute access due to fixed layout.
- Prevents adding new attributes not listed in `__slots__`.

---

## 6. Attribute Access, Assignment, and Errors with `__slots__`

- Only attributes listed in `__slots__` can be set.
- Attempting to assign a new attribute raises `AttributeError`.

```python
p = Point(1, 2)
p.x = 10  # OK
# p.z = 5  # AttributeError: 'Point' object has no attribute 'z'
```

---

## 7. Inheritance and `__slots__`

- Subclasses must declare their own `__slots__` to add new attributes.
- If a subclass does not declare `__slots__`, it will have a `__dict__` and allow arbitrary attributes.
- Multiple inheritance with `__slots__` can be tricky—use with care.

---

## 8. Limitations and Caveats of `__slots__`

- Cannot use `__slots__` with some built-in types (e.g., if inheriting from `list`, `dict`).
- Cannot use weak references unless `__weakref__` is included in `__slots__`.
- No support for class variables in `__slots__`.
- Not all Python tools and libraries expect or support `__slots__`.

---

## 9. Best Practices for Using `__slots__`

- Use `__slots__` for classes with many instances and a fixed set of attributes.
- Document the purpose and limitations of `__slots__` in your class docstring.
- Avoid using `__slots__` in classes that require dynamic attributes or complex inheritance.

---

## 10. Common Pitfalls and Anti-Patterns

- Forgetting to include all needed attributes in `__slots__`.
- Using `__slots__` in classes that need dynamic attributes.
- Not including `__weakref__` if weak references are required.
- Overusing `__slots__` for minor memory savings.

---

## 11. Real-World Examples and Advanced Usage

(Advanced/practical examples will be added in the next step.)

### 1. Memory Savings with **slots**

```python
import sys

class Regular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Slotted:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

r = Regular(1, 2)
s = Slotted(1, 2)
print(sys.getsizeof(r.__dict__))  # Size of instance dict
# print(sys.getsizeof(s.__dict__))  # AttributeError: 'Slotted' object has no attribute '__dict__'
```

---

### 2. Preventing Arbitrary Attribute Assignment

```python
class Person:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Alice', 30)
p.name = 'Bob'  # OK
# p.address = '123 Main St'  # AttributeError
```

---

### 3. Inheritance and Extending **slots**

```python
class Base:
    __slots__ = ('a',)
    def __init__(self, a):
        self.a = a

class Child(Base):
    __slots__ = ('b',)
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

c = Child(1, 2)
print(c.a, c.b)
# c.c = 3  # AttributeError
```

---

### 4. Allowing Weak References with **weakref**

```python
import weakref
class Node:
    __slots__ = ('value', '__weakref__')
    def __init__(self, value):
        self.value = value

n = Node(10)
w = weakref.ref(n)
print(w())  # <__main__.Node object ...>
```

---

### 5. Edge Case: Subclass Without **slots**

```python
class Parent:
    __slots__ = ('x',)
class Child(Parent):
    pass

c = Child()
c.x = 1
c.y = 2  # Allowed! Child has __dict__
```

---

*These advanced examples show how to use **slots** for memory savings, attribute control, inheritance, weak references, and highlight important edge cases. Mastering **slots** is key for efficient and robust Python class design.*
