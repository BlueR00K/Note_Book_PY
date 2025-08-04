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

---

### Can you use recursive generators to traverse a file system?

Yes! Recursive generators are perfect for walking through directories and files:

```python
import os


    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            yield from walk_files(full_path)
        else:
            yield full_path

# for file in walk_files("./some_folder"):
#     print(file)
```

---

### How would you combine recursive generators and decorators for debugging?

You can use a decorator to log each recursive call and its arguments:

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

@debug
def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
print(list(flatten(nested)))
```

---

### Can you build a recursive generator that yields paths in a graph?

Absolutely! You can recursively yield all paths from a start node to an end node:

```python
def find_paths(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path
    for node in graph.get(start, []):
        if node not in path:
            yield from find_paths(graph, node, end, path + [node])

---
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}
for p in find_paths(graph, 'A', 'D'):
    print(p)
# Output: All paths from 'A' to 'D'
```

---

### What happens if you decorate a generator with a decorator that modifies its output?

If a decorator wraps a generator and changes its output, you can transform or filter the yielded values:

```python
def double_yields(gen_func):
    def wrapper(*args, **kwargs):
        for value in gen_func(*args, **kwargs):
            yield value * 2
    return wrapper

@double_yields
def numbers():
    for i in range(5):
        yield i

print(list(numbers()))  # [0, 2, 4, 6, 8]
```

---

## More Details: When to Use Recursive Generators and Decorators

- Use recursive generators for any problem involving nested, hierarchical, or tree-like data.
- Decorators can add logging, memoization, timing, or transformation to recursive functions and generators.
- Combining both lets you build powerful, maintainable solutions for complex data traversal and manipulation.

## Final Thoughts

Recursive generators and decorators unlock elegant solutions for complex, nested, and recursive problems. Mastering them will help you write more expressive, maintainable, and powerful Python code.
