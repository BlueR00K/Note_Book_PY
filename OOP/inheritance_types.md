
# Inheritance and Its Types in OOP (Python)

## Syllabus

1. Introduction: What is inheritance and why is it important?
2. Why use inheritance?
3. Basic inheritance syntax in Python
4. Types of inheritance
    - Single, multiple, multilevel, hierarchical, hybrid
5. Method Resolution Order (MRO)
6. Overriding and use of super()
7. Abstract Base Classes (ABC)
8. Best practices
9. Advanced and practical examples
10. Summary and key takeaways

---

## 1. Introduction

**Inheritance** is a core concept in Object-Oriented Programming (OOP) that allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). It promotes code reuse, extensibility, and logical hierarchy.

---

## 2. Why Use Inheritance?

- **Code Reuse:** Share common logic between classes.
- **Extensibility:** Add or override features in subclasses.
- **Hierarchy:** Model real-world relationships (e.g., Animal → Dog).
- **Polymorphism:** Treat objects of different subclasses uniformly.

---

## 3. Basic Inheritance Syntax in Python

```python
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    pass

c = Child()
c.greet()  # Inherits greet from Parent
```

---

## 4. Types of Inheritance

### 4.1. Single Inheritance

- A subclass inherits from one superclass.
- **Example:**

```python
class Animal:
    pass
class Dog(Animal):
    pass
```

---

### 4.2. Multiple Inheritance

- A subclass inherits from more than one superclass.
- **Example:**

```python
class Flyer:
    def fly(self):
        print("Flying...")
class Swimmer:
    def swim(self):
        print("Swimming...")
class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
```

---

### 4.3. Multilevel Inheritance

- A class is derived from a class which is also derived from another class (grandparent → parent → child).
- **Example:**

```python
class Grandparent:
    pass
class Parent(Grandparent):
    pass
class Child(Parent):
    pass
```

---

### 4.4. Hierarchical Inheritance

- Multiple subclasses inherit from the same superclass.
- **Example:**

```python
class Vehicle:
    pass
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
```

---

### 4.5. Hybrid Inheritance

- A combination of two or more types of inheritance.
- Can lead to complex hierarchies and the "diamond problem".
- **Example:**

```python
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
```

---

## 5. Method Resolution Order (MRO)

- Python uses the C3 linearization algorithm to determine the order in which base classes are searched when executing a method.
- Use `ClassName.__mro__` or `help(ClassName)` to inspect MRO.

---

## 6. Overriding and super()

- Subclasses can override parent methods.
- Use `super()` to call the parent method.

```python
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()
```

---

## 7. Abstract Base Classes (ABC)

- Use the `abc` module to define abstract classes and methods.
- Enforces implementation in subclasses.

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
```

---

## 8. Best Practices

- Use inheritance for "is-a" relationships, not for code sharing only.
- Prefer composition over inheritance for flexibility.
- Avoid deep or complex hierarchies.
- Document class relationships.
- Use ABCs for interfaces.

---

---

## 9. Advanced & Practical Examples

### 9.1. Single Inheritance: Customizing Behavior

```python
class Employee:
    def work(self):
        print("Working...")

class Developer(Employee):
    def work(self):
        print("Writing code!")

dev = Developer()
dev.work()  # Output: Writing code!
```

---

### 9.2. Multiple Inheritance: Mixins

```python
class JSONSerializable:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person, JSONSerializable):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

e = Employee("Alice", 123)
print(e.to_json())
```

---

### 9.3. Multilevel Inheritance: Extending Functionality

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Puppy(Dog):
    def speak(self):
        print("Yip!")

p = Puppy()
p.speak()  # Output: Yip!
```

---

### 9.4. Hierarchical Inheritance: Polymorphism

```python
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(4), Circle(3)]
for s in shapes:
    print(s.area())
```

---

### 9.5. Hybrid Inheritance: Diamond Problem and MRO

```python
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B, C):
    pass

d = D()
d.show()  # Output: B (MRO: D, B, C, A)
print(D.__mro__)
```

---

### 9.6. Abstract Base Class: Enforcing Interface

```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")

cat = Cat()
cat.make_sound()
```

---

---

## 10. Summary and Key Takeaways

- Inheritance enables code reuse, extensibility, and logical class hierarchies in OOP.
- Python supports single, multiple, multilevel, hierarchical, and hybrid inheritance.
- Method Resolution Order (MRO) determines how Python resolves method calls in complex hierarchies.
- Use `super()` for cooperative method calls and to avoid code duplication.
- Abstract Base Classes (ABCs) enforce interfaces and promote robust design.
- Prefer composition over inheritance for flexibility; avoid deep or complex hierarchies.
- Document class relationships and use inheritance for "is-a" relationships, not just for code sharing.
