# Recursive Generators and Decorators in Python

## What Are Recursive Generators?

Recursive generators are generator functions that call themselves to yield values from nested or hierarchical data structures. They are powerful for traversing trees, graphs, or any recursive pattern.

---

## Example: Traversing a Nested List with a Recursive Generator

```python
def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
for x in flatten(nested):
    print(x)
# Output: 1 2 3 4 5 6
```

---

## Example: Recursive Generator for Tree Traversal

```python
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def walk_tree(node):
    yield node.value
    for child in node.children:
        yield from walk_tree(child)

root = Node(1, [Node(2), Node(3, [Node(4), Node(5)])])
for v in walk_tree(root):
    print(v)
# Output: 1 2 3 4 5
```

---

## What Are Recursive Decorators?

Recursive decorators are decorators that apply themselves recursively to functions or methods, often used for logging, timing, or modifying behavior in recursive calls.

---

## Example: Logging Recursive Calls with a Decorator

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args})")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4))
# Output: Logs each call to factorial
```

---

## Example: Memoization Decorator for Recursive Generators

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fib_gen(n):
    if n < 2:
        yield n
    else:
        for x in fib_gen(n-1):
            yield x
        for x in fib_gen(n-2):
            yield x

print(list(fib_gen(3)))
# Output: [1, 0, 1, 0]
```

---

## Curiosity Sparkers

- Can you use recursive generators to traverse a file system?
- How would you combine recursive generators and decorators for debugging?
- Can you build a recursive generator that yields paths in a graph?
- What happens if you decorate a generator with a decorator that modifies its output?

---

## Final Thoughts

Recursive generators and decorators unlock elegant solutions for complex, nested, and recursive problems. Mastering them will help you write more expressive, maintainable, and powerful Python code.
