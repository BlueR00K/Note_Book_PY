
# Attribute Types in Python Classes

## Syllabus

1. Introduction: What are attribute types in Python classes?
2. Instance attributes: definition, usage, and examples
3. Class attributes: definition, usage, and examples
4. Static attributes: concept and Pythonic approach
5. Dynamic attributes: runtime addition and caveats
6. Properties (managed attributes): getter/setter, validation, and computed values
7. Private and protected attributes: naming conventions and access control
8. Attribute resolution order (MRO)
9. Using __slots__ to restrict attributes
10. Descriptor protocol for advanced attribute management
11. Best practices for attribute design and documentation
12. Advanced and practical examples
13. Summary and key takeaways

## 1. Introduction

Attributes in Python classes define the state and behavior of objects. Understanding the different types of attributes and their usage is essential for writing robust, maintainable, and idiomatic Python code.

## 2. Types of Attributes in Classes

### 2.1 Instance Attributes

- Defined inside methods (usually `__init__`) using `self`.
- Unique to each object instance.

```python
class Person:
    def __init__(self, name):
        self.name = name  # instance attribute
```

### 2.2 Class Attributes

- Defined directly in the class body, outside any method.
- Shared by all instances of the class.

```python
class Dog:
    species = "Canis familiaris"  # class attribute
    def __init__(self, name):
        self.name = name
```

### 2.3 Static Attributes (Static Variables)

- In Python, class attributes serve as static variables.
- Accessed via the class or instance, but only one copy exists.

### 2.4 Dynamic Attributes

- Added to instances at runtime, not defined in the class body.

```python
p = Person("Alice")

```

### 2.5 Properties (Managed Attributes)

- Use the `@property` decorator to define getter/setter logic.
- Allow controlled access to private data.

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def area(self):
        return self._width * self._height
```

### 2.6 Private and Protected Attributes

- Use `_attr` for protected and `__attr` for private (name-mangled) attributes.

## 3. Attribute Resolution Order

- Python looks for attributes in the following order:
    1. Instance attributes
    2. Class attributes
    3. Parent classes (MRO)

## 4. Best Practices

- Use instance attributes for per-object state.
- Use class attributes for shared constants or defaults.
- Use properties for validation or computed values.
- Avoid excessive use of dynamic attributes.
- Use naming conventions for protected/private attributes.
- Document all attributes clearly in class docstrings.

## 5. Advanced and Practical Examples

- Use instance attributes for per-object state.
- Use class attributes for shared constants or defaults.
- Use properties for validation or computed values.
- Avoid excessive use of dynamic attributes.
- Use naming conventions for protected/private attributes.
- Document all attributes clearly in class docstrings.

## 6. Summary and Key Takeaways

- Python classes support several attribute types: instance, class, static, dynamic, properties, and private/protected.
- Use the correct attribute type for clarity, maintainability, and robust design.
- Properties and descriptors enable advanced attribute management.
- Document and structure your attributes for best results.

Mastering attribute types is key to effective object-oriented programming in Python.

## Advanced and Practical Examples: Attribute Types in Python Classes

### 1. Instance vs. Class Attributes in Practice

```python
class Counter:
    count = 0  # class attribute
    def __init__(self):
        Counter.count += 1
        self.instance_id = Counter.count  # instance attribute

a = Counter()
b = Counter()
print(a.instance_id)  # 1
print(b.instance_id)  # 2
print(Counter.count)  # 2
```

### 2. Dynamic Attributes and Their Pitfalls

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Alice")
u.age = 30  # dynamic attribute
print(u.age)  # 30
# print(User.age)  # AttributeError

v = User("Bob")
# print(v.age)  # AttributeError: 'User' object has no attribute 'age'
```

### 3. Properties for Validation and Computed Values

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
```

### 4. Private and Protected Attributes in Inheritance

```python
class Base:
    def __init__(self):
        self._protected = "protected"
        self.__private = "private"

class Child(Base):
    def show(self):
        print(self._protected)  # Allowed (convention)
        # print(self.__private)  # AttributeError
        print(self._Base__private)  # Name mangling

c = Child()
c.show()
```

### 5. Using `__slots__` to Restrict Dynamic Attributes

```python
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
# p.z = 3  # AttributeError: 'Point' object has no attribute 'z'
```

### 6. Class Attributes as Shared State

```python
class Config:
    debug = True

a = Config()
b = Config()
Config.debug = False
print(a.debug)  # False
print(b.debug)  # False
a.debug = True  # Creates an instance attribute for 'a' only
print(a.debug)  # True
print(b.debug)  # False
print(Config.debug)  # False
```

### 7. Documenting Attributes with Docstrings and Type Hints

```python
class Employee:
    """Represents an employee.

    Attributes:
        name (str): The employee's name.
        id (int): The employee's ID.
        department (str): The department name.
    """
    def __init__(self, name: str, id: int, department: str):
        self.name = name
        self.id = id
        self.department = department
```

### 8. Using Properties for Read-Only and Write-Only Attributes

```python
class Account:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Negative balance not allowed")
        self._balance = value

acc = Account(100)
print(acc.balance)  # 100
acc.balance = 200
# acc.balance = -50  # Raises ValueError
```

### 9. Using Class Methods to Access/Modify Class Attributes

```python
class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
    @classmethod
    def get_count(cls):
        return cls.count

Counter.increment()
print(Counter.get_count())  # 1
```

### 10. Advanced: Descriptor Protocol for Managed Attributes

```python
class Positive:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self.name] = value

class Product:
    price = Positive("price")
    def __init__(self, price):
        self.price = price

p = Product(10)
# p.price = -5  # Raises ValueError
```

---
