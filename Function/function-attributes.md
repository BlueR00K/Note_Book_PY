# Function Attributes in Python

## What Are Function Attributes?

Function attributes are custom properties you can attach to any Python function object. They allow you to store metadata, configuration, or state directly on the function itself—making your code more flexible and expressive.

Think of function attributes as sticky notes you can attach to your functions!

---

## Setting and Accessing Function Attributes

You can set attributes on any function after it's defined:

```python
def greet(name):
    return f"Hello, {name}!"

greet.language = "English"
greet.greeting_type = "formal"

print(greet.language)        # English
print(greet.greeting_type)   # formal
```

---

## Use Cases for Function Attributes

- **Metadata:** Store information about the function (author, version, etc.)
- **Configuration:** Attach settings or flags
- **State:** Track usage, cache results, or store counters
- **Decorators:** Communicate between decorators and functions

---

## Example: Tracking Calls with an Attribute

```python
def counter():
    counter.calls += 1
    print(f"Called {counter.calls} times!")

counter.calls = 0

counter()
counter()
counter()
# Output: Called 1 times! ... Called 3 times!
```

---

## Example: Function Attributes in Decorators

Function attributes are often used in decorators to store extra information:

```python
def tag(func):
    func.is_tagged = True
    return func

@tag
def my_function():
    pass

print(my_function.is_tagged)  # True
```

---

## Built-in Function Attributes

Every function in Python has built-in attributes:

- `__name__`: Function name
- `__doc__`: Docstring
- `__defaults__`: Default argument values
- `__code__`: Compiled code object
- `__dict__`: Custom attributes

```python
def sample(x=42):
    """A sample function."""
    return x

print(sample.__name__)     # sample
print(sample.__doc__)      # A sample function.
print(sample.__defaults__) # (42,)
print(sample.__dict__)     # {}
```

## More Built-in Function Attributes

Python functions have several other useful built-in attributes:

- `__annotations__`: Type hints for arguments and return value
- `__module__`: The module name where the function is defined
- `__closure__`: Tuple of cell objects for closed-over variables
- `__kwdefaults__`: Default values for keyword-only arguments
- `__qualname__`: Qualified name (useful for nested functions)

---

### Practical Examples of Built-in Attributes

```python
from typing import Any

def example(a: int, b: str = "hi") -> Any:
    """An example function."""
    return a, b

print(example.__name__)        # example
print(example.__doc__)         # An example function.
print(example.__defaults__)    # ("hi",)
print(example.__annotations__) # {'a': int, 'b': str, 'return': Any}
print(example.__module__)      # __main__
print(example.__kwdefaults__)  # None (if no keyword-only defaults)
print(example.__qualname__)    # example
print(example.__dict__)        # {}
```

---

### Example: Closure Attribute

```python
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f.__closure__)  # (<cell at ...: 10>,)
print(f.__closure__[0].cell_contents)  # 10
```

## Curiosity Sparkers

---

### Can you use function attributes to implement memoization?

Yes! You can use a function attribute to cache results and avoid recomputation:

```python
def fib(n):
    if n in fib.cache:
        return fib.cache[n]
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    fib.cache[n] = result
    return result

fib.cache = {}
print(fib(10))  # 55
print(fib.cache)  # Shows cached results
```

---

### How would you use function attributes to build a plugin system?

Function attributes can register plugins or handlers dynamically:

```python
def process(data):
    for plugin in process.plugins:
        data = plugin(data)
    return data

def double(x):
    return x * 2


    return x ** 2

process.plugins = [double, square]
print(process(3))  # (3 * 2) ** 2 = 36
```

---

### What happens if you set an attribute on a built-in function?

Most built-in functions (like `len`, `print`) do not support custom attributes and will raise an `AttributeError`:

```python
try:
    len.description = "Returns the length of an object"
except AttributeError as e:
    print(e)  # 'builtin_function_or_method' object has no attribute 'description'
```

---

### Can you use function attributes to communicate between multiple decorators?

Yes! Decorators can set and read function attributes to share information:

```python
def flag(func):
    func.is_flagged = True
    return func

---
    if getattr(func, 'is_flagged', False):
        print("Function is flagged!")
    func.info = "Extra info"
    return func

@info
@flag
def my_func():
    pass

print(my_func.is_flagged)  # True
print(my_func.info)        # Extra info
```

## Final Thoughts

Function attributes are a hidden superpower in Python. They let you attach data, state, and meaning to your functions, opening up creative ways to design flexible and maintainable code.
