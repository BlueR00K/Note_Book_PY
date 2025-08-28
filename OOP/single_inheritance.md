# Single Inheritance in Python

## 1. Introduction

Single inheritance is a fundamental concept in object-oriented programming (OOP) where a class (child/subclass) inherits attributes and methods from one parent (base/super) class. It enables code reuse, logical hierarchy, and extension of existing functionality.

---

## 2. What is Single Inheritance?

- In single inheritance, a subclass derives from only one superclass.
- The subclass inherits all public and protected members of the parent class.
- The subclass can override or extend the parent’s methods and attributes.

---

## 3. Syntax and Basic Example

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()  # Animal speaks
d.bark()   # Woof!
```

---

## 4. Overriding Methods

- The subclass can provide its own implementation of methods defined in the parent class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow!")

c = Cat()
c.speak()  # Meow!
```

---

## 5. Using `super()`

- The `super()` function allows you to call methods from the parent class.
- Useful for extending or customizing inherited behavior.

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

## 6. Best Practices

- Use single inheritance for clear, logical relationships.
- Prefer composition over inheritance if the relationship is not "is-a".
- Use `super()` to maintain parent class behavior when overriding methods.
- Document the inheritance hierarchy in class docstrings.
- Avoid deep inheritance chains for maintainability.

---

## Advanced and Practical Examples: Single Inheritance

### 1. Extending Parent Functionality

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def start(self):
        print(f"{self.make} {self.model} is starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car-specific startup checks complete.")

c = Car("Toyota", "Corolla")
c.start()
# Toyota Corolla is starting...
# Car-specific startup checks complete.
```

### 2. Inheriting and Overriding Attributes

```python
class Employee:
    def __init__(self, name):
        self.name = name
        self.role = "Employee"

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.role = "Manager"  # override attribute
        self.department = department

m = Manager("Alice", "IT")
print(m.name, m.role, m.department)
# Alice Manager IT
```

### 3. Using `super()` in Deep Inheritance Chains

```python
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")
class C(B):
    def greet(self):
        super().greet()
        print("Hello from C")

c = C()
c.greet()
# Hello from A
# Hello from B
# Hello from C
```

### 4. Type Checking and `isinstance`/`issubclass`

```python
class Animal:
    pass
class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))     # True
print(isinstance(d, Animal))  # True
print(issubclass(Dog, Animal))  # True
```

### 5. Customizing `__init__` and Calling Parent Initializer

```python
class Shape:
    def __init__(self, color):
        self.color = color
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

c = Circle("red", 5)
print(c.color, c.radius)
# red 5
```

### 6. Inheriting Methods and Adding New Ones

```python
class Writer:
    def write(self):
        print("Writing...")
class Blogger(Writer):
    def blog(self):
        print("Blogging...")

b = Blogger()
b.write()  # Writing...
b.blog()   # Blogging...
```

### 7. Using Docstrings to Document Inheritance

```python
class Animal:
    """Base class for all animals."""
    pass
class Dog(Animal):
    """Dog class, inherits from Animal."""
    pass
```

### 8. Edge Case: Overriding Methods Without Calling `super()`

```python
class Base:
    def greet(self):
        print("Hello from Base")
class Child(Base):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()  # Hello from Child
```

### 9. Using Single Inheritance for Code Reuse

```python
class Logger:
    def log(self, message):
        print(f"LOG: {message}")
class Service(Logger):
    def process(self):
        self.log("Processing started")

s = Service()
s.process()
# LOG: Processing started
```

### 10. Best Practice: Prefer Composition When Appropriate

```python
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()  # composition
    def start(self):
        self.engine.start()

c = Car()
c.start()
# Engine started
```

---
