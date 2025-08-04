# Marker Parameters in Python

Marker parameters are special parameters in Python functions that allow you to specify the kind of arguments that a function can accept. These include positional-only parameters, keyword-only parameters, and variable-length arguments.

## Positional-Only Parameters

Positional-only parameters can only be specified by their position in the function call. They are defined using a `/` in the function signature.

### Example

```python
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Alice", greeting="Hi"))  # Output: Hi, Alice!
# print(greet(name="Alice"))  # This will raise a TypeError
```

## Keyword-Only Parameters

Keyword-only parameters can only be specified by their name in the function call. They are defined using a `*` in the function signature.

### Example

```python
def greet(*, name, greeting="Hello"):
    return f"{greeting}, {name}!"

# print(greet("Alice"))  # This will raise a TypeError
print(greet(name="Alice"))  # Output: Hello, Alice!
print(greet(name="Alice", greeting="Hi"))  # Output: Hi, Alice!
```

## Variable-Length Arguments

Variable-length arguments allow you to pass a variable number of arguments to a function. These include `*args` for positional arguments and `**kwargs` for keyword arguments.

### Example

```python
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)
# Output:
# 1
# 2
# 3

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30)
# Output:
# name: Alice
# age: 30
```

## Combining Different Parameter Types

You can combine different types of parameters in a single function. The order should be: positional-only parameters, positional or keyword parameters, keyword-only parameters, and variable-length arguments.

### Example

```python
def combined_example(pos1, pos2, /, pos_or_kw, *, kw_only, **kwargs):
    print(f"pos1: {pos1}, pos2: {pos2}, pos_or_kw: {pos_or_kw}, kw_only: {kw_only}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

combined_example(1, 2, pos_or_kw=3, kw_only=4, extra=5)
# Output:
# pos1: 1, pos2: 2, pos_or_kw: 3, kw_only: 4
# extra: 5
```

This example demonstrates how to use different types of parameters in a single function.
