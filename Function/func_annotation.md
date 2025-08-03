# Function Annotations in Python

Function annotations provide a way of associating various parts of a function with arbitrary Python expressions at compile time. They are often used for type hints, which help with code readability and can be used by tools for static type checking.

## Common Types from typing Library

Here are the most commonly used types from the `typing` library:

- `Any`
- `Callable`
- `Dict`
- `List`
- `Tuple`
- `Set`
- `FrozenSet`
- `Type`
- `TypeVar`
- `Union`
- `Optional`
- `Literal`
- `Generic`
- `Sequence`
- `Mapping`
- `Iterable`
- `Iterator`
- `NoReturn`
- `Protocol`
- `ClassVar`
- `Final`
- `Self` (Python 3.11+)
- `Concatenate` (for advanced typing)

Reference: [Python typing documentation](https://docs.python.org/3/library/typing.html)

## Callable Type

The `Callable` type hint indicates that a value is a function or any callable object with a specified signature.

### Callable Types in Python

- **Functions** (def, lambda)
- **Methods** (bound and unbound)
- **Classes** (with `__call__` method)
- **Objects** (instances of classes with `__call__`)

### Example: Callable Type

```python
from typing import Callable

def add(x: int, y: int) -> int:
    return x + y

def execute(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(execute(add, 2, 3))  # Output: 5
```

### Example: Callable Class

```python
class Multiplier:
    def __call__(self, x: int, y: int) -> int:
        return x * y

mult = Multiplier()
print(mult(3, 4))  # Output: 12
```

### Example: Callable with Any Arguments

```python
from typing import Callable

def call_any(func: Callable[..., int], *args, **kwargs) -> int:
    return func(*args, **kwargs)
```

## *args and **kwargs in Function Annotations

- `*args` allows a function to accept any number of positional arguments.
- `**kwargs` allows a function to accept any number of keyword arguments.

### Annotating *args and **kwargs

- Use `*args: Type` and `**kwargs: Type` in function definitions.
- In type hints, use `Tuple[Type, ...]` for `*args` and `Dict[str, Type]` for `**kwargs`.

### Example

```python
from typing import Tuple, Dict, Any

def demo(*args: int, **kwargs: str) -> None:
    print(args, kwargs)

def demo2(*args: Any, **kwargs: Any) -> None:
    print(args, kwargs)
```

### Example with Type Hints

```python
from typing import Tuple, Dict

def func(*args: Tuple[int, ...], **kwargs: Dict[str, int]) -> None:
    print(args, kwargs)
```

## Type Aliases: Fully Detailed Guide

Type aliases allow you to create a new name for an existing type, making code more readable and maintainable, especially for complex types.

### Why Use Type Aliases?

- Simplifies complex type hints
- Improves code readability
- Makes refactoring easier

### How to Create a Type Alias

```python
from typing import List, Dict

Employee = Dict[str, str]
Vector = List[float]
```

### Example Usage

```python
Employees = List[Employee]

def get_names(employees: Employees) -> List[str]:
    return [emp['name'] for emp in employees]
```

### Type Aliases for Complex Types

```python
from typing import Callable, Tuple

Operation = Callable[[int, int], int]
Point = Tuple[float, float]
```

### Type Aliases with Generics

```python
from typing import TypeVar, List

T = TypeVar('T')
Vector = List[T]
```

## Type Variables: Full Description and Guide

Type variables (`TypeVar`) are used to create generic functions, classes, and type aliases. They allow you to write code that works with multiple types while preserving type safety.

### Why Use Type Variables?

- Enable generic programming
- Allow functions/classes to work with any type
- Improve code reusability

### How to Create a Type Variable

```python
from typing import TypeVar

T = TypeVar('T')
```

### Example: Generic Function

```python
from typing import TypeVar, List

T = TypeVar('T')

def get_first(elements: List[T]) -> T:
    return elements[0]
```

### Example: Generic Class

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    def push(self, item: T) -> None:
        self.items.append(item)
    def pop(self) -> T:
        return self.items.pop()

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
```

### Example: Bounded TypeVar

```python
from typing import TypeVar

Number = TypeVar('Number', int, float)

def add(x: Number, y: Number) -> Number:
    return x + y
```

### Example: Covariant and Contravariant TypeVar

```python
from typing import TypeVar

T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)
```

### Practical Benefits

- Type variables make code more flexible and reusable
- Used extensively in libraries like `typing`, `collections`, and `asyncio`

Reference: [TypeVar documentation](https://docs.python.org/3/library/typing.html#typing.TypeVar)

# Function Annotations in Python

Function annotations provide a way of associating various parts of a function with arbitrary Python expressions at compile time. They are often used for type hints, which help with code readability and can be used by tools for static type checking.

## Syntax

Function annotations are defined using a colon (`:`) after the parameter name, followed by the type hint, and an arrow (`->`) before the return type.

### Example

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## Common Type Hints

### Built-in Types

- `int`: Integer type
- `float`: Floating-point number
- `str`: String type
- `bool`: Boolean type
- `list`: List type
- `tuple`: Tuple type
- `dict`: Dictionary type
- `set`: Set type

### Example

```python
def add(a: int, b: int) -> int:
    return a + b

def concatenate(strings: list[str]) -> str:
    return ''.join(strings)
```

### Optional Type

The `Optional` type hint indicates that a value can be of a specified type or `None`.

### Example

```python
from typing import Optional

def get_name(name: Optional[str] = None) -> str:
    if name is None:
        return "Unknown"
    return name
```

### Union Type

The `Union` type hint indicates that a value can be one of several types.

### Example

```python
from typing import Union

def process(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Processing integer: {value}"
    return f"Processing string: {value}"
```

### Any Type

The `Any` type hint indicates that a value can be of any type.

### Example

```python
from typing import Any

def print_value(value: Any) -> None:
    print(value)
```

### Callable Type

The `Callable` type hint indicates that a value is a function with a specified signature.

### Example

```python
from typing import Callable

def execute(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

### List, Tuple, and Dict Types

You can specify the types of elements in lists, tuples, and dictionaries.

### Example

```python
from typing import List, Tuple, Dict

def process_list(items: List[int]) -> int:
    return sum(items)

def process_tuple(data: Tuple[int, str]) -> str:
    return f"Number: {data[0]}, String: {data[1]}"

def process_dict(data: Dict[str, int]) -> int:
    return sum(data.values())
```

### Type Aliases

Type aliases allow you to create a new name for an existing type.

### Example

```python
from typing import List

Vector = List[float]

def scale_vector(vector: Vector, scalar: float) -> Vector:
    return [scalar * num for num in vector]
```

### Type Variables

Type variables allow you to create generic functions and classes.

### Example

```python
from typing import TypeVar, List

T = TypeVar('T')

def get_first_element(elements: List[T]) -> T:
    return elements[0]
```

## Practical Example

Let's create a practical example where we use function annotations to define a function that processes a list of employees and returns their names and salaries.

```python
from typing import List, Dict

def get_employee_info(employees: List[Dict[str, Union[str, int]]]) -> List[str]:
    info = []
    for employee in employees:
        name = employee['name']
        salary = employee['salary']
        info.append(f"Name: {name}, Salary: {salary}")
    return info

employees = [
    {'name': 'John', 'salary': 50000},
    {'name': 'Jane', 'salary': 60000},
    {'name': 'Doe', 'salary': 45000}
]

print(get_employee_info(employees))
# Output:
# ['Name: John, Salary: 50000', 'Name: Jane, Salary: 60000', 'Name: Doe, Salary: 45000']
```

This example demonstrates how to use function annotations to provide type hints for a function that processes a list of dictionaries.
