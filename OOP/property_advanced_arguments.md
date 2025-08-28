# Advanced Usage: Other Arguments of `property` and the `property` Decorator in Python

## 1. Introduction and Syllabus

The `property` built-in in Python is more than just a decorator for simple getter/setter patterns. It is a powerful descriptor that can be used directly, supports advanced argument patterns, and enables fine-grained control over attribute access, documentation, and introspection. Mastering the full capabilities of `property` is essential for professional Python development, especially in large or framework-based projects.

### Syllabus

- What is the `property` object? (definition, motivation, and descriptor protocol)
- The full signature of `property()`
- Using `property()` as a function vs. as a decorator
- Arguments: `fget`, `fset`, `fdel`, `doc`
- Dynamic and programmatic property creation
- Customizing property docstrings and metadata
- Read-only, write-only, and computed properties with custom docs
- Advanced patterns: property chaining, property factories, and class decorators
- Introspection and property attributes (`fget`, `fset`, `fdel`, `__doc__`)
- Best practices and professional use cases
- Common pitfalls and anti-patterns
- Real-world advanced examples

---

## 2. What is the `property` Object?

- `property` is a built-in class that implements the descriptor protocol.
- It allows you to manage attribute access by defining getter, setter, and deleter methods, and optionally a docstring.
- Can be used as a decorator or instantiated directly.

---

## 3. Full Signature of `property()`

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

- `fget`: function to get the attribute value
- `fset`: function to set the attribute value
- `fdel`: function to delete the attribute
- `doc`: docstring for the property (shown in help and introspection)

---

## 4. Using `property()` as a Function (Not Just a Decorator)

You can create properties programmatically, not just with decorators:

```python
class Person:
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def del_name(self):
        del self._name
    name = property(get_name, set_name, del_name, "The person's name.")
```

---

## 5. Customizing Property Docstrings and Metadata

- The `doc` argument sets the property’s docstring, visible in `help()` and IDEs.
- You can access property methods and docstring via `obj.__class__.prop.fget`, `fset`, `fdel`, and `__doc__`.

```python
print(Person.name.__doc__)  # The person's name.
print(Person.name.fget)     # <function Person.get_name ...>
```

---

## 6. Dynamic and Programmatic Property Creation

- Properties can be created in loops or dynamically, useful for frameworks and metaprogramming.

```python
def make_property(attr):
    def getter(self):
        return getattr(self, '_' + attr)
    def setter(self, value):
        setattr(self, '_' + attr, value)
    return property(getter, setter, doc=f"Dynamic property for {attr}")

class Data:
    x = make_property('x')
    y = make_property('y')
    def __init__(self, x, y):
        self._x = x
        self._y = y
```

---

## 7. Advanced Patterns: Property Factories and Chaining

- You can build property factories for reusable patterns (e.g., type checking, validation, computed properties).
- Chaining properties or composing them with descriptors enables advanced behaviors.

---

## 8. Introspection and Property Attributes

- Access the underlying getter, setter, deleter, and docstring:

```python
p = Data.x
print(p.fget)   # <function ...>
print(p.fset)   # <function ...>
print(p.__doc__)  # Dynamic property for x
```

---

## 9. Best Practices and Professional Use Cases

- Use the `doc` argument for clear documentation, especially in libraries and APIs.
- Prefer the decorator syntax for simple cases, but use the functional form for dynamic or advanced patterns.
- Avoid overcomplicating property logic—keep it maintainable.
- Use introspection to build tools, documentation, or validation frameworks.

---

## 10. Common Pitfalls and Anti-Patterns

- Forgetting to set the `doc` argument (leads to missing documentation)
- Overusing dynamic property creation (can reduce code clarity)
- Not handling edge cases in custom getter/setter logic
- Using properties for trivial or unnecessary encapsulation

---

## 11. Real-World Advanced Examples

### 1. Dynamic Property Creation in a Loop

```python
def make_property(attr):
    def getter(self):
        return getattr(self, '_' + attr)
    def setter(self, value):
        setattr(self, '_' + attr, value)
    return property(getter, setter, doc=f"Dynamic property for {attr}")

class Point:
    pass

for attr in ('x', 'y', 'z'):
    setattr(Point, attr, make_property(attr))

p = Point()
p.x = 10
p.y = 20
p.z = 30
print(p.x, p.y, p.z)  # 10 20 30
print(Point.x.__doc__)  # Dynamic property for x
```

---

### 2. Custom Validation and Type Checking with Property Factories

```python
def typed_property(name, expected_type):
    private_name = '_' + name
    def getter(self):
        return getattr(self, private_name)
    def setter(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"{name} must be of type {expected_type.__name__}")
        setattr(self, private_name, value)
    return property(getter, setter, doc=f"{name} ({expected_type.__name__})")

class Person:
    age = typed_property('age', int)
    name = typed_property('name', str)
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Alice', 30)
# p.age = 'thirty'  # Raises TypeError
```

---

### 3. Read-Only Computed Property with Custom Docstring

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    def get_area(self):
        return 3.14159 * self._radius ** 2
    area = property(get_area, doc="Area of the circle (read-only)")

c = Circle(5)
print(c.area)  # 78.53975
print(Circle.area.__doc__)
```

---

### 4. Introspection: Accessing Property Methods and Docstrings

```python
class Demo:
    def get_value(self): return 42
    def set_value(self, v): pass
    value = property(get_value, set_value, doc="A demo property.")

print(Demo.value.fget)   # <function Demo.get_value ...>
print(Demo.value.fset)   # <function Demo.set_value ...>
print(Demo.value.__doc__)  # A demo property.
```

---

### 5. Advanced: Property with Custom Deleter and Logging

```python
class Resource:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        print(f"Setting name to {value}")
        self._name = value
    def del_name(self):
        print(f"Deleting name {self._name}")
        del self._name
    name = property(get_name, set_name, del_name, "Resource name with logging.")

r = Resource('db')
r.name = 'cache'  # Setting name to cache
del r.name        # Deleting name cache
```

---

*These advanced examples show how to leverage all arguments of the property decorator for dynamic, validated, and introspectable attribute management. Mastering these patterns is essential for professional Python development and framework design.*
