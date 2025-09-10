
# LBYL, EAFP, and Duck Typing in Python

## Syllabus

1. Introduction: What are LBYL, EAFP, and duck typing, and why are they important?
2. What are LBYL and EAFP?
3. The role of exceptions in Pythonic code
4. Duck typing: philosophy and practice
5. LBYL vs. EAFP: pros, cons, and when to use each
6. Writing robust code with EAFP and duck typing
7. Common pitfalls and anti-patterns
8. Advanced and practical examples
9. Summary and key takeaways

---

## 1. Introduction

Python encourages a unique approach to error handling and interface design, summarized by the idioms "LBYL" (Look Before You Leap) and "EAFP" (Easier to Ask Forgiveness than Permission). These philosophies are closely related to Python's dynamic nature and its embrace of duck typing. Understanding these concepts is essential for writing idiomatic, robust, and maintainable Python code.

---

## 2. What are LBYL and EAFP?

- **LBYL (Look Before You Leap):** Check conditions explicitly before performing an operation.
- **EAFP (Easier to Ask Forgiveness than Permission):** Try the operation directly and handle exceptions if it fails.

**Real-world analogy:**

- LBYL: Checking if a door is unlocked before trying to open it.
- EAFP: Trying to open the door and dealing with it if it’s locked.

---

## 3. The Role of Exceptions in Pythonic Code

- Python uses exceptions extensively for error handling.
- EAFP is preferred in idiomatic Python because it leads to cleaner, more readable code, especially in the presence of duck typing.
- LBYL can be useful when exceptions are expensive or undesirable.

---

## 4. Duck Typing: Philosophy and Practice

- "If it walks like a duck and quacks like a duck, it’s a duck."
- Python focuses on whether an object implements the required methods/attributes, not its type.
- EAFP and duck typing go hand-in-hand: try to use an object as intended, and handle exceptions if it doesn’t support the required interface.

---

## 5. LBYL vs. EAFP: Pros, Cons, and When to Use Each

### LBYL Example

```python
if hasattr(obj, 'read'):
    data = obj.read()
else:
    raise AttributeError('Object does not support read()')
```

### EAFP Example

```python
try:
    data = obj.read()
except AttributeError:
    raise AttributeError('Object does not support read()')
```

- **LBYL Pros:**
  - Can avoid exceptions in performance-critical code
  - Sometimes clearer when multiple conditions must be checked
- **LBYL Cons:**
  - Race conditions: the state can change between the check and the action
  - More verbose and less idiomatic in Python
- **EAFP Pros:**
  - More concise and Pythonic
  - Works naturally with duck typing
  - Avoids race conditions
- **EAFP Cons:**
  - Can obscure the source of errors if exceptions are not handled carefully
  - May be less efficient if exceptions are common

---

## 6. Writing Robust Code with EAFP and Duck Typing

- Use EAFP for most operations on objects whose interface you expect, not their type.
- Catch only the exceptions you expect and can handle.
- Document the expected interface for your functions and classes.
- Use LBYL when exceptions are expensive or when you need to check multiple conditions atomically.

---

## 7. Common Pitfalls and Anti-Patterns

- Catching broad exceptions (e.g., `except Exception`) can hide bugs.
- Using LBYL and EAFP together can lead to redundant or confusing code.
- Overusing LBYL can make code less Pythonic and more error-prone.

---

## 8. Advanced and Practical Examples: LBYL, EAFP, and Duck Typing

### 1. File Handling: LBYL vs. EAFP

#### LBYL

```python
import os
filename = 'data.txt'
if os.path.exists(filename):
  with open(filename) as f:
    data = f.read()
else:
  print('File does not exist')
```

#### EAFP (Preferred in Python)

```python
try:
  with open('data.txt') as f:
    data = f.read()
except FileNotFoundError:
  print('File does not exist')
```

---

### 2. Duck Typing in Practice: Polymorphic APIs

```python
def process(item):
  # EAFP: just try to use the interface
  try:
    item.do_work()
  except AttributeError:
    print('Object does not support do_work()')

class Task:
  def do_work(self):
    print('Task completed!')

process(Task())  # Task completed!
process(42)      # Object does not support do_work()
```

---

### 3. Avoiding Race Conditions: Why EAFP is Safer

```python
# LBYL (unsafe in concurrent environments)
if key in my_dict:
  value = my_dict[key]  # Key could be deleted by another thread here

# EAFP (safe)
try:
  value = my_dict[key]
except KeyError:
  value = None
```

---

### 4. Custom Duck Types: Implementing the Expected Interface

```python
class FileLike:
  def read(self):
    return 'data from FileLike object'

def read_data(source):
  try:
    return source.read()
  except AttributeError:
    raise ValueError('Source is not file-like')

print(read_data(FileLike()))  # data from FileLike object
```

---

### 5. EAFP with Multiple Operations

```python
def safe_divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return float('inf')
  except TypeError:
    return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # inf
print(safe_divide(10, 'x')) # None
```

---

### 6. Best Practice: Catch Only What You Expect

```python
try:
  result = some_operation()
except (ValueError, KeyError) as e:
  print(f'Handled error: {e}')
```

---

---

## 9. Summary and Key Takeaways

- EAFP (Easier to Ask Forgiveness than Permission) is the preferred Pythonic style for error handling and interface use, especially with duck typing.
- LBYL (Look Before You Leap) can be useful in performance-critical or multi-condition checks, but is less idiomatic and can introduce race conditions.
- Duck typing focuses on what an object can do, not what it is—write code that expects an interface, not a type.
- Catch only the exceptions you expect and can handle; avoid broad `except Exception` blocks.
- Document expected interfaces and error handling strategies for maintainable code.
