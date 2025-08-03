# DocStrings in Python

DocStrings (Documentation Strings) are special strings used to document modules, classes, methods, and functions in Python. They help explain what a piece of code does, its parameters, return values, and usage examples. DocStrings are accessible at runtime via the `__doc__` attribute and are a key part of writing readable, maintainable code.

## Basic Usage

A DocString is written as a string literal (usually triple quotes) as the first statement in a module, class, method, or function.

```python
def greet(name):
    """Return a friendly greeting for the given name.
    
    Args:
        name (str): The name to greet.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

print(greet.__doc__)
```

## DocStrings in Classes

```python
class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def add(self, x, y):
        """Add two numbers and return the result."""
        return x + y

    def multiply(self, x, y):
        """Multiply two numbers and return the result."""
        return x * y

print(Calculator.__doc__)
print(Calculator.add.__doc__)
```

## DocStrings in Modules

At the top of a Python file, you can add a DocString to describe the module's purpose.

```python
"""
math_utils.py

This module provides utility functions for mathematical operations.
"""

def square(x):
    """Return the square of a number."""
    return x * x
```

## Multi-line and Formatted DocStrings

DocStrings can be single-line or multi-line. For complex functions, multi-line DocStrings are preferred.

```python
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    
    Example:
        >>> fibonacci(5)
        5
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## DocStrings in Data Structures

You can even add DocStrings to classes used as data structures.

```python
class Person:
    """
    Represents a person with a name and age.
    
    Attributes:
        name (str): The person's name.
        age (int): The person's age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Unique Example: DocStrings for Lambda Functions

Lambda functions do not support DocStrings directly, but you can assign a DocString to a variable holding a lambda.

```python
add = lambda x, y: x + y
add.__doc__ = "Add two numbers together."
print(add.__doc__)
```

## Best Practices

- Always use triple quotes for DocStrings.
- Clearly describe the purpose, parameters, and return values.
- Include examples for complex functions.
- Use DocStrings for all public modules, classes, and functions.

## Practical Benefits

- DocStrings are used by IDEs and documentation tools (like Sphinx).
- They make code easier to understand and maintain.
- They help other developers (and your future self) use your code correctly.

---
DocStrings are a simple but powerful way to make your Python code self-documenting and professional.
