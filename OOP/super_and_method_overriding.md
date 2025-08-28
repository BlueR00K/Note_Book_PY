# `super()` and Method Overriding in Python

## 1. Introduction

`super()` is a built-in function in Python used to call methods from a parent (super) class. Method overriding allows a subclass to provide a specific implementation of a method already defined in its superclass. Together, they are essential for customizing and extending class behavior in object-oriented programming.

---

## 2. What is Method Overriding?

- Method overriding occurs when a subclass defines a method with the same name as a method in its parent class.
- The subclass’s method replaces (overrides) the parent’s version when called on a subclass instance.
- Enables polymorphism and customization of inherited behavior.

### Example

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()  # Woof!
```

---

## 3. What is `super()`?

- `super()` returns a temporary object of the superclass, allowing you to call its methods.
- Commonly used in method overriding to extend or customize parent class behavior.
- Ensures proper initialization and method resolution order (MRO) in multiple inheritance.

### Example

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks!")

d = Dog("Buddy", "Labrador")
d.speak()
# Buddy makes a sound
# Buddy barks!
```

---

## 4. Why Use `super()`?

- To avoid duplicating code from the parent class.
- To ensure all parent initializations and logic are executed.
- To support cooperative multiple inheritance (MRO).
- To make code more maintainable and extensible.

---

## 5. Best Practices

- Always use `super()` in method overrides when you want to extend, not replace, parent behavior.
- Use `super().__init__()` in subclass constructors to ensure proper initialization.
- In multiple inheritance, always use `super()` to respect the MRO.
- Avoid calling parent methods directly by class name unless you have a specific reason.
- Document overridden methods and the use of `super()` in docstrings.

---

*Next: Advanced and practical examples of `super()` and method overriding will be added in the following step.*

---

## Advanced and Practical Examples: `super()` and Method Overriding

### Syllabus: Deep Dive into `super()` and Method Overriding

- Overriding instance methods, class methods, and static methods
- Using `super()` in single and multiple inheritance
- Method Resolution Order (MRO) and the C3 linearization algorithm
- Cooperative multiple inheritance and the diamond problem
- Overriding special (dunder) methods
- Calling parent methods with and without `super()`
- Overriding properties and descriptors
- Using `super()` in mixins and abstract base classes
- Common pitfalls and anti-patterns
- Real-world use cases: logging, validation, resource management, etc.

---

### 1. Overriding Instance, Class, and Static Methods

```python
class Base:
    def foo(self):
        print("Base.foo")
    @classmethod
    def bar(cls):
        print("Base.bar")
    @staticmethod
    def baz():
        print("Base.baz")

class Sub(Base):
    def foo(self):
        print("Sub.foo")
        super().foo()
    @classmethod
    def bar(cls):
        print("Sub.bar")
        super().bar()
    @staticmethod
    def baz():
        print("Sub.baz")
        Base.baz()

s = Sub()
s.foo()
Sub.bar()
Sub.baz()
# Sub.foo
# Base.foo
# Sub.bar
# Base.bar
# Sub.baz
# Base.baz
```

### 2. Using `super()` in Multiple Inheritance (Diamond Problem)

```python
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()
class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()
class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()
# Hello from D
# Hello from B
# Hello from C
# Hello from A
```

### 3. Method Resolution Order (MRO) and C3 Linearization

```python
class X: pass
class Y: pass
class A(X, Y): pass
class B(Y, X): pass
class C(A, B): pass

print(C.mro())
# [<class 'C'>, <class 'A'>, <class 'B'>, <class 'Y'>, <class 'X'>, <class 'object'>]
```

### 4. Overriding Special (Dunder) Methods

```python
class Base:
    def __str__(self):
        return "Base"
class Sub(Base):
    def __str__(self):
        return "Sub->" + super().__str__()

s = Sub()
print(str(s))  # Sub->Base
```

### 5. Overriding Properties and Using `super()`

```python
class Base:
    @property
    def value(self):
        return 10
class Sub(Base):
    @property
    def value(self):
        return super().value + 5

s = Sub()
print(s.value)  # 15
```

### 6. Calling Parent Methods Directly vs. with `super()`

```python
class Parent:
    def show(self):
        print("Parent.show")
class Child(Parent):
    def show(self):
        print("Child.show")
        Parent.show(self)  # direct call
        super().show()    # preferred

c = Child()
c.show()
# Child.show
# Parent.show
# Parent.show
```

### 7. Using `super()` in Mixins and Abstract Base Classes

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

### 8. Common Pitfall: Forgetting to Use `super()`

```python
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        # Missing super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
# d.name  # AttributeError: 'Dog' object has no attribute 'name'
```

### 9. Real-World Use Case: Logging and Validation

```python
class Base:
    def save(self):
        print("Saving to database...")
class Audited(Base):
    def save(self):
        print("Audit: Save called")
        super().save()

a = Audited()
a.save()
# Audit: Save called
# Saving to database...
```

### 10. Advanced: Cooperative Multiple Inheritance with `super()`

```python
class A:
    def do(self):
        print("A.do")
        super().do()
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
class Root:
    def do(self):
        print("Root.do")

D.__mro__ = (D, B, C, A, Root, object)
d = D()
d.do()
# D.do
# B.do
# C.do
# A.do
# Root.do
```

---
