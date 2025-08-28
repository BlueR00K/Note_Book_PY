# Class Documentation, Docstrings, and mypy in Python OOP

## 1. Introduction

Proper documentation and type checking are essential for writing maintainable, readable, and robust Python code. This section covers class documentation, docstrings, and the use of `mypy` for static type checking in Python OOP.

---

## 2. Class Documentation

- **Class documentation** provides information about the purpose and usage of a class.
- It is typically included as a docstring immediately after the class definition.
- Good documentation helps other developers (and your future self) understand how to use the class.

### Example

```python
class Animal:
    """Represents a generic animal.
    
    Attributes:
        species (str): The species of the animal.
    """
    def __init__(self, species: str):
        self.species = species
```

---

## 3. Docstrings

- **Docstrings** are string literals that appear as the first statement in a module, function, class, or method.
- They are used by documentation tools and IDEs to provide context-sensitive help.
- Docstrings can be single-line or multi-line (triple-quoted).
- Use the [PEP 257](https://peps.python.org/pep-0257/) conventions for writing docstrings.

### Example

```python
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b
```

### Multi-line Docstring Example

```python
class Person:
    """Represents a person.
    
    Args:
        name (str): The person's name.
        age (int): The person's age.
    """
    def __init__(self, name: str, age: int):
        """Initialize a Person object."""
        self.name = name
        self.age = age
```

---

## 4. Docstrings for Methods and Properties

- Each method should have its own docstring describing its purpose, parameters, and return value.
- Properties can also have docstrings.

### Example

```python
class Rectangle:
    """A rectangle shape."""
    def __init__(self, width: float, height: float):
        """Initialize width and height."""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    @property
    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return self.width == self.height
```

---

## 5. Using mypy for Static Type Checking

- **mypy** is a static type checker for Python.
- It checks your code for type errors based on type hints (PEP 484).
- Helps catch bugs before runtime and improves code quality.

### Installation

```sh
pip install mypy
```

### Basic Usage

```sh
mypy your_script.py
```

### Example with Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### Running mypy

```sh
mypy example.py
```

---

## 6. Best Practices

- Always write clear and concise docstrings for classes, methods, and functions.
- Use type hints to improve code clarity and enable static checking.
- Run `mypy` regularly to catch type-related bugs early.
- Follow PEP 257 for docstring conventions and PEP 484 for type hints.

---

*Next: Advanced and practical examples of class documentation, docstrings, and mypy will be added in the following step.*

---

## Advanced and Practical Examples: Class Documentation, Docstrings, and mypy

### Example 1: Comprehensive Class and Method Docstrings

```python
class BankAccount:
    """A simple bank account class.

    Attributes:
        owner (str): The name of the account owner.
        balance (float): The current account balance.
    """
    def __init__(self, owner: str, balance: float = 0.0):
        """Initialize a new BankAccount.

        Args:
            owner (str): The account owner's name.
            balance (float, optional): Initial balance. Defaults to 0.0.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal succeeded, False otherwise.
        """
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
```

### Example 2: Module-Level Docstrings and mypy Usage

```python
"""banking.py: Example module for bank account operations.

This module demonstrates module-level docstrings and type checking with mypy.
"""

from typing import List

class Transaction:
    """Represents a bank transaction."""
    def __init__(self, amount: float, description: str):
        self.amount = amount
        self.description = description

def summarize(transactions: List[Transaction]) -> float:
    """Calculate the total amount from a list of transactions."""
    return sum(t.amount for t in transactions)
```

#### Running mypy on the above code

```sh
mypy banking.py
```

### Example 3: Docstrings for Properties and Static Methods

```python
class Celsius:
    """Temperature in Celsius."""
    def __init__(self, temperature: float):
        self._temperature = temperature

    @property
    def temperature(self) -> float:
        """Get or set the temperature in Celsius."""
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._temperature = value

    @staticmethod
    def to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return celsius * 9 / 5 + 32
```

### Example 4: mypy Detecting Type Errors

```python
def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

result = add_numbers(2, "three")  # mypy will flag this as an error
```

#### mypy Output

```
error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"
```
