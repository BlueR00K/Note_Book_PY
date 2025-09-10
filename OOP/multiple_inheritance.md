
# Multiple Inheritance in Python

## Syllabus

1. Introduction: What is multiple inheritance and why is it important?
2. What is multiple inheritance?
3. Syntax and basic example
4. The diamond problem and MRO
5. Using `super()` in multiple inheritance
6. Best practices
7. Advanced and practical examples
8. Summary and key takeaways

---

## 1. Introduction

Multiple inheritance is an object-oriented programming feature where a class can inherit attributes and methods from more than one parent class. It enables powerful code reuse and flexible class hierarchies, but also introduces complexity such as the diamond problem and method resolution order (MRO).

---

## 2. What is Multiple Inheritance?

- A subclass can inherit from two or more parent classes.
- The subclass gains access to all public and protected members of its parents.
- Python supports multiple inheritance directly (unlike some other languages).

---

## 3. Syntax and Basic Example

```python
class A:
    def foo(self):
        print("A.foo")
class B:
    def bar(self):
        print("B.bar")
class C(A, B):
    pass

c = C()
c.foo()  # A.foo
c.bar()  # B.bar
```

---

## 4. The Diamond Problem and MRO

- The diamond problem occurs when a class inherits from two classes that both inherit from a common ancestor.
- Python uses the C3 linearization algorithm to determine the method resolution order (MRO).
- Use `ClassName.mro()` or `help(ClassName)` to inspect the MRO.

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
print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

## 5. Using `super()` in Multiple Inheritance

- `super()` ensures that all parent classes are called in the correct order according to the MRO.
- Each class should use `super()` to delegate to the next class in the MRO.

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

- Use multiple inheritance only when it models a clear, logical relationship.
- Always use `super()` in methods that may be overridden in subclasses.
- Avoid deep and complex inheritance hierarchies.
- Prefer mixins for sharing functionality across classes.
- Document the inheritance structure and MRO in class docstrings.

---

## 7. Advanced and Practical Examples: Multiple Inheritance

### 1. Combining Functionality from Multiple Parents

```python
class Flyer:
    def fly(self):
        print("Flying...")
class Swimmer:
    def swim(self):
        print("Swimming...")
class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()   # Flying...
d.swim()  # Swimming...
```

### 2. Mixins: Adding Reusable Functionality

```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal, JsonMixin):
    def bark(self):
        print("Woof!")

d = Dog("Buddy")
print(d.to_json())  # {"name": "Buddy"}
```

### 3. Diamond Problem: Ensuring Each Parent is Called Once

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

### 4. Inspecting the MRO

```python
class X: pass
class Y: pass
class A(X, Y): pass
class B(Y, X): pass
class C(A, B): pass

print(C.mro())
# [<class 'C'>, <class 'A'>, <class 'B'>, <class 'Y'>, <class 'X'>, <class 'object'>]
```

### 5. Overriding Methods in Multiple Inheritance

```python
class Writer:
    def write(self):
        print("Writing...")
class Blogger:
    def write(self):
        print("Blogging...")
class Author(Writer, Blogger):
    pass

a = Author()
a.write()  # Writing... (Writer is first in MRO)
```

### 6. Using `super()` in Mixins

```python
class LogMixin:
    def log(self, message):
        print(f"LOG: {message}")
        super().log(message)
class Base:
    def log(self, message):
        print(f"Base: {message}")
class Service(LogMixin, Base):
    def log(self, message):
        print(f"Service: {message}")
        super().log(message)

s = Service()
s.log("Started")
# Service: Started
# LOG: Started
# Base: Started
```

### 7. Edge Case: Attribute Name Conflicts

```python
class A:
    def __init__(self):
        self.value = "A"
class B:
    def __init__(self):
        self.value = "B"
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

c = C()
print(c.value)  # B (last assignment wins)
```

### 8. Abstract Base Classes and Multiple Inheritance

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Colored:
    def color(self):
        return "red"
class Square(Shape, Colored):
    def area(self):
        return 4

s = Square()
print(s.area())   # 4
print(s.color())  # red
```

### 9. Best Practice: Prefer Mixins for Shared Functionality

```python
class TimestampMixin:
    def timestamp(self):
        import datetime
        return datetime.datetime.now()
class Entity(TimestampMixin):
    pass

e = Entity()
print(e.timestamp())
```

### 10. Limitation: Cooperative `super()` Only Works with New-Style Classes

# All classes in Python 3 are new-style (inherit from `object`), so `super()` works as expected

---

## 8. Summary and Key Takeaways

- Multiple inheritance enables powerful code reuse but introduces complexity (diamond problem, MRO).
- Always use `super()` in methods that may be overridden to ensure proper chaining.
- Prefer mixins for sharing functionality across classes.
- Avoid deep and complex hierarchies; document the inheritance structure and MRO.

---
