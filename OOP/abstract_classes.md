# Abstract Classes in Python

## 1. Introduction and Syllabus

Abstract classes are a core concept in object-oriented programming, providing a way to define common interfaces and enforce implementation requirements for subclasses. In Python, abstract classes are implemented using the `abc` module, which allows you to define abstract methods and properties that must be overridden by concrete subclasses. Mastering abstract classes is essential for designing robust, extensible, and maintainable codebases.

### Syllabus

- What is an abstract class? (definition, motivation, and real-world analogy)
- The `abc` module and `ABC` base class
- Defining abstract methods and properties
- Instantiating abstract classes (and why you can't)
- Implementing concrete subclasses
- Abstract properties and class methods
- Best practices for interface design
- Common pitfalls and anti-patterns
- Real-world examples and advanced usage

---

## 2. What is an Abstract Class?

- An abstract class is a class that cannot be instantiated directly.
- It defines a common interface and may provide partial implementation.
- Subclasses must implement all abstract methods to become concrete (instantiable).

**Real-world analogy:** Think of an abstract class as a blueprint for a building. You can't live in a blueprint, but you can use it to build real houses (concrete subclasses).

---

## 3. The `abc` Module and `ABC` Base Class

- The `abc` module provides tools for defining abstract base classes (ABCs).
- Inherit from `abc.ABC` to make a class abstract.
- Use the `@abstractmethod` decorator to mark methods as abstract.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

---

## 4. Defining Abstract Methods and Properties

- Abstract methods must be implemented by subclasses.
- Abstract properties can be defined using `@property` and `@abstractmethod` together.

```python
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass
```

---

## 5. Instantiating Abstract Classes

- You cannot instantiate an abstract class directly.
- Attempting to do so raises a `TypeError`.
- Only concrete subclasses (with all abstract methods implemented) can be instantiated.

---

## 6. Implementing Concrete Subclasses

- Subclasses must override all abstract methods and properties.
- Once all are implemented, the subclass becomes concrete and can be instantiated.

```python
class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()  # Woof!
```

---

## 7. Abstract Properties and Class Methods

- You can define abstract properties and class methods using `@property`, `@classmethod`, and `@abstractmethod` together.

```python
class Base(ABC):
    @classmethod
    @abstractmethod
    def create(cls):
        pass
```

---

## 8. Best Practices for Interface Design

- Use abstract classes to define clear, minimal interfaces.
- Document the purpose and expected usage of each abstract method.
- Avoid adding implementation to abstract methods—keep them as contracts.
- Prefer composition and duck typing for flexibility, but use ABCs for formal contracts.

---

## 9. Common Pitfalls and Anti-Patterns

- Forgetting to implement all abstract methods in subclasses.
- Adding unnecessary implementation to abstract methods.
- Overusing abstract classes when simpler patterns suffice.
- Not documenting the interface and requirements.

---

## 10. Real-World Examples and Advanced Usage

### 1. Abstract Base Class with Multiple Concrete Subclasses

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car drives on the road.")

class Boat(Vehicle):
    def move(self):
        print("Boat sails on water.")

v1 = Car()
v2 = Boat()
v1.move()  # Car drives on the road.
v2.move()  # Boat sails on water.
```

---

### 2. Abstract Property and Concrete Implementation

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary

dev = Developer(100000)
print(dev.salary)  # 100000
```

---

### 3. Abstract Class with Class Method Contract

```python
from abc import ABC, abstractmethod

class Serializer(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass

class User(Serializer):
    def __init__(self, name):
        self.name = name
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'])

u = User.from_dict({'name': 'Alice'})
print(u.name)  # Alice
```

---

### 4. Edge Case: Instantiating an Incomplete Subclass

```python
class IncompleteDog(Animal):
    pass
# d = IncompleteDog()  # TypeError: Can't instantiate abstract class IncompleteDog with abstract method speak
```

---

### 5. Best Practice: Documenting Abstract Methods

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass
```

---

*These advanced examples show how to use abstract classes for interface design, property enforcement, class method contracts, and robust subclassing. Mastering abstract classes is key to building extensible and maintainable Python code.*
