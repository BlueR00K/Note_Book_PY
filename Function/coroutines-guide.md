# Coroutines in Python: Generators & Functions

## What Are Coroutines?

Coroutines are special functions that can pause and resume their execution, allowing for cooperative multitasking. In Python, coroutines are most commonly implemented using generators, but can also be created with `async def` for asynchronous programming.

Think of coroutines as actors on a stage: they perform, pause, and wait for their next cue!

---

## Coroutine vs. Generator: What's the Difference?

- **Generators** produce a sequence of values using `yield`.
- **Coroutines** can consume values sent to them, using `yield` or `await`.
- All coroutines are generators, but not all generators are coroutines.

---

## Coroutine Basics with Generators

A coroutine is a generator that uses `yield` as an expression, allowing data to be sent in:

```python
def echo():
    while True:
        value = yield
        print(f"Echo: {value}")

g = echo()
next(g)         # Prime the coroutine

g.send("Hello") # Echo: Hello
g.send("World") # Echo: World
```

---

## Example: Coroutine for Running Average

Coroutines can maintain state and process incoming data on the fly:

```python
def running_average():
    total = 0
    count = 0
    avg = None
    while True:
        value = yield avg
        if value is None:
            break
        total += value
        count += 1
        avg = total / count

avg_coro = running_average()
print(next(avg_coro))    # None
print(avg_coro.send(10)) # 10.0
print(avg_coro.send(20)) # 15.0
print(avg_coro.send(30)) # 20.0
avg_coro.close()
```

---

## Coroutine Termination

Coroutines can be closed with `.close()` or by sending a sentinel value (like `None`). You can also inject exceptions with `.throw()`.

---

## Coroutine Pipelines

Coroutines can be chained to build powerful data processing pipelines:

```python
def producer():
    for i in range(5):
        yield i

def doubler():
    while True:
        value = yield
        print(value * 2)

d = doubler()
next(d)
for num in producer():
    d.send(num)
```

---

## Asynchronous Coroutines with `async def`

Python's `async def` and `await` keywords allow for true asynchronous coroutines:

```python
import asyncio

async def async_echo():
    while True:
        value = await asyncio.sleep(1, result="Hello async!")
        print(value)

# asyncio.run(async_echo())
```

---

## Curiosity Sparkers

---

### Can you build a coroutine that filters and transforms data in real time?

Yes! Coroutines can process, filter, and transform data as it arrives:

```python
def filter_and_square():
    while True:
        value = yield
        if value % 2 == 0:
            print(f"Even squared: {value ** 2}")

f = filter_and_square()
next(f)
for i in range(1, 6):
    f.send(i)
```

---

### How would you use coroutines to implement a state machine?

Coroutines can elegantly model state machines by maintaining and switching states:

```python
def traffic_light():
    state = 'RED'
    while True:
        command = yield state
        if command == 'next':
            state = {'RED': 'GREEN', 'GREEN': 'YELLOW', 'YELLOW': 'RED'}[state]

t = traffic_light()
print(next(t))         # RED
print(t.send('next'))  # GREEN
print(t.send('next'))  # YELLOW
print(t.send('next'))  # RED
```

---

### What happens if you send an exception into a coroutine?

You can inject exceptions with `.throw()`. The coroutine can catch and handle them, or propagate and terminate:

```python
def demo():
    try:
        yield "Start"
        yield "Middle"
    except ValueError:
        yield "Caught ValueError!"
    yield "End"

g = demo()
print(next(g))         # Start
print(next(g))         # Middle
print(g.throw(ValueError))  # Caught ValueError!
print(next(g))         # End
```

---

### Can you combine generator-based and async coroutines in a pipeline?

Yes! You can mix generator-based and async coroutines for powerful, flexible pipelines:

```python
import asyncio

def sync_gen():
    for i in range(3):
        yield i

async def async_consumer():
    for value in sync_gen():
        await asyncio.sleep(0.5)
        print(f"Async received: {value}")

# asyncio.run(async_consumer())

---

## Final Thoughts

Coroutines unlock a new level of expressiveness and efficiency in Python. Whether you're building data pipelines, event-driven systems, or asynchronous applications, mastering coroutines will make your code more powerful and elegant.
