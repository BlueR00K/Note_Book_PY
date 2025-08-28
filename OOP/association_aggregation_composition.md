# Association, Aggregation, and Composition in OOP (Python)

## 1. Introduction

In Object-Oriented Programming (OOP), relationships between classes are fundamental for modeling real-world systems. Three key types of relationships are:

- **Association**
- **Aggregation**
- **Composition**

Understanding these helps you design robust, maintainable, and flexible code.

---

## 2. Association

- **Definition:** A general binary relationship between two classes, where objects of one class use or are connected to objects of another.
- **Characteristics:**
  - "Uses-a" or "knows-a" relationship
  - Both objects have independent lifecycles
  - Can be one-to-one, one-to-many, or many-to-many
- **Example:**
  - A `Teacher` and a `Department` (a teacher can belong to multiple departments)

### Python Example: Association

```python
class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name

# Association: teacher knows about department
math = Department("Mathematics")
alice = Teacher("Alice")
alice.department = math
```

---

## 3. Aggregation

- **Definition:** A special form of association representing a "whole-part" relationship, where the part can exist independently of the whole.
- **Characteristics:**
  - "Has-a" relationship
  - The container (whole) and contained (part) have independent lifecycles
  - Represented with a hollow diamond in UML
- **Example:**
  - A `Team` and `Player` (players can exist without a team)

### Python Example: Aggregation

```python
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)

# Aggregation: players can exist independently
john = Player("John")
team = Team("Sharks")
team.add_player(john)
```

---

## 4. Composition

- **Definition:** A strong form of aggregation where the part cannot exist independently of the whole. If the whole is destroyed, so are its parts.
- **Characteristics:**
  - "Owns-a" or "part-of" relationship
  - Lifecycles are tightly bound
  - Represented with a filled diamond in UML
- **Example:**
  - A `House` and its `Room`s (rooms do not exist without the house)

### Python Example: Composition

```python
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = [Room("Living Room"), Room("Bedroom")]

# Composition: rooms are created and destroyed with the house
my_house = House("123 Main St")
```

---

## 5. Comparison Table

| Relationship   | Lifecycles Independent? | Ownership Strength | Example         |
|----------------|------------------------|-------------------|-----------------|
| Association    | Yes                    | Weak              | Teacher-Dept    |
| Aggregation    | Yes                    | Medium            | Team-Player     |
| Composition    | No                     | Strong            | House-Room      |

---

## 6. Real-World Use Cases

- **Association:** Logging, event listeners, user and profile
- **Aggregation:** School and students, library and books
- **Composition:** Car and engine, document and paragraphs

---

## 7. Best Practices

---

## 8. Advanced & Practical Examples

### 8.1. Association: Event System Example

```python
# Association: Logger and Application
class Logger:
  def log(self, message):
    print(f"[LOG] {message}")

class Application:
  def __init__(self, logger):
    self.logger = logger  # Association
  def run(self):
    self.logger.log("Application started.")

logger = Logger()
app = Application(logger)
app.run()
```

---

### 8.2. Aggregation: School and Students

```python
class Student:
  def __init__(self, name):
    self.name = name

class School:
  def __init__(self, name):
    self.name = name
    self.students = []
  def enroll(self, student):
    self.students.append(student)

# Students can exist before/after school
alice = Student("Alice")
bob = Student("Bob")
school = School("Greenwood")
school.enroll(alice)
school.enroll(bob)
```

---

### 8.3. Composition: File System Example

```python
class File:
  def __init__(self, name, content):
    self.name = name
    self.content = content

class Folder:
  def __init__(self, name):
    self.name = name
    self.files = [File("readme.txt", "Welcome!"), File("data.csv", "id,value")]  # Composition

  def list_files(self):
    return [f.name for f in self.files]

folder = Folder("Project")
print(folder.list_files())
# If folder is deleted, files are deleted too (no external references)
```

---

### 8.4. Mixed Example: Library System

```python
class Book:
  def __init__(self, title):
    self.title = title

class Shelf:
  def __init__(self):
    self.books = []  # Aggregation: books can be moved between shelves
  def add_book(self, book):
    self.books.append(book)

class Library:
  def __init__(self):
    self.shelves = [Shelf() for _ in range(3)]  # Composition: shelves belong to library

book1 = Book("1984")
book2 = Book("Brave New World")
library = Library()
library.shelves[0].add_book(book1)
library.shelves[1].add_book(book2)
```

---

*These advanced examples show how association, aggregation, and composition are used in real-world Python OOP design.*
