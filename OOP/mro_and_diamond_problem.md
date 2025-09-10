
# MRO and the Diamond Problem in Multiple Inheritance (Python)

## Syllabus

1. Introduction: What is MRO and the diamond problem?
2. What is the diamond problem?
3. What is MRO (Method Resolution Order)?
4. How Python solves the diamond problem
5. Using `super()` with MRO
6. Best practices
7. Advanced and practical examples
8. Summary and key takeaways

---

## 1. Introduction

The Method Resolution Order (MRO) determines the order in which base classes are searched when executing a method. The diamond problem is a classic issue in multiple inheritance where a class inherits from two classes that both inherit from a common ancestor. Python solves this with the C3 linearization algorithm.

---

## 2. What is the Diamond Problem?

- Occurs when a class inherits from two classes that both inherit from a common ancestor.
- Can lead to ambiguity: which parent’s method should be called?

### Example

```python
class A:
    def greet(self):
        print("A")
class B(A):
    def greet(self):
        print("B")
class C(A):
    def greet(self):
        print("C")
class D(B, C):
    pass

d = D()
d.greet()  # B
```

---

## 3. What is MRO (Method Resolution Order)?

- MRO is the order in which Python looks for a method in a hierarchy of classes.
- Python uses the C3 linearization algorithm to compute the MRO.
- Use `ClassName.mro()` or `help(ClassName)` to inspect the MRO.

### Example

```python
print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

## 4. How Python Solves the Diamond Problem

- Python’s C3 linearization ensures each class appears only once in the MRO.
- The MRO is left-to-right, depth-first, but respects the order of base classes.
- Each class’s method is called at most once.

---

## 5. Using `super()` with MRO

- `super()` delegates method calls to the next class in the MRO.
- All classes in the hierarchy should use `super()` to ensure proper chaining.

### Example

```python
class A:
    def do(self):
        print("A.do")
class B(A):
    def do(self):
        print("B.do")
        super().do()
class C(A):
    def do(self):
        print("C.do")
        super().do()
class D(B, C):
    def do(self):
        print("D.do")
        super().do()

d = D()
d.do()
# D.do
# B.do
# C.do
# A.do
```

---

## 6. Best Practices

- Always use `super()` in methods that may be overridden in subclasses.
- Avoid deep and complex inheritance hierarchies.
- Use mixins for reusable functionality.
- Document the MRO and inheritance structure in class docstrings.

---

## 7. Advanced and Practical Examples: MRO and the Diamond Problem

### 1. Visualizing the Diamond Problem

```python
class A:
    def who(self):
        print("A")
class B(A):
    def who(self):
        print("B")
        super().who()
class C(A):
    def who(self):
        print("C")
        super().who()
class D(B, C):
    def who(self):
        print("D")
        super().who()

d = D()
d.who()
# D
# B
# C
# A
```

### 2. Inspecting and Explaining MRO

```python
print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

### 3. MRO with More Complex Hierarchies

```python
class X: pass
class Y: pass
class A(X, Y): pass
class B(Y, X): pass
class C(A, B): pass

print(C.mro())
# [<class 'C'>, <class 'A'>, <class 'B'>, <class 'Y'>, <class 'X'>, <class 'object'>]
```

### 4. Real-World Example: Cooperative Multiple Inheritance

```python
class SaveMixin:
    def save(self):
        print("SaveMixin.save")
        super().save()
class AuditMixin:
    def save(self):
        print("AuditMixin.save")
        super().save()
class Base:
    def save(self):
        print("Base.save")
class Model(SaveMixin, AuditMixin, Base):
    pass

m = Model()
m.save()
# SaveMixin.save
# AuditMixin.save
# Base.save
```

### 5. Edge Case: Skipping `super()` Breaks the Chain

```python
class A:
    def do(self):
        print("A.do")
class B(A):
    def do(self):
        print("B.do")
        # super().do()  # Not called
class C(A):
    def do(self):
        print("C.do")
        super().do()
class D(B, C):
    def do(self):
        print("D.do")
        super().do()

d = D()
d.do()
# D.do
# B.do
# (chain stops, A.do not called)
```

### 6. Using `super()` in Mixins and Abstract Base Classes

```python
from abc import ABC, abstractmethod
class LogMixin:
    def log(self, message):
        print(f"LOG: {message}")
        super().log(message)
class Base(ABC):
    @abstractmethod
    def log(self, message):
        pass
class Service(LogMixin, Base):
    def log(self, message):
        print(f"Service: {message}")
        # No super() call here to avoid recursion

s = Service()
s.log("Started")
# LOG: Started
# Service: Started
```

### 7. Best Practice: Documenting MRO in Class Docstrings

```python
class A:
    """Base class A."""
    pass
class B(A):
    """B inherits from A."""
    pass
class C(A):
    """C inherits from A."""
    pass
class D(B, C):
    """D inherits from B and C. MRO: D -> B -> C -> A -> object"""
    pass
```

---

## 8. Summary and Key Takeaways

- Python’s C3 MRO solves the diamond problem by ensuring each class appears only once in the resolution order.
- Always use `super()` in methods that may be overridden to ensure proper chaining.
- Avoid deep and complex inheritance hierarchies; use mixins for reusable functionality.
- Document the MRO and inheritance structure in class docstrings for clarity.
