
# Polymorphism in OOP (Python)

## 1. Introduction and Syllabus

Polymorphism is one of the four pillars of Object-Oriented Programming (OOP), alongside encapsulation, inheritance, and abstraction. In Python, polymorphism allows you to write code that can work with objects of different types, as long as they provide the required interface (methods/attributes). This makes your code more flexible, extensible, and easier to maintain.

Polymorphism is not just a theoretical concept—it is a practical tool for building reusable and adaptable software. Understanding how Python implements polymorphism, and how to use it effectively, is essential for any serious Python developer.

### Syllabus

- What is polymorphism? (definition, motivation, and real-world analogy)
- Why is polymorphism important in OOP?
- Types of polymorphism: compile-time (static) vs. run-time (dynamic)
- Method overriding and dynamic dispatch
- Duck typing and the Pythonic approach
- Operator overloading and special methods
- Polymorphism with abstract base classes (ABCs)
- Polymorphic collections and functions
- Best practices and common pitfalls
- Real-world and advanced examples

---

## 2. Why Use Polymorphism?

Polymorphism enables you to:

- **Write flexible code:** Functions and methods can operate on objects of different classes, as long as they implement the expected interface.
- **Promote extensibility:** You can add new classes or types without modifying existing code, following the Open/Closed Principle.
- **Encourage code reuse:** The same function or method can be used for different types, reducing duplication.
- **Decouple components:** Code that relies on interfaces rather than concrete types is easier to test, maintain, and extend.

**Real-world analogy:** Think of a universal remote control. It can operate different brands of TVs, DVD players, and sound systems, as long as each device understands the remote's signals. The remote is polymorphic—it works with many types of devices.

---

## 3. Types of Polymorphism

Polymorphism can be broadly classified into two types:

### 3.1. Compile-Time (Static) Polymorphism

- In some languages, this is achieved via method overloading (multiple methods with the same name but different signatures). Python does not support true method overloading, but you can mimic it using default arguments, `*args`, and `**kwargs`.

### 3.2. Run-Time (Dynamic) Polymorphism

- This is the primary form of polymorphism in Python. It is achieved through method overriding (subclasses redefine methods of their parent class) and duck typing (an object's suitability is determined by the presence of certain methods and properties, rather than the object's type).

---

## 4. Method Overriding (Dynamic Polymorphism)

Method overriding is a key mechanism for achieving polymorphism in Python. When a subclass provides its own implementation of a method that is already defined in its superclass, the subclass's version is used. This allows you to call the same method on different objects and get behavior appropriate to their class.

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

Python is a dynamically typed language and embraces the philosophy of "duck typing":

> "If it walks like a duck and quacks like a duck, it’s a duck."

This means that Python cares about whether an object has the required methods and attributes, not about the object's actual type. If an object implements the expected interface, it can be used in place of any other object with the same interface.

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

Python allows you to define how objects of your classes behave with built-in operators (like `+`, `-`, `*`, etc.) by implementing special methods (also called "dunder" methods, e.g., `__add__`, `__str__`). This is a form of polymorphism, as the same operator can have different meanings depending on the types of its operands.

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

Sometimes, you want to enforce that certain methods are implemented by all subclasses. Python provides the `abc` module (Abstract Base Classes) for this purpose. By defining an abstract base class, you can specify a common interface that all subclasses must implement. This is useful for large projects and frameworks where formal contracts are important.

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

- Use polymorphism to write code that is flexible, extensible, and easy to maintain.
- Prefer duck typing and interfaces over explicit type checks (e.g., avoid `isinstance()` unless necessary).
- Use abstract base classes (ABCs) when you need to enforce a contract or interface.
- Keep interfaces simple and focused—avoid adding unnecessary methods.
- Document the expected interface for your classes and functions.
- Test your code with different types to ensure true polymorphic behavior.

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

---

*These advanced examples show how polymorphism is used in real-world Python code, from collections to interfaces and built-in functions. Mastering polymorphism will make your code more Pythonic, robust, and adaptable to change.*
