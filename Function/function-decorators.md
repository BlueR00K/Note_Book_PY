# Python Function Decorators: The Magic Behind the Scenes

## What is a Decorator?

A **decorator** is a design pattern in Python that allows you to add new functionality to an existing object (usually a function) without modifying its structure. Decorators are a powerful tool for code reuse, readability, and separation of concerns.

Think of decorators as “wrappers” that you put around your functions to make them do more—like adding a turbocharger to a car without changing the engine!

---

## Why Use Decorators?

- **Code Reusability:** Write logic once, apply it everywhere.
- **Separation of Concerns:** Keep your core logic clean.
- **DRY Principle:** Don’t Repeat Yourself.

---

## How Do Decorators Work?

Decorators use Python’s ability to treat functions as first-class objects. You can pass functions as arguments, return them, and assign them to variables.

### Basic Decorator Structure

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

---

## Practical, Mind-Blowing Examples

### 1. Timing Function Execution

Ever wondered how long your function takes to run? Decorators can measure that!

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds.")
        return result
    return wrapper

@timer
def compute():
    total = sum(i*i for i in range(10_000))
    print("Computation done!")

compute()
```

---

### 2. Debugging Made Easy

Want to see what arguments your function received? Decorators can log them!

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")
```

---

### 3. Access Control: Password-Protected Functions

Imagine a function that only runs if you know the secret password!

```python
def require_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = input("Enter password: ")
            if attempt == password:
                return func(*args, **kwargs)
            else:
                print("Access denied!")
        return wrapper
    return decorator

@require_password("open-sesame")
def launch_missiles():
    print("Missiles launched! 🚀")

launch_missiles()
```

---

## Decorators with Arguments

Decorators themselves can accept arguments! This is called a **decorator factory**.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def cheer():
    print("Python is awesome!")

cheer()
```

---

## Preserving Function Metadata

Decorators can hide the original function’s name and docstring. Use `functools.wraps` to fix this!

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def hello():
    """Say hello"""
    print("Hello!")

print(hello.__name__)  # Output: hello
print(hello.__doc__)   # Output: Say hello
```

---

## Chaining Multiple Decorators

You can stack decorators to combine their powers!

```python
@timer
@debug
def process_data(data):
    time.sleep(0.5)
    print(f"Processed {data}")

process_data("my_data")
```

---

## Real-World Use Cases

- **Authentication:** Restrict access to certain functions.
- **Logging:** Track function calls and errors.
- **Caching:** Store results of expensive computations.
- **Validation:** Check arguments before running the function.

---

## Curiosity Sparkers

- **Can you write a decorator that retries a function if it fails?**
- **How would you create a decorator that memoizes function results?**
- **Can you build a decorator that limits how often a function can be called?**

---

## Summary Table

| Feature            | Example Use Case         | Syntax Example         |
|--------------------|-------------------------|-----------------------|
| Basic Decorator    | Logging                 | `@log`                |
| With Arguments     | Repeating, Access Ctrl  | `@repeat(3)`          |
| Chaining           | Timing + Debugging      | `@timer @debug`       |
| Metadata Preserved | Documentation           | `@functools.wraps`    |

---

## Final Thought

Decorators are like magic spells for your functions. They let you add superpowers without touching the original code. Once you master them, you’ll see Python in a whole new light!

---

**Try creating your own decorator now! What amazing functionality will you add to your functions?**
