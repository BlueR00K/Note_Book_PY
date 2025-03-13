# Lambda Functions in Python

A lambda function is a small anonymous function defined using the `lambda` keyword. Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.

## Syntax
```python
lambda arguments: expression
```

## Example
```python
# A simple lambda function that adds 10 to the input
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
```

## Use Cases

### 1. Sorting and Filtering Data

Lambda functions are often used with functions like `sorted()`, `filter()`, and `map()`.

```python
# Sorting a list of tuples based on the second element
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# Filtering a list to get even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

### 2. Using with `map()` Function

The `map()` function applies a given function to all items in an input list.

```python
# Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

### 3. Using with `reduce()` Function

The `reduce()` function from the `functools` module applies a rolling computation to sequential pairs of values in a list.

```python
from functools import reduce

# Summing all numbers in a list
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15
```

## Practical Example

Let's create a practical example where we use lambda functions to process a list of dictionaries representing employees and filter out those who earn more than a certain amount.

```python
employees = [
    {'name': 'John', 'salary': 50000},
    {'name': 'Jane', 'salary': 60000},
    {'name': 'Doe', 'salary': 45000},
    {'name': 'Smith', 'salary': 70000}
]

# Filter employees with salary greater than 55000
high_earners = list(filter(lambda emp: emp['salary'] > 55000, employees))
print(high_earners)
# Output: [{'name': 'Jane', 'salary': 60000}, {'name': 'Smith', 'salary': 70000}]
```

This example demonstrates how lambda functions can be used to filter data based on specific criteria.