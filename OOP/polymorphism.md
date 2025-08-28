# Polymorphism in OOP (Python)

## 1. Introduction

**Polymorphism** is a fundamental concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types).

---

## 2. Why Use Polymorphism?

- **Flexibility:** Write code that works with objects of different types.
- **Extensibility:** Add new classes with minimal changes to existing code.
- **Code Reuse:** Use the same function or method for different types.
- **Decoupling:** Reduce dependencies between components.

---

## 3. Types of Polymorphism

### 3.1. Compile-Time (Static) Polymorphism

- Achieved via method overloading (not natively supported in Python, but can be mimicked with default arguments or `*args`/`**kwargs`).

### 3.2. Run-Time (Dynamic) Polymorphism

- Achieved via method overriding and duck typing (core to Python).

---

## 4. Method Overriding (Dynamic Polymorphism)

- Subclasses provide a specific implementation of a method defined in the parent class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Calls the overridden method
```

---

## 5. Duck Typing in Python

- "If it walks like a duck and quacks like a duck, it’s a duck."
- Python cares about methods/attributes, not the object's actual type.

```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def make_it_fly(flier):
    flier.fly()

make_it_fly(Bird())
make_it_fly(Airplane())
```

---

## 6. Operator Overloading (Special Methods)

- Python allows classes to define their own behavior for built-in operators by implementing special methods (e.g., `__add__`, `__str__`).

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
print(v1 + v2)  # Output: (4, 6)
```

---

## 7. Polymorphism with Abstract Base Classes

- Use the `abc` module to define a common interface.

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

def print_area(shape):
    print(shape.area())

print_area(Square(5))
print_area(Circle(3))
```

---

## 8. Best Practices

- Use polymorphism to write flexible, extensible, and maintainable code.
- Prefer duck typing and interfaces over type checks.
- Use ABCs for formal interfaces when needed.
- Avoid unnecessary complexity—keep interfaces simple.

---

---

## 9. Advanced & Practical Examples

### 9.1. Polymorphic Collections

```python
class TextFile:
    def read(self):
        return "Reading text file"

class CSVFile:
    def read(self):
        return "Reading CSV file"

files = [TextFile(), CSVFile()]
for f in files:
    print(f.read())  # Polymorphic call
```

---

### 9.2. Function Polymorphism with *args and **kwargs

```python
def add(*args):
    return sum(args)

print(add(1, 2))
print(add(1, 2, 3, 4))
```

---

### 9.3. Real-World Example: Payment System

```python
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with credit card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with PayPal.")

def process_payment(method, amount):
    method.pay(amount)

process_payment(CreditCard(), 100)
process_payment(PayPal(), 50)
```

---

### 9.4. Polymorphism in Built-in Functions

```python
print(len([1, 2, 3]))      # List
print(len("hello"))       # String
print(len({1: "a", 2: "b"}))  # Dictionary
```

---

### 9.5. Polymorphism with Iterators

```python
for item in [1, 2, 3]:
    print(item)
for char in "abc":
    print(char)
for key in {1: "a", 2: "b"}:
    print(key)
```

---

*These advanced examples show how polymorphism is used in real-world Python code, from collections to interfaces and built-in functions.*
