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