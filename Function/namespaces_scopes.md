# Namespaces and Scopes in Python

Namespaces and scopes are fundamental concepts in Python that determine how names (identifiers) are mapped to objects and how long they are accessible. Understanding them is crucial for writing clear, bug-free code.

## What is a Namespace?

A namespace is a mapping from names to objects. Think of it as a dictionary where the keys are variable names and the values are the objects those names refer to.

- **Built-in Namespace:** Contains names like `print`, `len`, etc. Available everywhere.
- **Global Namespace:** Contains names defined at the top-level of a module or script.
- **Local Namespace:** Contains names defined inside a function.
- **Enclosing Namespace:** Contains names in enclosing functions (for nested functions).

## Example: Different Namespaces

```python
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)  # Refers to local namespace of inner
    inner()
    print(x)      # Refers to local namespace of outer

x = 'global x'
outer()
print(x)          # Refers to global namespace
```

## What is a Scope?

Scope refers to the region of code where a namespace is directly accessible. Python uses the LEGB rule to resolve names:

- **L**ocal
- **E**nclosing
- **G**lobal
- **B**uilt-in

## LEGB Rule Example

```python
def outer():
    msg = 'enclosing'
    def inner():
        msg = 'local'
        print(msg)  # Local scope
    inner()
    print(msg)      # Enclosing scope

msg = 'global'
outer()
print(msg)          # Global scope
```

## Built-in Namespace Example

```python
print(len([1, 2, 3]))  # 'print' and 'len' are in the built-in namespace
```

## Global vs. Local Variables

Variables assigned inside a function are local by default. To modify a global variable inside a function, use the `global` keyword.

```python
x = 10

def change_global():
    global x
    x = 20

change_global()
print(x)  # Output: 20
```

## Nonlocal Keyword

The `nonlocal` keyword allows you to modify variables in the enclosing (but not global) scope.

```python
def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x = 'inner'
    inner()
    print(x)  # Output: 'inner'

outer()
```

## Practical Example: Nested Functions and Scopes

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

inc = counter()
print(inc())  # Output: 1
print(inc())  # Output: 2
```

## Unique Example: Dynamic Namespace Creation

You can create custom namespaces using dictionaries or the `types.SimpleNamespace` class.

```python
from types import SimpleNamespace

person = SimpleNamespace(name='Alice', age=30)
print(person.name)  # Output: Alice
```

## Scope Pitfalls

- **UnboundLocalError:** Occurs when you try to use a variable before it is assigned in the local scope.
- **Shadowing:** Local variables can shadow global or built-in names, leading to bugs.

```python
x = 5

def foo():
    print(x)  # Error if x is assigned later in foo
    x = 10
foo()
```

## Best Practices

- Avoid using the same name for variables in different scopes unless necessary.
- Use `global` and `nonlocal` only when you need to modify variables outside the current scope.
- Prefer function arguments and return values for passing data.

## Summary Table: Namespace Types

| Namespace   | Example Location         | Lifetime                |
|-------------|-------------------------|-------------------------|
| Built-in    | `print`, `len`          | Entire program          |
| Global      | Module-level variables  | Until module is unloaded|
| Enclosing   | Outer function in nest  | Until outer function ends|
| Local       | Inside a function       | Until function returns  |

---
Namespaces and scopes are the backbone of Python's name resolution. Mastering them helps you write robust, maintainable, and bug-free code.
