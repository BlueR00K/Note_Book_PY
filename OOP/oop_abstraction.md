# 🐍 Abstraction in Python (Ultra Detailed)

## 🔹 Introduction

Abstraction is an OOP principle that **hides the internal implementation** of a class and exposes only the necessary features. It allows developers to focus on **what an object does** rather than **how it does it**.

In Python, abstraction is implemented using:

1. **Abstract Base Classes (ABC)**
2. **Interfaces via abstract methods**
3. **Encapsulation combined with abstraction**

---

## 🔹 Why Abstraction is Important

- Reduces **complexity** by hiding unnecessary details.
- Promotes **code reusability** and **modularity**.
- Enforces a **standard interface** for multiple implementations.
- Facilitates **maintenance** and **scalability**.

---

## 🔹 Abstract Base Classes (ABC)

Python provides the `abc` module to create abstract classes and methods.

### ✅ Basic Syntax

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass
```

### ✅ Implementing an Abstract Class

```python
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def stop_engine(self):
        print("Bike engine stopped")

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start_engine()
    v.stop_engine()
```

---

## 🔹 Key Points about ABC

- You **cannot instantiate** an abstract class directly.
- Subclasses must implement **all abstract methods**.
- Abstract classes can have **normal methods** as well:

```python
class Machine(ABC):
    @abstractmethod
    def operate(self):
        pass

    def info(self):
        print("This is a machine")
```

---

## 🔹 Abstraction vs Encapsulation

| Feature          | Encapsulation                          | Abstraction                                |
|-----------------|---------------------------------------|-------------------------------------------|
| Definition      | Bundling data and methods together    | Hiding implementation details             |
| Purpose         | Control access to data                 | Focus on what an object does             |
| Access          | Private/Protected variables            | Abstract methods, interface enforcement  |
| Implementation  | `_var`, `__var`                        | `abc` module, abstract classes            |

---

## 🔹 Practical Examples

### 📌 Example 1: Payment System

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

methods = [CreditCard(), PayPal()]
for method in methods:
    method.pay(100)
```

---

### 📌 Example 2: Shape Area Calculator

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14 * self.r

shapes = [Rectangle(4,5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
```

---

### 📌 Example 3: Employee Management with Abstraction

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_bonus(self):
        pass

class Developer(Employee):
    def get_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    def get_bonus(self):
        return self.salary * 0.2

employees = [Developer("Alice", 5000), Manager("Bob", 8000)]
for emp in employees:
    print(f"{emp.name} bonus: {emp.get_bonus()}")
```

---

## 🔹 Abstraction Tips and Best Practices

- Use **abstract classes** when multiple classes share a common interface.
- Keep abstract methods **minimal** and essential.
- Combine abstraction with **encapsulation** to hide sensitive data.
- Avoid implementing too many abstract classes; overuse can make the design complex.
- Always document abstract methods clearly.

---

## 🔹 Frequently Asked Questions

**Q1. Can an abstract class have a constructor?**  

- ✅ Yes, abstract classes can have `__init__` and regular methods.

**Q2. Can an abstract class have implemented methods?**  

- ✅ Yes, only abstract methods need to be implemented by subclasses.

**Q3. What happens if a subclass does not implement all abstract methods?**  

- ❌ Instantiation of that subclass will raise `TypeError`.

**Q4. Difference between abstract class and interface in Python?**  

- Python **doesn’t have formal interfaces**; abstract classes act as interfaces.  
- Interface emphasizes **method contracts only**, abstract classes can have attributes and concrete methods.

---

## 🔹 Summary

- Abstraction hides complexity and exposes only essential features.  
- Implemented via `abc` module, abstract classes, and methods.  
- Must be combined with **encapsulation** for effective OOP design.  
- Encourages **modularity, reusability, maintainability, and scalability**.  

✅ Mastering abstraction helps build robust, clean, and professional Python OOP applications.
