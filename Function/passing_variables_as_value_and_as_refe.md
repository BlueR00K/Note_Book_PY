# Passing Variables as Value and as Reference in Python

In Python, understanding how variables are passed to functions is crucial for writing bug-free and efficient code. Unlike some languages, Python uses a mechanism called **"pass-by-object-reference"** (also known as "pass-by-assignment").

## What Does Pass-by-Object-Reference Mean?

- When you pass a variable to a function, you are passing a reference to the object, not the actual object itself.
- The function receives a reference to the same object, but the reference itself is passed by value.

## Mutable vs. Immutable Types

- **Immutable types**: `int`, `float`, `str`, `tuple`, `frozenset`, etc.
  - If you modify the value inside a function, it creates a new object.
- **Mutable types**: `list`, `dict`, `set`, `bytearray`, etc.
  - If you modify the object inside a function, the changes affect the original object.

## Examples

### Immutable Example

```python
def modify_number(x):
    x += 10
    print("Inside function:", x)

num = 5
modify_number(num)
print("Outside function:", num)
# Output:
# Inside function: 15
# Outside function: 5
```

*The original `num` is unchanged because integers are immutable.*

### Mutable Example

```python
def append_item(lst):
    lst.append(4)
    print("Inside function:", lst)

numbers = [1, 2, 3]
append_item(numbers)
print("Outside function:", numbers)
# Output:
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]
```

*The original list is changed because lists are mutable.*

## Rebinding vs. Mutating

- **Rebinding**: Assigning a new object to a parameter inside a function does not affect the original variable.
- **Mutating**: Changing the contents of a mutable object affects the original object.

### Example: Rebinding

```python
def rebind_list(lst):
    lst = [0, 0, 0]
    print("Inside function:", lst)

numbers = [1, 2, 3]
rebind_list(numbers)
print("Outside function:", numbers)
# Output:
# Inside function: [0, 0, 0]
# Outside function: [1, 2, 3]
```

## Practical Tip

- For immutable types, changes inside a function do not affect the original variable.
- For mutable types, changes inside a function can affect the original object.
- If you want to avoid modifying the original object, pass a copy (e.g., `list.copy()`).

## Summary Table

| Type       | Example         | Can be changed in function? | Notes                        |
|------------|----------------|----------------------------|------------------------------|
| Immutable  | int, str, tuple| No                         | New object is created        |
| Mutable    | list, dict, set| Yes                        | Original object is modified  |

## Advanced: Custom Objects

Custom classes behave like mutable objects unless you override their behavior.

```python
class Counter:
    def __init__(self, value):
        self.value = value

def increment(counter):
    counter.value += 1

c = Counter(5)
increment(c)
print(c.value)  # Output: 6
```

## Conclusion

Python's argument passing model is neither "pass-by-value" nor "pass-by-reference" in the traditional sense. Instead, it passes references to objects, and whether changes affect the original depends on the mutability of the object.

---

**Key Point:**  

- Immutable objects: safe from modification inside functions  
- Mutable objects: can be changed inside functions  
