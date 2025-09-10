
# Object-Oriented Programming (OOP) in Python

## Syllabus

1. Introduction: What is OOP and why is it important?
2. Core OOP concepts: encapsulation, abstraction, inheritance, polymorphism
3. Classes and objects
4. Constructors and destructors
5. Class vs. instance variables
6. Method types: instance, class, static
7. Dunder (magic) methods
8. Multiple inheritance and MRO
9. Best practices and anti-patterns
10. Advanced and practical examples
11. Summary and key takeaways

---

---

## 1. Introduction

Object-Oriented Programming (OOP) is a paradigm that organizes software design around **objects** rather than functions and logic. Objects represent **real-world entities**, and OOP provides a clear structure for code that is **reusable, modular, and easier to maintain**.

---

## 2. Core Concepts of OOP

Python supports all major OOP principles. The four pillars are:

1. **Encapsulation**
2. **Abstraction**
3. **Inheritance**
4. **Polymorphism**

---

### 2.1 Encapsulation

Encapsulation means **bundling data and methods** that operate on that data into a single unit (class). It also restricts direct access to some components.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.get_balance())  # 150
```

✅ **Key Point:** Private members in Python are indicated with a leading underscore (`_var`) or double underscore (`__var`).

---

### 2.2 Abstraction

Abstraction means **hiding implementation details** and showing only the essential features.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())  # 78.5
```

✅ **Key Point:** Python uses the `abc` module to define abstract base classes.

---

### 2.3 Inheritance

Inheritance allows a class to **reuse code** from another class (parent/child relationship).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

✅ **Key Point:** Supports single, multiple, and multilevel inheritance.

---

### 2.4 Polymorphism

Polymorphism allows different classes to use the **same interface** but provide different implementations.

```python
animals = [Dog("Rex"), Cat("Luna")]

for animal in animals:
    print(f"{animal.name} says {animal.speak()}")
```

✅ **Key Point:** Methods with the same name can behave differently depending on the object.

---

## 3. Classes and Objects

### 3.1 Classes and Objects

- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Tesla", "Model S")
print(my_car.brand, my_car.model)
```

---

## 4. Constructors and Destructors

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

p = Person("Alice")
del p
```

---

## 5. Class vs. Instance Variables

```python
class Student:
    school = "Python Academy"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Alice")
s2 = Student("Bob")
print(s1.school, s2.school)  # Python Academy Python Academy
```

---

## 6. Method Types

1. **Instance Method** – works with object instance
2. **Class Method** – works with class (declared with `@classmethod`)
3. **Static Method** – independent of class/object (declared with `@staticmethod`)

```python
class Math:
    def instance_method(self):
        return "Instance method called"

    @classmethod
    def class_method(cls):
        return "Class method called"

    @staticmethod
    def static_method():
        return "Static method called"

m = Math()
print(m.instance_method())
print(Math.class_method())
print(Math.static_method())
```

---

## 7. Dunder (Magic) Methods

Python provides special methods to customize class behavior.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("Python Mastery", "John Doe")
print(book)        # Python Mastery by John Doe
print(len(book))   # 14
```

---

## 8. Multiple Inheritance & MRO (Method Resolution Order)

```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Hello from A (Python follows MRO)
```

---

## 10. Advanced and Practical Examples: OOP in Python

### Example 1: Simple Employee Management

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f"{self.name} earns {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def info(self):
        return f"Manager {self.name} manages {self.department} department"

e1 = Employee("Alice", 40000)
m1 = Manager("Bob", 60000, "IT")

print(e1.info())
print(m1.info())
```

### Example 2: Shape Area Calculator

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

shapes = [Rectangle(4,5), Circle(3)]
for shape in shapes:
    print(shape.area())
```

---

---

## 11. Summary and Key Takeaways

- Encapsulation: Data hiding using classes.
- Abstraction: Hiding implementation details.
- Inheritance: Code reusability across classes.
- Polymorphism: Same interface, different behavior.
- Classes define blueprints, objects are instances.
- Python supports dunder methods, multiple inheritance, and different method types.
- With OOP, Python programs become modular, maintainable, and closer to real-world modeling.

- **Encapsulation** → Data hiding using classes.
- **Abstraction** → Hiding implementation details.
- **Inheritance** → Code reusability across classes.
- **Polymorphism** → Same interface, different behavior.
- Classes define blueprints, objects are instances.
- Python supports dunder methods, multiple inheritance, and different method types.

✅ With OOP, Python programs become modular, maintainable, and closer to real-world modeling.
