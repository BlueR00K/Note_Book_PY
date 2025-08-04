# Memoization in Python (for Recursive Functions and Generators)

## What Is Memoization?

Memoization is an optimization technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again. It's especially powerful for recursive algorithms, dramatically improving performance by avoiding redundant calculations.

Think of memoization as a magical notebook that remembers every answer you've already solved!

---

## Why Use Memoization?

- **Speed:** Avoids repeated work in recursive calls
- **Efficiency:** Reduces time complexity from exponential to linear in many cases
- **Simplicity:** Easy to implement with decorators or function attributes

---

## Classic Example: Fibonacci Without Memoization

```python
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Slow!
```

---

## Memoized Fibonacci with a Decorator

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Fast!
```

---

## Memoization for Recursive Generators

You can also memoize generators to cache yielded results:

```python
def memoize_gen(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            yield from cache[args]
        else:
            result = list(func(*args))
            cache[args] = result
            yield from result
    return wrapper

@memoize_gen
def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(tuple(item))  # Use tuple for hashable args
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
print(list(flatten(tuple(nested))))
```

---

## Built-in Tools: functools.lru_cache

Python's `functools.lru_cache` makes memoization easy and robust:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))
```

---

## Curiosity Sparkers

---

### Can you memoize mutually recursive functions?

Yes! You can use a shared cache (dictionary) outside the functions, or a decorator that works for both:

```python
cache = {}


    if n in cache:
        return cache[n]
    if n == 0:
        result = True
    else:
        result = is_odd(n-1)
    cache[n] = result
    return result

---
    if n in cache:
        return not cache[n]
    if n == 0:
        result = False
    else:
        result = is_even(n-1)
    cache[n] = not result
    return result

print(is_even(10))  # True
print(is_odd(10))   # False
```

---

### How would you memoize a recursive function with multiple arguments?

Just use all arguments as the cache key (tuples work well):

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

print(ackermann(3, 4))
```

---

### Can you use memoization for recursive generators that yield large data?

Yes, but be careful with memory usage! You can cache only partial results or use an LRU cache:

```python
from functools import lru_cache

@lru_cache(maxsize=10)
def big_gen(n):
    if n == 0:
        yield 0
    else:
        for x in big_gen(n-1):
            yield x + n

print(list(big_gen(5)))
```

---

### What happens if you memoize a function with unhashable arguments?

You’ll get a `TypeError` because unhashable types (like lists or dicts) can’t be used as dictionary keys. You can convert them to tuples or use a custom key function:

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        key = tuple(map(lambda x: tuple(x) if isinstance(x, list) else x, args))
        if key in cache:
            return cache[key]
        result = func(*args)
        cache[key] = result
        return result
    return wrapper

@memoize
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3]))  # 6
```

## Final Thoughts

Memoization is a game-changer for recursive algorithms. It transforms slow, impractical code into fast, elegant solutions. Mastering memoization will make your Python code more efficient and enjoyable to write!
