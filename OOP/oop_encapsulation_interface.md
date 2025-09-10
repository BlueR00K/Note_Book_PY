
# Encapsulation, Data Hiding, and Interfaces in Python

## Syllabus

1. Introduction: What are encapsulation, data hiding, and interfaces?
2. Encapsulation
3. Data hiding
4. Interface in Python
5. Advanced and practical examples
6. Frequently asked questions
7. Summary and key takeaways

---

---

## 1. Introduction

Encapsulation and data hiding are **fundamental OOP principles** that help control access to data and methods within classes. In Python, while true access restriction doesn’t exist (everything is technically accessible), conventions and special mechanisms allow developers to achieve **controlled access**.

This note explores **Encapsulation, Data Hiding, and Interfaces** in Python in detail.

---

## 2. Encapsulation

Encapsulation is the process of **binding data (variables) and methods (functions) together into a single unit (class)**.

### Example

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand       # public attribute
        self._speed = speed      # protected (convention)
        self.__engine_on = False # private (name mangling)

    def start_engine(self):
        self.__engine_on = True
        print(f"{self.brand} engine started")

    def accelerate(self):
        if self.__engine_on:
            self._speed += 10
            print(f"{self.brand} accelerated to {self._speed} km/h")
        else:
            print("Engine is off!")

car = Car("Tesla", 0)
car.start_engine()
car.accelerate()
```

---

## 3. Data Hiding

Python does not enforce access control like Java or C++, but it **follows naming conventions** to indicate intent:

1. **Public Members** (default) – Accessible everywhere.
2. **Protected Members** (`_var`) – By convention, should not be accessed outside class/subclass.
3. **Private Members** (`__var`) – Name mangling makes it harder to access directly.

### Example

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500

# Trying to access private attribute directly
# print(acc.__balance)  # ❌ AttributeError
print(acc._BankAccount__balance)  # ✅ Name mangling access (not recommended)
```

✅ **Key Point:** Double underscore (`__var`) triggers **name mangling** → attribute internally becomes `_ClassName__var`.

---

## 4. Interface in Python

An **interface** defines a **contract** of methods that a class must implement. Python doesn’t have explicit interfaces like Java, but you can achieve them using:

1. **Abstract Base Classes (ABCs)** from the `abc` module
2. **Duck Typing** (if it behaves like a duck, it’s a duck!)

### Using Abstract Base Classes

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class Stripe(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ${amount} using Stripe")

# Usage
methods = [PayPal(), Stripe()]
for method in methods:
    method.pay(100)
```

### Using Duck Typing

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Woof!
animal_sound(Cat())  # Meow!
```

✅ **Key Point:** If an object implements the required methods, Python considers it valid regardless of its class hierarchy.

---

## 5. Advanced and Practical Examples: Encapsulation, Data Hiding, and Interfaces

### Example 1: ATM Machine Simulation

```python
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

atm = ATM(500)
print(atm.deposit(200))  # 700
print(atm.withdraw(300)) # 400
print(atm.get_balance()) # 400
```

---

### Example 2: Interface for Vehicles

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike started with a button")

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
```

---

## 6. Frequently Asked Questions

**Q1. What is the difference between encapsulation and data hiding?**  

- Encapsulation = Bundling data + methods into classes.  
- Data hiding = Restricting direct access to attributes (via `_` and `__` conventions).  

**Q2. Does Python truly support private variables?**  

- No, it uses **name mangling** (`_ClassName__var`) to discourage access, but not enforce it.  

**Q3. How are interfaces implemented in Python?**  

- Using `abc.ABC` (formal interfaces) or duck typing (informal interfaces).  

**Q4. When should I use abstract classes vs duck typing?**  

- Use **ABC** when you want a strict contract.  
- Use **duck typing** when you want flexibility and Pythonic style.  

---

## 7. Summary and Key Takeaways

- **Encapsulation** → Combines data and behavior in classes.
- **Data Hiding** → Achieved via naming conventions (`_var`, `__var`).
- **Interface** → Implemented via abstract classes or duck typing.
- **Private members** are not truly private, but name mangled.
- Abstraction and encapsulation together promote **modularity, reusability, and maintainability**.

✅ With this knowledge, you can confidently design **robust and secure OOP systems** in Python.

---
