# Creating Classes, Adding Attributes and Methods in Python (OOP)

## 1. Introduction

Classes are blueprints for creating objects in Python. They define the structure (attributes) and behavior (methods) that their instances (objects) will have.

---

## 2. Defining a Class

- Use the `class` keyword followed by the class name (CamelCase by convention).
- The class body contains method and attribute definitions.

```python
class Dog:
    pass
```

---

## 3. Creating Objects (Instances)

- Instantiate a class by calling it like a function: `obj = ClassName()`

```python
d = Dog()
print(type(d))  # <class '__main__.Dog'>
```

---

## 4. Instance Attributes

- Defined inside methods (usually `__init__`) using `self`.
- Unique to each object.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d = Dog("Buddy", 3)
print(d.name, d.age)
```

---

## 5. Methods

- Functions defined inside a class.
- The first parameter is always `self` (the instance).

```python
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
```

---

## 6. Class Attributes

- Shared by all instances of the class.
- Defined directly in the class body.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute
    def __init__(self, name):
        self.name = name

d1 = Dog("Buddy")
d2 = Dog("Max")
print(d1.species, d2.species)
```

---

## 7. Special Methods (`__init__`, `__str__`, etc.)

- `__init__`: Constructor, called when an object is created.
- `__str__`: Defines string representation for `print()`.
- `__repr__`: Official string representation (for debugging).

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog named {self.name}"

d = Dog("Buddy")
print(d)  # Output: Dog named Buddy
```

---

## 8. Adding and Modifying Attributes Dynamically

- You can add attributes to objects at runtime.

```python
class Cat:
    pass

c = Cat()
c.color = "black"
print(c.color)
```

---

## 9. Private and Protected Attributes (Naming Conventions)

- `_attr`: Protected (convention, not enforced)
- `__attr`: Name mangling for private attributes

```python
class Person:
    def __init__(self, name):
        self._nickname = name  # Protected
        self.__secret = "hidden"  # Private

p = Person("Alice")
print(p._nickname)
# print(p.__secret)  # AttributeError
print(p._Person__secret)  # Access via name mangling
```

---

## 10. Best Practices

- Use `self` for instance attributes and methods.
- Use class attributes for shared data.
- Use naming conventions for protected/private attributes.
- Keep methods focused and well-named.
- Document your classes and methods.

---

## 11. Advanced & Practical Examples

### 11.1. Class with Default and Optional Attributes

```python
class Car:
    wheels = 4  # Class attribute
    def __init__(self, make, model, color="black"):
        self.make = make
        self.model = model
        self.color = color

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic", color="red")
print(car1.make, car1.color)  # Toyota black
print(car2.make, car2.color)  # Honda red
```

---

### 11.2. Method Chaining

```python
class Builder:
    def __init__(self):
        self.parts = []
    def add(self, part):
        self.parts.append(part)
        return self  # Enables chaining
    def build(self):
        return f"Built: {', '.join(self.parts)}"

b = Builder().add("Engine").add("Wheels").add("Doors")
print(b.build())  # Output: Built: Engine, Wheels, Doors
```

---

### 11.3. Using Properties for Attribute Control

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

t = Temperature(25)
t.celsius = 0
# t.celsius = -300  # Raises ValueError
print(t.celsius)
```

---

### 11.4. Static and Class Methods

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
    @classmethod
    def description(cls):
        return f"This is {cls.__name__} class."

print(Math.add(2, 3))
print(Math.description())
```

---

### 11.5. Real-World Example: Bank Account

```python
class BankAccount:
    interest_rate = 0.02
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    def add_interest(self):
        self.balance += self.balance * self.interest_rate

acct = BankAccount("Alice", 1000)
acct.deposit(500)
acct.withdraw(200)
acct.add_interest()
print(acct.balance)
```

---

*These advanced examples show practical patterns for class design, attribute management, and method usage in Python OOP.*