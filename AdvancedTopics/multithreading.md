# Multithreading in Python

## Syllabus

1. Introduction: What is multithreading?
2. Why use multithreading?
3. The threading module: basics and API
4. Thread lifecycle and management
5. Synchronization primitives (Lock, RLock, Semaphore, Event, Condition)
6. Common pitfalls and best practices
7. Real-world use cases
8. Demo: Python multithreading program
9. Debugging and profiling multithreaded code
10. Summary and key takeaways

---

## 1. Introduction: What is Multithreading?

Multithreading is a technique that allows a program to run multiple threads (smaller units of a process) concurrently. In Python, threads share the same memory space, making communication between them easy but also introducing the risk of race conditions. Multithreading is especially useful for I/O-bound tasks, such as network operations or file I/O, but is limited for CPU-bound tasks due to the Global Interpreter Lock (GIL).

In this topic, you will learn:

- The fundamentals of multithreading in Python
- How to create and manage threads
- How to synchronize threads and avoid common pitfalls
- How to use multithreading for real-world problems
- How to debug and profile multithreaded code

Let's begin by understanding why and when to use multithreading.

---

## 2. Why Use Multithreading?

### Benefits

- Improves responsiveness in I/O-bound applications
- Allows background tasks to run without blocking the main thread
- Useful for GUI applications, network servers, and file operations

### Limitations

- Not effective for CPU-bound tasks due to the GIL
- Risk of race conditions and deadlocks

---

## 3. The threading Module: Basics and API

Python's `threading` module provides a high-level interface for working with threads.

### Creating Threads

```python
import threading

def print_numbers():
 for i in range(5):
  print(f"Number: {i}")

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

### Thread Subclassing

```python
import threading

class MyThread(threading.Thread):
 def run(self):
  print("Thread running!")

t = MyThread()
t.start()
t.join()
```

### Thread API Overview

- `start()`: Begin thread execution
- `join()`: Wait for thread to finish
- `is_alive()`: Check if thread is running
- `name`: Thread name

---

## 4. Thread Lifecycle and Management

### Thread States

- New: Thread is created but not started
- Runnable: Thread is ready to run
- Running: Thread is executing
- Blocked/Waiting: Thread is waiting for a resource
- Dead: Thread has finished execution

### Diagram: Thread Lifecycle

```text
New --> Runnable --> Running --> Blocked/Waiting --> Running --> Dead
```

### Managing Threads

- Use `join()` to wait for threads
- Use `is_alive()` to check status
- Use thread-safe data structures for communication

---

## 5. Synchronization Primitives

### Lock

```python
import threading

lock = threading.Lock()
shared_resource = 0

def increment():
 global shared_resource
 for _ in range(1000):
  with lock:
   shared_resource += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
 t.start()
for t in threads:
 t.join()
print(shared_resource)
```

### RLock (Reentrant Lock)

```python
import threading

rlock = threading.RLock()

def recursive_function(n):
 with rlock:
  if n > 0:
   recursive_function(n-1)

recursive_function(5)
```

### Semaphore

```python
import threading
import time

semaphore = threading.Semaphore(2)

def worker(num):
 with semaphore:
  print(f"Worker {num} is running")
  time.sleep(1)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads:
 t.start()
for t in threads:
 t.join()
```

### Event

```python
import threading
import time

event = threading.Event()

def waiter():
 print("Waiting for event...")
 event.wait()
 print("Event received!")

thread = threading.Thread(target=waiter)
thread.start()
time.sleep(2)
event.set()
thread.join()
```

### Condition

```python
import threading

condition = threading.Condition()
items = []

def producer():
 with condition:
  items.append(1)
  print("Item produced")
  condition.notify()

def consumer():
 with condition:
  while not items:
   condition.wait()
  print("Item consumed")

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
```

---

## 6. Common Pitfalls and Best Practices

### Pitfalls

- Race conditions
- Deadlocks
- Starvation
- Not joining threads
- Using non-thread-safe data structures

### Best Practices

- Always use locks for shared data
- Keep critical sections small
- Avoid holding locks while performing I/O
- Use thread-safe queues for communication
- Profile and test multithreaded code

---

## 7. Real-world Use Cases

- Web servers handling multiple requests
- Downloading files in parallel
- Background data processing
- Real-time data acquisition
- GUI applications (keeping UI responsive)

---

## 8. Demo: Python Multithreading Program

Below is a demo program that launches multiple threads to download web pages concurrently and measure the total time taken.

```python
import threading
import requests
import time

urls = [
 "https://www.example.com",
 "https://www.python.org",
 "https://www.github.com",
 "https://www.stackoverflow.com",
 "https://www.wikipedia.org"
]

def download(url):
 print(f"Starting download: {url}")
 resp = requests.get(url)
 print(f"Finished download: {url} ({len(resp.content)} bytes)")

start = time.time()
threads = [threading.Thread(target=download, args=(url,)) for url in urls]
for t in threads:
 t.start()
for t in threads:
 t.join()
end = time.time()
print(f"Total time: {end - start:.2f} seconds")
```

---

## 9. Debugging and Profiling Multithreaded Code

### Debugging Tips

- Use logging to trace thread activity
- Use thread names for clarity
- Use `threading.enumerate()` to list active threads
- Use tools like `faulthandler` and `pdb`

### Profiling

- Use `cProfile` for performance analysis
- Use thread-safe counters and timers

---

## 10. Summary and Key Takeaways

- Multithreading enables concurrent execution of tasks in Python
- Best for I/O-bound workloads
- Use synchronization primitives to avoid race conditions
- Always join threads and use thread-safe data structures
- Debug and profile to ensure correctness and performance

---
