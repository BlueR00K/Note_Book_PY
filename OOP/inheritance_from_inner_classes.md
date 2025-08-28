# Inheritance from Inner Classes in Python

## 1. Introduction

Inner classes (nested classes) are classes defined within another class. While not common in everyday Python code, they can be useful for encapsulating logic that is tightly coupled to the outer class. Inheriting from inner classes is an advanced topic and can be used to extend or customize the behavior of nested structures.

---

## 2. What is an Inner (Nested) Class?

- An inner class is defined inside the body of another class.
- It is usually used for helper classes or to logically group related functionality.

```python
class Outer:
    class Inner:
        pass
```

---

## 3. Accessing and Instantiating Inner Classes

- Access an inner class using the outer class: `Outer.Inner`.
- Instantiate: `obj = Outer.Inner()`

```python
class Outer:
    class Inner:
        def greet(self):
            print("Hello from Inner")

obj = Outer.Inner()
obj.greet()  # Hello from Inner
```

---

## 4. Inheriting from Inner Classes

- You can inherit from an inner class by referencing it as a base class: `class Sub(Outer.Inner): ...`
- The inner class must be accessible in the current scope.

```python
class Outer:
    class Inner:
        def show(self):
            print("Base Inner")

class Sub(Outer.Inner):
    def show(self):
        print("Derived from Inner")
        super().show()

s = Sub()
s.show()
# Derived from Inner
# Base Inner
```

---

## 5. Use Cases and Considerations

- Use inner classes for tightly coupled logic or as implementation details.
- Inheriting from inner classes is rare and can make code harder to read.
- Inner classes do not have special access to the outer class’s instance or attributes.
- Prefer composition or module-level classes for most use cases.

---

## 6. Best Practices

- Only use inner classes when they are truly an implementation detail.
- Document the relationship and intended usage clearly.
- Avoid deep nesting and complex inheritance from inner classes.
- Consider alternatives (composition, module-level classes) for maintainability.

---

*Next: Advanced and practical examples of inheritance from inner classes will be added in the following step.*

---

## Advanced and Practical Examples: Inheritance from Inner Classes

### 1. Extending Functionality of an Inner Class

```python
class Container:
    class Item:
        def __init__(self, value):
            self.value = value
        def describe(self):
            print(f"Item with value: {self.value}")

class SpecialItem(Container.Item):
    def describe(self):
        print("SpecialItem:")
        super().describe()

s = SpecialItem(42)
s.describe()
# SpecialItem:
# Item with value: 42
```

### 2. Inheriting from an Inner Class Defined in Another Module

Suppose `shapes.py` contains:

```python
# shapes.py
class Drawing:
    class Circle:
        def area(self, r):
            from math import pi
            return pi * r * r
```

In another file:

```python
from shapes import Drawing
class ColoredCircle(Drawing.Circle):
    def color(self):
        return "red"

c = ColoredCircle()
print(c.area(3))  # 28.274...
print(c.color())  # red
```

### 3. Edge Case: Inner Class Access to Outer Class

```python
class Outer:
    class Inner:
        def show(self):
            print("Inner does NOT have access to Outer instance")

o = Outer()
i = o.Inner()
i.show()
```

### 4. Using Inner Classes for Namespacing and Logical Grouping

```python
class UI:
    class Button:
        def click(self):
            print("Button clicked")
    class TextBox:
        def enter_text(self, text):
            print(f"Text entered: {text}")

b = UI.Button()
b.click()
t = UI.TextBox()
t.enter_text("Hello")
```

### 5. Inheriting from Deeply Nested Inner Classes

```python
class A:
    class B:
        class C:
            def hello(self):
                print("Hello from C")

class D(A.B.C):
    def hello(self):
        print("Hello from D (derived from C)")
        super().hello()

d = D()
d.hello()
# Hello from D (derived from C)
# Hello from C
```

### 6. Limitation: Pickling and Serialization

```python
import pickle
class Outer:
    class Inner:
        def __init__(self, x):
            self.x = x

i = Outer.Inner(5)
# pickle.dumps(i)  # Raises PicklingError: Can't pickle <class ...>: it's not the same object as ...
```

### 7. Best Practice: Prefer Module-Level Classes for Reuse

```python
# Instead of using inner classes for inheritance, define at module level:
class Base:
    pass
class Derived(Base):
    pass
```

---
