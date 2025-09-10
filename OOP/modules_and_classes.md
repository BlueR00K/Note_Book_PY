
# Modules and Classes in Python

## Syllabus

1. Introduction: What are modules and classes, and why are they important?
2. What is a module?
3. What is a class?
4. Organizing classes in modules
5. Importing classes and modules
6. Best practices
7. Advanced and practical examples
8. Summary and key takeaways

---

## 1. Introduction

Modules and classes are fundamental building blocks for organizing and structuring Python code. Modules allow you to group related code into files, while classes enable object-oriented programming and encapsulation.

---

## 2. What is a Module?

- A **module** is any Python file (`.py`) that contains code (functions, classes, variables, etc.).
- Modules help organize code into logical, reusable components.
- You can import modules using the `import` statement.

### Example

```python
# file: math_utils.py
def add(a, b):
    return a + b
```

```python
# file: main.py
import math_utils
print(math_utils.add(2, 3))  # Output: 5
```

---

## 3. What is a Class?

- A **class** is a blueprint for creating objects (instances) with attributes and methods.
- Classes support encapsulation, inheritance, and polymorphism.

### Example

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving {self.make} {self.model}")

car = Car("Toyota", "Corolla")
car.drive()
```

---

## 4. Organizing Classes in Modules

- You can define multiple classes in a single module or split them across several modules for clarity.
- Use imports to access classes from other modules.

### Example

```python
# file: vehicles.py
class Car:
    ...
class Truck:
    ...
```

```python
# file: main.py
from vehicles import Car, Truck
car = Car(...)
truck = Truck(...)
```

---

## 5. Importing Classes and Modules

- Use `import module` or `from module import ClassName` to bring code into your script.
- You can use aliases with `as` for convenience.

### Example

```python
import math as m
print(m.sqrt(16))  # Output: 4.0
```

---

## 6. Best Practices

- Group related classes and functions in modules.
- Use descriptive module and class names.
- Avoid circular imports by careful module design.
- Keep modules focused and not too large.
- Document modules and classes with docstrings.

---

## 7. Advanced and Practical Examples: Modules and Classes

### Example 1: Creating a Custom Module with Multiple Classes and Functions

Suppose you have a module `shapes.py`:

```python
# shapes.py
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        from math import pi
        return pi * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

def describe_shape(shape):
    print(f"Area: {shape.area()}")
```

And use it in another file:

```python
# main.py
from shapes import Circle, Square, describe_shape
c = Circle(3)
s = Square(4)
describe_shape(c)  # Area: 28.274...
describe_shape(s)  # Area: 16
```

---

### Example 2: Using `__all__` to Control Module Exports

```python
# shapes.py
__all__ = ["Circle", "Square"]
class Circle: ...
class Square: ...
class _HiddenShape: ...  # Not exported
```

Now, `from shapes import *` will only import `Circle` and `Square`.

---

### Example 3: Importing with Aliases and Avoiding Name Conflicts

```python
import datetime as dt
now = dt.datetime.now()
print(now)
```

---

### Example 4: Organizing a Package with Multiple Modules

Suppose you have a package structure:

```
mypackage/
│   __init__.py
│   animals.py
│   vehicles.py
```

`animals.py`:

```python
class Dog: ...
class Cat: ...
```

`vehicles.py`:

```python
class Car: ...
class Bike: ...
```

`main.py`:

```python
from mypackage.animals import Dog
from mypackage.vehicles import Car
```

---

### Example 5: Dynamic Imports and the `importlib` Module

```python
import importlib
math_module = importlib.import_module("math")
print(math_module.sqrt(25))  # Output: 5.0

```

---

## 8. Summary and Key Takeaways

- Modules group related code and enable code reuse and organization.
- Classes provide blueprints for objects, supporting encapsulation and OOP.
- Use imports to access code across modules and packages.
- Organize code for clarity, avoid circular imports, and document modules/classes.
- Use advanced features like `__all__` and `importlib` for control and flexibility.
