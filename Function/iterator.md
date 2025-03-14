# Iterators in Python

Iterators are objects that allow you to traverse through all the elements of a collection, regardless of its specific implementation. They are an essential part of Python's iteration protocol.

## Iterable

An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop. Examples include lists, tuples, strings, and dictionaries.

### Example
```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
# Output:
# 1
# 2
# 3
```

## Iterator

An iterator is an object representing a stream of data; it returns the data one element at a time. Iterators implement two methods: `__iter__()` and `__next__()`.

### Example
```python
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # This will raise a StopIteration exception
```

## Creating an Iterator

You can create your own iterator by defining a class with `__iter__()` and `__next__()` methods.

### Example
```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator([1, 2, 3])
for item in my_iter:
    print(item)
# Output:
# 1
# 2
# 3
```

## Iteration

Iteration is the process of looping through the elements of an iterable. Python's `for` loop is a convenient way to iterate over iterables.

### Example
```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
# Output:
# 1
# 2
# 3
```

## The `iter()` Function

The `iter()` function returns an iterator object. It can be used to convert an iterable into an iterator.

### Example
```python
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
```

## The `next()` Function

The `next()` function retrieves the next item from an iterator. If the iterator is exhausted, it raises a `StopIteration` exception.

### Example
```python
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # This will raise a StopIteration exception
```

## Practical Example

Let's create a practical example where we define an iterator for a custom range of numbers.

### Example
```python
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration

custom_range = CustomRange(1, 5)
for number in custom_range:
    print(number)
# Output:
# 1
# 2
# 3
# 4
```

This example demonstrates how to create a custom iterator that generates a range of numbers.