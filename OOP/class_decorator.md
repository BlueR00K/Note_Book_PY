# Class Decorators in Python

## Syllabus

1. Introduction: What are class decorators in Python?
2. Understanding class decorators:
    - Definition, motivation, and real-world analogy
    - How class decorators differ from function decorators
3. Syntax and mechanics:
    - Basic usage and decorator syntax
    - How Python applies class decorators
4. Implementing class decorators:
    - Simple class decorator functions
    - Using classes as decorators
    - Decorators with arguments (decorator factories)
    - Stacking and composing multiple class decorators
5. Use cases and advanced patterns:
    - Automatic class registration (plugin systems)
    - Method wrapping (logging, timing, validation)
    - Singleton and factory patterns
    - Enforcing interface/attribute presence
    - Adding or modifying class attributes and methods
6. Best practices and design guidelines:
    - Preserving class metadata
    - Avoiding side effects and anti-patterns
    - Documenting decorator behavior
    - Testing decorated classes
7. Common pitfalls and anti-patterns:
    - Returning non-class objects
    - Breaking inheritance or MRO
    - Unintended side effects
8. Advanced and practical examples:
    - Real-world code samples
    - Edge cases and debugging tips
9. Further reading and resources
10. Summary and key takeaways

## 1. Introduction

Class decorators are a powerful feature in Python that allow you to modify or enhance classes in a reusable and declarative way. They are similar to function decorators but operate at the class level, enabling behaviors such as automatic method wrapping, registration, validation, and more. Understanding class decorators is essential for advanced Python development, especially in frameworks and libraries.

---

## 2. What is a Class Decorator?

- A class decorator is a callable (usually a function or class) that takes a class object as input and returns either the same class or a modified/replacement class.
- Syntax: Place `@decorator_name` above the class definition.

```python
@my_decorator
class MyClass:
    ...
```

---

## 3. Syntax and Basic Usage

- A class decorator is defined as a function that accepts a class and returns a class.

```python
def simple_decorator(cls):
    # Modify or wrap the class
    return cls

@simple_decorator
class Example:
    pass
```

---

## 4. Difference Between Function and Class Decorators

- Function decorators take a function and return a function; class decorators take a class and return a class.
- Both use the `@decorator` syntax, but their targets and use cases differ.

---

## 5. Use Cases and Motivation

- Automatic registration of classes (e.g., plugin systems)
- Adding or modifying methods or attributes
- Enforcing coding standards or validation
- Wrapping methods for logging, timing, or access control
- Implementing singleton or factory patterns

---

## 6. Implementing a Simple Class Decorator

```python
def add_repr(cls):
    def __repr__(self):
        return f"<{cls.__name__} {self.__dict__}>"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p)  # <Point {'x': 1, 'y': 2}>
```

---

## 7. Decorators with Arguments

- To accept arguments, use a decorator factory (a function returning a decorator).

```python
def add_method(name, value):
    def decorator(cls):
        setattr(cls, name, value)
        return cls
    return decorator

@add_method('greet', lambda self: 'Hello!')
class Person:
    pass

print(Person().greet())  # Hello!
```

---

## 8. Stacking Multiple Class Decorators

- Multiple decorators can be stacked; they are applied from the innermost (bottom) to the outermost (top).

```python
@decorator1
@decorator2
class MyClass:
    ...
```

---

## 9. Best Practices and Common Pitfalls

- Always return a class from your decorator.
- Be careful not to break inheritance or method resolution order.
- Document the decorator's effect and usage.
- Avoid side effects at import time.
- Test decorated classes thoroughly.

---

## 10. Real-World Examples and Advanced Usage

---

## 11. Advanced & Practical Examples: Class Decorators

### 1. Automatic Class Registration (Plugin Pattern)

```python
registry = {}
def register(cls):
    registry[cls.__name__] = cls
    return cls

@register
class PluginA:
    pass

@register
class PluginB:
    pass

print(registry)  # {'PluginA': <class ...>, 'PluginB': <class ...>}
```

---

### 2. Singleton Pattern via Class Decorator

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print('Connecting...')

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

---

### 3. Method Wrapping: Logging All Method Calls

```python
def log_methods(cls):
    import functools
    for attr, value in cls.__dict__.items():
        if callable(value) and not attr.startswith('__'):
            @functools.wraps(value)
            def wrapper(self, *args, __method=value, **kwargs):
                print(f"Calling {cls.__name__}.{__method.__name__}")
                return __method(self, *args, **kwargs)
            setattr(cls, attr, wrapper)
    return cls

@log_methods
class Greeter:
    def hello(self):
        print('Hello!')

g = Greeter()
g.hello()  # Logs method call
```

---

### 4. Enforcing Attribute Presence (Interface Enforcement)

```python
def require_attrs(*attrs):
    def decorator(cls):
        for attr in attrs:
            if not hasattr(cls, attr):
                raise TypeError(f"Missing required attribute: {attr}")
        return cls
    return decorator

@require_attrs('x', 'y')
class Point:
    x = 0
    y = 0

# @require_attrs('foo')
# class Bad:
#     pass  # Raises TypeError
```

---

### 5. Using a Class as a Decorator (Decorator Class)

```python
class AddClassVar:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __call__(self, cls):
        setattr(cls, self.name, self.value)
        return cls

@AddClassVar('category', 'math')
class Calculator:
    pass

print(Calculator.category)  # math
```

---

### 6. Stacking and Composing Class Decorators

```python
def uppercase_class_name(cls):
    cls.__name__ = cls.__name__.upper()
    return cls

@register
@uppercase_class_name
class pluginC:
    pass

print(registry)  # Includes 'PLUGINC'
```

---

### 7. Anti-Pattern: Returning Non-Class from Decorator

```python
def bad_decorator(cls):
    return 42  # BAD: Should return a class

# @bad_decorator
# class Foo: pass  # Will break code expecting a class
```

---

### 8. Best Practice: Preserve Class Metadata

Use `functools.wraps` or manually copy `__name__`, `__doc__`, etc., when wrapping classes.

---

### 9. Further Reading

- [Python docs: Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318: Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- [Class Decorators vs. Metaclasses](https://realpython.com/primer-on-python-decorators/#decorating-classes)
