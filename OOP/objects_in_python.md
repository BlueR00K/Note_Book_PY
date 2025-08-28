# Objects in Python (OOP)

## 1. Introduction

An **object** is a core concept in Object-Oriented Programming (OOP). In Python, everything is an object: numbers, strings, functions, classes, and even modules. Objects are instances of classes and encapsulate data (attributes) and behavior (methods).

---

## 2. What is an Object?

- An object is an instance of a class.
- It bundles data (attributes) and functions (methods) together.
- Objects have identity, type, and value.

---

## 3. Creating Objects in Python

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} barks!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy barks!
```

---

## 4. Object Attributes and Methods

- **Attributes:** Variables that belong to the object (instance variables).
- **Methods:** Functions defined in the class that operate on the object.
- Access attributes/methods using dot notation: `object.attribute` or `object.method()`

---

## 5. The `self` Parameter

- Refers to the current instance of the class.
- Used to access attributes and methods from within the class.

---

## 6. Built-in Functions for Objects

- `type(obj)`: Returns the type of the object.
- `id(obj)`: Returns the unique identifier (memory address) of the object.
- `isinstance(obj, Class)`: Checks if `obj` is an instance of `Class`.
- `hasattr(obj, 'attr')`: Checks if the object has an attribute.
- `getattr(obj, 'attr', default)`: Gets the value of an attribute.
- `setattr(obj, 'attr', value)`: Sets the value of an attribute.
- `delattr(obj, 'attr')`: Deletes an attribute.

---

## 7. Object Lifecycle

- **Creation:** When an object is instantiated.
- **Usage:** While the object is referenced and used.
- **Destruction:** When no references remain, Python's garbage collector reclaims the memory.
- The `__del__` method can be defined for cleanup (rarely needed).

---

## 8. Special Methods (Magic/Dunder Methods)

- Methods with double underscores (e.g., `__init__`, `__str__`, `__len__`).
- Allow objects to implement and customize built-in behavior.

```python
class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(b)  # Output: Book: Python 101
```

---

## 9. Mutable vs Immutable Objects

- **Mutable:** Can be changed after creation (e.g., lists, dicts, sets, user-defined objects).
- **Immutable:** Cannot be changed after creation (e.g., int, float, str, tuple, frozenset).

---

## 10. Object Identity vs Equality

- `is`: Checks if two references point to the same object (identity).
- `==`: Checks if two objects have the same value (equality).

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True
print(x == y)  # True
print(x is z)  # False
print(x == z)  # True
```

---

## 11. Best Practices

- Use objects to encapsulate related data and behavior.
- Prefer composition over inheritance for code reuse.
- Use special methods to make objects more Pythonic.
- Document your classes and objects clearly.

---

## 12. Advanced & Practical Examples

### 12.1. Dynamic Attribute Assignment

```python
class DynamicObject:
    pass

obj = DynamicObject()
obj.name = "Dynamic"
obj.value = 42
print(obj.name, obj.value)  # Output: Dynamic 42
```

---

### 12.2. Customizing Object Behavior with Special Methods

```python
class Counter:
    def __init__(self, start=0):
        self.value = start
    def __add__(self, other):
        return Counter(self.value + other.value)
    def __str__(self):
        return f"Counter({self.value})"

c1 = Counter(5)
c2 = Counter(10)
c3 = c1 + c2
print(c3)  # Output: Counter(15)
```

---

### 12.3. Object Factories and Class Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))

p = Person.from_string("Alice,30")
print(p.name, p.age)  # Output: Alice 30
```

---

### 12.4. Using Objects as Function Arguments and Return Values

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def double_area(rect):
    return rect.area() * 2

r = Rectangle(3, 4)
print(double_area(r))  # Output: 24
```

---

### 12.5. Object Introspection and Reflection

```python
class Sample:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = Sample()
print(dir(obj))  # List all attributes and methods
print(hasattr(obj, 'x'))  # True
print(getattr(obj, 'y'))  # 20
setattr(obj, 'z', 99)
print(obj.z)  # 99
```

---

### 12.6. Real-World Example: Shopping Cart

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def total(self):
        return sum(item.price for item in self.items)

cart = Cart()
cart.add(Item("Book", 12.99))
cart.add(Item("Pen", 1.99))
print(cart.total())  # Output: 14.98
```

---

*These advanced examples show how objects are used dynamically, customized, and applied in real-world Python code.*
