
# Property, Setter, and Getter in Python Classes

### Syllabus

1. Introduction to Properties
2. What is a Property? (Definition, Motivation, Real-World Analogy)
3. Why Use Properties Instead of Public Attributes?
4. The `property` Decorator: Syntax and Usage
5. Defining Getter, Setter, and Deleter Methods
6. Read-Only and Write-Only Properties
7. Validation and Computed Properties
8. Best Practices for Encapsulation
9. Common Pitfalls and Anti-Patterns
10. Advanced/Practical Examples
11. Summary

---

## 1. Introduction to Properties

Python provides a powerful and Pythonic way to manage attribute access and encapsulation using the `property` decorator, along with setter and getter methods. This approach allows you to control how attributes are accessed, validated, or computed, while maintaining a clean and intuitive interface for users of your classes.

---

## 2. What is a Property? (Definition, Motivation, Real-World Analogy)

A property is a special kind of attribute in Python that allows you to define methods for getting, setting, or deleting a value, while still using attribute access syntax (`obj.attr`).

**Real-world analogy:** Think of a property as a smart thermostat: you can set or get the temperature, but the device can validate, log, or adjust the value behind the scenes.

---

## 3. Why Use Properties Instead of Public Attributes?

- Encapsulate internal state and provide a public interface
- Add validation, logging, or computation to attribute access
- Avoid breaking code that uses attribute access when changing implementation
- Enable read-only or write-only attributes

---

## 4. The `property` Decorator: Syntax and Usage

- Use the `@property` decorator to define a getter method
- Use `@<property>.setter` to define a setter
- Use `@<property>.deleter` to define a deleter (optional)

```python
class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
```

---

## 5. Defining Getter, Setter, and Deleter Methods

- **Getter:** Returns the value of the attribute
- **Setter:** Sets or validates the value
- **Deleter:** Deletes the attribute (rarely used)

---

## 6. Read-Only and Write-Only Properties

- Omit the setter to make a property read-only
- Omit the getter to make a property write-only (rare)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @property
    def area(self):
        return 3.14159 * self._radius ** 2  # Read-only computed property
```

---

## 7. Validation and Computed Properties

- Use setters to validate or transform values
- Use properties to compute values on the fly

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
```

---

## 8. Best Practices for Encapsulation

- Use a single underscore (`_attr`) for internal attributes
- Document the purpose and expected usage of properties
- Avoid unnecessary logic in getters/setters
- Use properties to maintain backward compatibility

---

## 9. Common Pitfalls and Anti-Patterns

- Using properties for trivial access (no added value)
- Adding heavy computation to getters (can surprise users)
- Not documenting side effects or validation
- Overusing properties for all attributes

---

## 10. Advanced/Practical Examples

### 10.1. Read-Only, Write-Only, and Computed Properties

```python
class Account:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        """Read-only property."""
        return self._balance
    @property
    def deposit(self):
        """Write-only property."""
        raise AttributeError("Deposit is write-only")
    @deposit.setter
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

acc = Account(100)
acc.deposit = 50
print(acc.balance)  # 150
```

---

### 10.2. Properties for Validation and Logging

```python
class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print(f"Setting price to {value}")
        self._price = value

p = Product(10)
p.price = 20  # Setting price to 20
```

---

### 10.3. Properties for Backward Compatibility

```python
class OldClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, val):
        self._value = val

# Later, change implementation but keep interface:
class NewClass(OldClass):
    @property
    def value(self):
        return self._value * 2
    @value.setter
    def value(self, val):
        self._value = val // 2

n = NewClass(10)
print(n.value)  # 20
n.value = 40
print(n.value)  # 40
```

---

### 10.4. Using Deleter for Resource Management

```python
class FileHolder:
    def __init__(self, filename):
        self._filename = filename
        self._file = open(filename, 'w')
    @property
    def file(self):
        return self._file
    @file.deleter
    def file(self):
        print(f"Closing file {self._filename}")
        self._file.close()
        del self._file

f = FileHolder('test.txt')
del f.file  # Closing file test.txt
```

---

### 10.5. Best Practice: Documenting Properties

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def area(self):
        """Area of the rectangle (read-only property)."""
        return self._width * self._height
```

---

---

## 11. Summary

Mastering properties, setters, and getters in Python enables you to create robust, maintainable, and Pythonic classes. Using these tools effectively is key to encapsulation, validation, and clean APIs in professional Python development.
