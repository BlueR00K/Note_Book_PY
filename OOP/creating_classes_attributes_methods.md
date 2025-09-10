
# Creating Classes, Adding Attributes and Methods in Python (OOP)

## Syllabus

1. Introduction: What are classes, attributes, and methods in Python OOP?
2. Defining a class:
    - Syntax and naming conventions
    - Class body and indentation
3. Creating objects (instances):
    - Instantiation and object identity
4. Instance attributes:
    - Defining in `__init__`
    - Per-object state
5. Methods:
    - Instance methods and `self`
    - Method invocation
6. Class attributes:
    - Shared state
    - Access patterns
7. Special methods:
    - `__init__`, `__str__`, `__repr__`, and more
    - Customizing object behavior
8. Adding and modifying attributes dynamically:
    - Runtime attribute addition
    - Use cases and caveats
9. Private and protected attributes:
    - Naming conventions (`_attr`, `__attr`)
    - Name mangling and access control
10. Properties and attribute control:
    - Using `@property` for getters/setters
    - Validation and computed attributes
11. Static and class methods:
    - `@staticmethod` and `@classmethod`
    - Differences and use cases
12. Best practices:
    - Naming, documentation, and design
    - Avoiding anti-patterns
13. Advanced and practical examples:
    - Method chaining
    - Real-world class design
    - Combining features
14. Summary and key takeaways

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

## 10. Properties and Attribute Control

- Use the `@property` decorator to create managed attributes (getters/setters).
- Properties allow validation, computed values, and encapsulation.

```python
class Celsius:
    def __init__(self, temp):
        self._temp = temp
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._temp = value

c = Celsius(25)
c.temp = 0
# c.temp = -300  # Raises ValueError
print(c.temp)
```

---

## 11. Static and Class Methods

- Use `@staticmethod` for utility functions that do not access class or instance state.
- Use `@classmethod` for alternative constructors or methods that operate on the class itself.
- Static and class methods are called on the class, not the instance.

```python
class Example:
    @staticmethod
    def add(x, y):
        return x + y
    @classmethod
    def from_string(cls, s):
        name, age = s.split(',')
        return cls(name, int(age))
```

---

## 12. Best Practices

- Use `self` for instance attributes and methods.
- Use class attributes for shared data.
- Use naming conventions for protected/private attributes.
- Use properties for validation and encapsulation.
- Use static/class methods appropriately.
- Keep methods focused and well-named.
- Document your classes and methods with docstrings.
- Avoid anti-patterns like excessive dynamic attributes or unclear naming.

---

---

## 13. Advanced & Practical Examples

### 13.1. Class with Default and Optional Attributes

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

### 13.2. Method Chaining

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

### 13.3. Using Properties for Attribute Control

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

### 13.4. Static and Class Methods

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

### 13.5. Real-World Example: Bank Account

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

---

## 14. Summary and Key Takeaways

- Classes define the structure and behavior of objects in Python.
- Use instance attributes for per-object state and class attributes for shared state.
- Methods define object behavior; use special methods to customize built-in operations.
- Properties provide controlled access and validation for attributes.
- Use static and class methods for utility and alternative constructors.
- Follow best practices for naming, documentation, and design.
- Combine these features for robust, maintainable, and Pythonic OOP code.
