# Creating Iterators and Iterables Using Classes in Python

## 1. Introduction and Syllabus

Iterators and iterables are fundamental to Python's data model and enable the use of `for` loops, comprehensions, and many built-in functions. By implementing special methods in your own classes, you can create custom objects that support iteration, lazy evaluation, and streaming data. Mastering iterators and iterables is essential for writing efficient, Pythonic, and reusable code.

### Syllabus

- What are iterators and iterables? (definition, motivation, and real-world analogy)
- The iterator protocol: `__iter__` and `__next__`
- Creating custom iterators with classes
- Creating custom iterables with classes
- Differences between iterators and iterables
- Using iterators in `for` loops and comprehensions
- Lazy evaluation and infinite sequences
- Best practices for iterator design
- Common pitfalls and anti-patterns
- Real-world examples and advanced usage

---

## 2. What are Iterators and Iterables?

- **Iterable:** An object capable of returning its members one at a time. Implements `__iter__()`.
- **Iterator:** An object representing a stream of data; returns itself from `__iter__()` and implements `__next__()`.
- Iterators raise `StopIteration` when exhausted.

**Real-world analogy:** Think of an iterable as a playlist (can be played multiple times), and an iterator as the playhead (remembers where you are in the playlist).

---

## 3. The Iterator Protocol: `__iter__` and `__next__`

- To make an object iterable, implement `__iter__()` to return an iterator.
- To make an object an iterator, implement both `__iter__()` (returns self) and `__next__()` (returns next value or raises `StopIteration`).

---

## 4. Creating Custom Iterators with Classes

```python
class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(3):
    print(num)  # 3 2 1
```

---

## 5. Creating Custom Iterables with Classes

```python
class Squares:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return SquaresIterator(self.n)

class SquaresIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i ** 2
        self.i += 1
        return result

for sq in Squares(5):
    print(sq)  # 0 1 4 9 16
```

---

## 6. Differences Between Iterators and Iterables

- An **iterable** can create new iterators (multiple passes).
- An **iterator** is its own stateful object (single pass).
- Built-in containers (list, dict, set, etc.) are iterables, not iterators.

---

## 7. Using Iterators in For Loops and Comprehensions

- `for` loops call `iter(obj)` to get an iterator, then repeatedly call `next()`.
- Comprehensions and many built-ins (e.g., `sum`, `max`) use the iterator protocol.

---

## 8. Lazy Evaluation and Infinite Sequences

- Iterators can represent infinite or very large sequences without loading all data into memory.

```python
class Naturals:
    def __init__(self):
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.n += 1
        return self.n

# Usage: for n in Naturals(): ... (be careful: infinite loop!)
```

---

## 9. Best Practices for Iterator Design

- Keep iterator state internal and private.
- Raise `StopIteration` to signal the end.
- Avoid side effects in `__next__()`.
- Document iterator behavior and limitations.

---

## 10. Common Pitfalls and Anti-Patterns

- Forgetting to raise `StopIteration`.
- Returning a new iterator from `__iter__()` in an iterator class (should return self).
- Mixing iterator and iterable responsibilities in one class (prefer separation for clarity).

---

## 11. Real-World Examples and Advanced Usage

---

## 12. Advanced & Practical Examples: Iterators and Iterables

### 1. Reverse Iteration with Custom Iterator

```python
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Usage:
for ch in Reverse('Python'):
    print(ch, end=' ')  # n o h t y P
```

---

### 2. Filtering Iterator (Like `filter`)

```python
class EvenFilter:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            if value % 2 == 0:
                return value
        raise StopIteration

# Usage:
for even in EvenFilter([1,2,3,4,5,6]):
    print(even, end=' ')  # 2 4 6
```

---

### 3. Lookahead Iterator (Peekable)

```python
class Peekable:
    def __init__(self, iterable):
        self._it = iter(iterable)
        self._cache = None
        self._has_cache = False
    def __iter__(self):
        return self
    def __next__(self):
        if self._has_cache:
            self._has_cache = False
            return self._cache
        return next(self._it)
    def peek(self):
        if not self._has_cache:
            self._cache = next(self._it)
            self._has_cache = True
        return self._cache

# Usage:
p = Peekable([10, 20, 30])
print(p.peek())  # 10
print(next(p))   # 10
print(next(p))   # 20
```

---

### 4. Chaining Iterators (Composition)

```python
class Chain:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.current = iter(self.iterables[0])
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.iterables):
            try:
                return next(self.current)
            except StopIteration:
                self.index += 1
                if self.index < len(self.iterables):
                    self.current = iter(self.iterables[self.index])
        raise StopIteration

# Usage:
for x in Chain([1,2], (3,4), '56'):
    print(x, end=' ')  # 1 2 3 4 5 6
```

---

### 5. Iterator as a Context Manager

```python
class FileLineIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        self.file = open(self.filename)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
    def __iter__(self):
        return self
    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line.rstrip('\n')

# Usage:
# with FileLineIterator('somefile.txt') as lines:
#     for line in lines:
#         print(line)
```

---

### 6. Integrating Iterators with Generators

```python
class IterableWrapper:
    def __init__(self, gen_func, *args, **kwargs):
        self.gen_func = gen_func
        self.args = args
        self.kwargs = kwargs
    def __iter__(self):
        return self.gen_func(*self.args, **self.kwargs)

def countdown_gen(n):
    while n > 0:
        yield n
        n -= 1

# Usage:
for x in IterableWrapper(countdown_gen, 3):
    print(x)  # 3 2 1
```

---

### 7. Real-World Use Case: Batching Large Data

```python
class BatchIterator:
    def __init__(self, iterable, batch_size):
        self._it = iter(iterable)
        self.batch_size = batch_size
    def __iter__(self):
        return self
    def __next__(self):
        batch = []
        try:
            for _ in range(self.batch_size):
                batch.append(next(self._it))
        except StopIteration:
            pass
        if not batch:
            raise StopIteration
        return batch

# Usage:
for batch in BatchIterator(range(10), 3):
    print(batch)  # [0,1,2] [3,4,5] [6,7,8] [9]
```

---

### 8. Anti-Pattern: Returning New Iterator from `__iter__` in an Iterator

```python
class BadIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        # BAD: returns a new iterator each time
        return BadIterator(self.data)
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Usage:
# Only the first for-loop will work as expected; subsequent loops will restart.
```

---

### 9. Best Practice: Separate Iterable and Iterator

```python
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return MyRangeIterator(self.start, self.end)

class MyRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Usage:
for i in MyRange(3, 7):
    print(i, end=' ')  # 3 4 5 6
```

---

### 10. Further Reading

- [PEP 234: Iterators](https://peps.python.org/pep-0234/)
- [Python docs: Iterator Types](https://docs.python.org/3/library/stdtypes.html#typeiter)
- [itertools module](https://docs.python.org/3/library/itertools.html)
