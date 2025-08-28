# All Method Types in Python Classes

## 1. Introduction and Syllabus

Python supports several types of methods in classes, each with its own purpose, syntax, and use cases. Understanding the differences between instance methods, class methods, static methods, and special (dunder) methods is essential for writing clear, maintainable, and idiomatic Python code.

### Syllabus

- What is a method? (definition and motivation)
- Instance methods
- Class methods
- Static methods
- Special (dunder) methods
- Method resolution and binding
- When to use each method type
- Best practices and design patterns
- Common pitfalls and anti-patterns
- Real-world examples and advanced usage

---

## 2. What is a Method?

A method is a function defined inside a class that operates on instances or the class itself. Methods provide behavior to objects and can access or modify object or class state.

**Real-world analogy:** Think of a method as a button on a remote control—pressing different buttons (calling different methods) makes the device (object) do different things.

---

## 3. Instance Methods

- The most common method type in Python.
- Defined with `def` and take `self` as the first parameter.
- Operate on a specific instance of the class and can access/modify instance attributes.

```python
class Dog:
    def bark(self):
        print(f"{self} says woof!")
```

---

## 4. Class Methods

- Defined with the `@classmethod` decorator.
- Take `cls` (the class itself) as the first parameter.
- Can access/modify class state shared by all instances.
- Often used as alternative constructors or for operations that affect the class as a whole.

```python
class Dog:
    count = 0
    def __init__(self):
        Dog.count += 1
    @classmethod
    def how_many(cls):
        print(f"There are {cls.count} dogs.")
```

---

## 5. Static Methods

- Defined with the `@staticmethod` decorator.
- Do not take `self` or `cls` as the first parameter.
- Behave like plain functions but live in the class’s namespace for logical grouping.
- Cannot access or modify instance or class state.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

---

## 6. Special (Dunder) Methods

- Methods with double underscores before and after their names (e.g., `__init__`, `__str__`, `__call__`).
- Enable operator overloading and integration with Python’s built-in functions.
- Called implicitly by Python in certain situations.

```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person({self.name})"
```

---

## 7. Method Resolution and Binding

- Methods are bound to the instance or class when accessed.
- Python uses the Method Resolution Order (MRO) to determine which method to call in inheritance hierarchies.
- Unbound methods (accessed via the class) require explicit passing of the instance or class.

---

## 8. When to Use Each Method Type

- **Instance methods:** When you need to access or modify object state.
- **Class methods:** When you need to access or modify class state, or provide alternative constructors.
- **Static methods:** When the method does not need to access object or class state, but logically belongs to the class.
- **Special methods:** When you want to customize object behavior with operators or built-in functions.

---

## 9. Best Practices and Design Patterns

- Use the appropriate method type for clarity and maintainability.
- Document the purpose and expected usage of each method.
- Avoid using static methods when instance or class methods are more appropriate.
- Use special methods to make your objects more Pythonic and interoperable.

---

## 10. Common Pitfalls and Anti-Patterns

- Forgetting to use `self`, `cls`, or decorators.
- Using static methods when instance/class methods are needed (or vice versa).
- Overusing special methods without clear purpose.
- Not documenting method behavior and side effects.

---

## 11. Real-World Examples and Advanced Usage

### 1. Instance, Class, and Static Methods in One Class

```python
class Employee:
    company = "TechCorp"
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, I am {self.name} from {self.company}.")  # Instance method
    @classmethod
    def set_company(cls, name):
        cls.company = name  # Class method
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0  # Static method

e = Employee("Alice")
e.greet()
Employee.set_company("InnoSoft")
e2 = Employee("Bob")
e2.greet()
print(Employee.is_valid_name("Charlie"))
```

---

### 2. Alternative Constructors with Class Methods

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def from_string(cls, date_str):
        y, m, d = map(int, date_str.split("-"))
        return cls(y, m, d)

d = Date.from_string("2025-08-28")
print(d.year, d.month, d.day)
```

---

### 3. Static Methods for Utility Functions

```python
class MathUtils:
    @staticmethod
    def factorial(n):
        return 1 if n == 0 else n * MathUtils.factorial(n-1)

print(MathUtils.factorial(5))  # 120
```

---

### 4. Special Methods for Operator Overloading

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
print(v1 + v2)  # (4, 6)
```

---

### 5. Method Resolution Order (MRO) in Multiple Inheritance

```python
class A:
    def who(self):
        print("A")
class B(A):
    def who(self):
        print("B")
        super().who()
class C(A):
    def who(self):
        print("C")
        super().who()
class D(B, C):
    def who(self):
        print("D")
        super().who()

d = D()
d.who()
# Output:
# D
# B
# C
# A
```

---

### 6. Edge Case: Forgetting Decorators

```python
class Example:
    def static_method():
        print("This is not a static method!")

Example.static_method()  # TypeError: missing 1 required positional argument: 'self'
```

---

### 7. Best Practice: Documenting Method Types

```python
class MyClass:
    def instance_method(self):
        """Instance method: operates on an instance."""
        pass
    @classmethod
    def class_method(cls):
        """Class method: operates on the class."""
        pass
    @staticmethod
    def static_method():
        """Static method: utility, no access to class or instance."""
        pass
```

---

*These advanced examples show how to use all method types in Python classes to write clear, maintainable, and idiomatic code. Mastering method types is key to effective object-oriented programming in Python.*
