# First-Class Functions in Python

In Python, functions are first-class citizens. This means that functions can be treated like any other object. They can be passed as arguments to other functions, returned as values from other functions, and assigned to variables.

## Example
```python
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
greeting = greet
print(greeting("Alice"))  # Output: Hello, Alice!
```

## Use Cases

### 1. Passing Functions as Arguments

Functions can be passed as arguments to other functions.

```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)  # Output: 25
```

### 2. Returning Functions from Functions

Functions can return other functions.

```python
def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function

inner = outer_function()
print(inner())  # Output: Hello from the inner function!
```

### 3. Using Functions in Data Structures

Functions can be stored in data structures like lists and dictionaries.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = {
    'add': add,
    'subtract': subtract
}

print(operations['add'](10, 5))  # Output: 15
print(operations['subtract'](10, 5))  # Output: 5
```

## Practical Example

Let's create a practical example where we use first-class functions to create a simple calculator that can perform different operations based on user input.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculator(operation, x, y):
    return operation(x, y)

# Dictionary of operations
operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Example usage
x, y = 10, 5
print(calculator(operations['add'], x, y))      # Output: 15
print(calculator(operations['subtract'], x, y)) # Output: 5
print(calculator(operations['multiply'], x, y)) # Output: 50
print(calculator(operations['divide'], x, y))   # Output: 2.0
```

This example demonstrates how first-class functions can be used to create a flexible and extensible calculator.