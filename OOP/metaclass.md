# Metaclasses in Python

## 1. Introduction and Syllabus

Metaclasses are an advanced and powerful feature in Python that allow you to control the creation and behavior of classes themselves. They are often described as "classes of classes" and are essential for building frameworks, enforcing coding standards, and implementing advanced patterns such as singletons, registries, and automatic attribute validation.

### Syllabus

- What is a metaclass? (definition, motivation, and real-world analogy)
- How Python creates classes: type, class, and metaclass
- The `type` metaclass and custom metaclasses
- Syntax for specifying a metaclass
- The metaclass `__new__` and `__init__` methods
- Use cases for metaclasses
- Best practices and when to use (or avoid) metaclasses
- Common pitfalls and anti-patterns
- Real-world examples and advanced usage

---

## 2. What is a Metaclass?

- A metaclass is a class whose instances are themselves classes.
- Just as classes define how objects behave, metaclasses define how classes behave.
- By default, all classes in Python are created using the built-in `type` metaclass.

**Real-world analogy:** Think of a metaclass as a factory blueprint for factories (classes), which in turn produce products (objects).

---

## 3. How Python Creates Classes: type, class, and metaclass

- When you define a class, Python uses a metaclass to create it.
- The default metaclass is `type`, but you can specify your own.
- Classes are themselves objects, and metaclasses control their creation and behavior.

---

## 4. The `type` Metaclass and Custom Metaclasses

- `type` is both the default metaclass and a function for creating new types.
- You can create a class dynamically using `type(name, bases, dict)`.
- Custom metaclasses are created by subclassing `type`.

---

## 5. Syntax for Specifying a Metaclass

- Use the `metaclass` keyword argument in the class definition:

```python
class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass
```

---

## 6. The Metaclass `__new__` and `__init__` Methods

- `__new__(mcs, name, bases, namespace)` is called to create the class object.
- `__init__(cls, name, bases, namespace)` initializes the class object after creation.
- You can modify the class, add attributes, enforce rules, or register classes here.

---

## 7. Use Cases for Metaclasses

- Enforcing coding standards (e.g., all methods must be documented)
- Automatic attribute validation or transformation
- Singleton, registry, or plugin patterns
- Automatic class registration for frameworks
- Debugging, logging, or profiling class creation

---

## 8. Best Practices and When to Use (or Avoid) Metaclasses

- Use metaclasses only when simpler solutions (decorators, class inheritance) are insufficient.
- Document the purpose and behavior of your metaclasses clearly.
- Avoid metaclasses for everyday OOP—prefer them for framework or library development.

---

## 9. Common Pitfalls and Anti-Patterns

- Overcomplicating code with unnecessary metaclasses
- Making metaclasses too complex or hard to debug
- Not documenting metaclass side effects
- Breaking compatibility with multiple inheritance or third-party libraries

---

## 10. Real-World Examples and Advanced Usage

### 1. Enforcing Class Attributes with a Metaclass

```python
class RequireDocMeta(type):
    def __new__(mcs, name, bases, namespace):
        for attr, value in namespace.items():
            if callable(value) and not value.__doc__:
                raise TypeError(f"Method {attr} must have a docstring")
        return super().__new__(mcs, name, bases, namespace)

class Good(metaclass=RequireDocMeta):
    def foo(self):
        """This is documented."""
        pass
# class Bad(metaclass=RequireDocMeta):
#     def bar(self):
#         pass  # Raises TypeError: Method bar must have a docstring
```

---

### 2. Automatic Class Registration (Plugin Pattern)

```python
class RegistryMeta(type):
    registry = {}
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if name != 'Base':
            mcs.registry[name] = cls
        return cls

class Base(metaclass=RegistryMeta):
    pass
class PluginA(Base):
    pass
class PluginB(Base):
    pass

print(RegistryMeta.registry)  # {'PluginA': <class ...>, 'PluginB': <class ...>}
```

---

### 3. Singleton Pattern with a Metaclass

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

---

### 4. Debugging and Logging Class Creation

```python
class LoggingMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating class {name}")
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=LoggingMeta):
    pass
# Output: Creating class MyClass
```

---

### 5. Best Practice: Minimal, Well-Documented Metaclasses

```python
class MinimalMeta(type):
    """A minimal metaclass for demonstration purposes."""
    pass

class Example(metaclass=MinimalMeta):
    """This class uses a minimal metaclass."""
    pass
```

---

*These advanced examples show how to use metaclasses for enforcing standards, registration, singletons, logging, and more. Use metaclasses judiciously and document their behavior for maintainable, professional code.*
