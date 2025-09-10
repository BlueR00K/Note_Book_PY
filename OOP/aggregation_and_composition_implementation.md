
# Aggregation and Composition in Python

## Syllabus

1. Introduction: What are aggregation and composition?
2. Motivation and real-world analogies
3. Key differences: aggregation vs. composition
4. When to use aggregation vs. composition
5. Implementing aggregation in Python (patterns, code)
6. Implementing composition in Python (patterns, code)
7. Managing object lifecycles and ownership
8. Best practices for class relationships
9. Common pitfalls and anti-patterns
10. Advanced and practical examples
11. Summary and key takeaways

---

## 1. Introduction

Aggregation and composition are two fundamental object-oriented design principles for modeling relationships between classes. They describe how objects can be built from other objects, and how lifecycles and ownership are managed. Understanding and implementing these patterns is essential for designing robust, maintainable, and expressive Python code.

---

## 2. What are Aggregation and Composition?

- **Aggregation:** A "has-a" relationship where the child (part) can exist independently of the parent (whole). The parent holds a reference to the child, but does not own its lifecycle.
- **Composition:** A stronger "owns-a" relationship where the child cannot exist independently of the parent. The parent is responsible for creating and destroying the child.

**Real-world analogy:**

- Aggregation: A university and its students. Students can exist independently of the university.
- Composition: A house and its rooms. Rooms do not exist independently of the house.

---

---

## 3. Aggregation vs. Composition: Key Differences

- **Lifecycle:** In aggregation, the part can outlive the whole. In composition, the part is destroyed with the whole.
- **Ownership:** Aggregation implies shared ownership; composition implies exclusive ownership.
- **Implementation:** Aggregation uses references to external objects; composition creates and manages internal objects.

---

---

## 4. When to Use Aggregation vs. Composition

- Use aggregation when objects can be shared or reused elsewhere.
- Use composition when the parent should fully control the child’s lifecycle.
- Prefer composition for strong ownership and encapsulation.

---

---

## 5. Implementing Aggregation in Python

- Pass existing objects as arguments to the parent’s constructor or methods.
- The parent stores references but does not create or destroy the child.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Aggregation: engine can exist independently
    def drive(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.drive()
```

---

---

## 6. Implementing Composition in Python

- The parent creates and manages the child object(s) internally.
- The child’s lifecycle is tied to the parent.

```python
class Wheel:
    def rotate(self):
        print("Wheel rotating")

class Bicycle:
    def __init__(self):
        self.front_wheel = Wheel()
        self.rear_wheel = Wheel()
    def ride(self):
        self.front_wheel.rotate()
        self.rear_wheel.rotate()

bike = Bicycle()
bike.ride()
```

---

---

## 7. Managing Object Lifecycles and Ownership

- In aggregation, deleting the parent does not affect the child.
- In composition, deleting the parent should also delete or invalidate the child.
- Use `__del__` or context managers for explicit resource management if needed.

---

---

## 8. Best Practices for Class Relationships

- Prefer composition for strong ownership and encapsulation.
- Use aggregation for shared resources or loose coupling.
- Document the relationship and ownership model in class docstrings.
- Avoid circular references and memory leaks.

---

---

## 9. Common Pitfalls and Anti-Patterns

- Confusing aggregation with composition (mixing lifecycles)
- Overusing aggregation for objects that should be composed
- Not documenting ownership and lifecycle expectations
- Creating unnecessary dependencies between unrelated classes

---

---

## 10. Advanced and Practical Examples: Aggregation and Composition

### 1. Aggregation: Shared Resource Example

```python
class Printer:
    def print_document(self, doc):
        print(f"Printing: {doc}")

class Office:
    def __init__(self, printer):
        self.printer = printer  # Aggregation: shared printer
    def print_report(self):
        self.printer.print_document("Office Report")

shared_printer = Printer()
office1 = Office(shared_printer)
office2 = Office(shared_printer)
office1.print_report()
office2.print_report()
```

---

---

### 2. Composition: Parent Owns and Manages Parts

```python
class CPU:
    def compute(self):
        print("CPU computing...")

class Computer:
    def __init__(self):
        self.cpu = CPU()  # Composition: Computer owns CPU
    def run(self):
        self.cpu.compute()

pc = Computer()
pc.run()
```

---

---

### 3. Aggregation with Lifecycle Independence

```python
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)

book = Book("Python 101")
library = Library()
library.add_book(book)
del library  # Book still exists
print(book.title)  # Python 101
```

---

---

### 4. Composition with Resource Cleanup

```python
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
    def write(self, text):
        self.file.write(text)
    def __del__(self):
        print("Closing file...")
        self.file.close()

class Logger:
    def __init__(self, filename):
        self.handler = FileHandler(filename)
    def log(self, message):
        self.handler.write(message + '\n')

logger = Logger('log.txt')
logger.log('Hello!')
del logger  # Closing file...
```

---

---

### 5. Best Practice: Documenting Relationships

```python
class Engine:
    """Engine can be shared (aggregation)."""
    pass
class Car:
    """Car aggregates Engine; does not own its lifecycle."""
    def __init__(self, engine):
        self.engine = engine
```

---

---

## 11. Summary and Key Takeaways

- Aggregation and composition model real-world relationships between classes
- Use aggregation for shared or loosely coupled objects; use composition for strong ownership
- Manage object lifecycles and document relationships clearly
- Avoid common pitfalls such as mixing lifecycles or creating unnecessary dependencies
- Use advanced patterns for resource management and robust design

---
