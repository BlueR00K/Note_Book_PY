# Nested Exception Handling in Python

## 1. Syllabus

- Introduction to nested exception handling
- Syntax and flow of nested try/except blocks
- Use cases and motivations for nesting
- Detailed examples (simple and complex)
- Best practices and common pitfalls
- Real-world scenarios (file, network, database, user input)
- Advanced usage (re-raising, custom exceptions, multi-level nesting)
- Comparison with flat exception handling
- Summary and key takeaways

---

## 2. Introduction

Nested exception handling involves placing one or more try/except blocks inside another try/except block. This technique is essential for writing robust, maintainable, and professional Python code, especially in complex applications where different parts of the code may need to handle errors differently.

### Why Use Nested Exception Handling?

- **Fine-grained control:** Allows you to handle specific exceptions at the most appropriate level of your code.
- **Separation of concerns:** Inner blocks can handle local errors, while outer blocks can manage broader or unexpected issues.
- **Resource management:** Ensures that resources (files, network connections, etc.) are properly cleaned up, even if an error occurs deep in the call stack.
- **Graceful degradation:** Lets your program recover from certain errors and continue running, or escalate only critical failures.

### Common Use Cases

- Handling file I/O errors inside a function, while the caller handles user input errors.
- Managing database transactions, where inner blocks handle query errors and outer blocks handle connection issues.
- Network operations, where you may want to retry on certain errors but abort on others.
- Complex business logic, where different layers of the application have different responsibilities for error handling.

### Example Overview

Consider a program that reads a file, processes its contents, and writes results to another file. You might want to handle file-not-found errors at the outer level, but handle data parsing errors at an inner level:

```python
try:
 with open('input.txt') as infile:
  try:
   data = [int(line) for line in infile]
  except ValueError as e:
   print(f"Data error: {e}")
  else:
   with open('output.txt', 'w') as outfile:
    for number in data:
     outfile.write(f"{number * 2}\n")
except FileNotFoundError:
 print("Input file not found.")
```

This structure allows the program to distinguish between file errors and data errors, handling each appropriately.

---

---

## 3. Syntax and Flow of Nested try/except Blocks

Nested try/except blocks are simply try/except statements placed inside other try/except statements. This can be done at any level of code: within functions, loops, or even inside other except or finally blocks.

### Basic Syntax

```python
try:
     # Outer block
     try:
          # Inner block
          ...
     except SomeException:
          # Handle inner exception
          ...
except AnotherException:
     # Handle outer exception
     ...
```

### Flow Diagram

1. The outer try block is entered.
2. If an exception occurs in the inner try block, Python looks for a matching except in the inner block first.
3. If not handled, the exception propagates to the outer except block.
4. If still not handled, it propagates up the call stack.

---

## 4. Detailed Examples (Simple and Complex)

### 4.1. Simple Nested Example

```python
try:
     try:
          print("Inner try")
          1 / 0
     except ZeroDivisionError:
          print("Inner except: Division by zero")
     else:
          print("Inner else")
     finally:
          print("Inner finally")
except Exception as e:
     print(f"Outer except: {e}")
finally:
     print("Outer finally")
```

### 4.2. Nested Exception Handling in Functions

```python
def parse_and_divide(s, divisor):
     try:
          try:
               num = int(s)
          except ValueError:
               print("Could not parse integer.")
               return None
          return num / divisor
     except ZeroDivisionError:
          print("Cannot divide by zero.")
          return None

result = parse_and_divide("42", 0)
result2 = parse_and_divide("not_a_number", 2)
```

### 4.3. Multi-level Nesting

```python
try:
     try:
          try:
               raise RuntimeError("Deep error!")
          except ValueError:
               print("Level 3 ValueError")
     except RuntimeError as e:
          print(f"Level 2 caught: {e}")
except Exception as e:
     print(f"Level 1 caught: {e}")
```

---

## 5. Best Practices and Common Pitfalls

- Keep nested try/except blocks as simple and shallow as possible.
- Use nested blocks only when you need different handling at different levels.
- Avoid deeply nested exception handling; refactor into functions or use context managers.
- Always document why nesting is needed.
- Clean up resources in finally blocks or with context managers.

**Common Pitfall:** Swallowing exceptions in inner blocks can hide bugs. Always log or re-raise if you can't handle it.

---

## 6. Real-World Scenarios

### 6.1. File and Data Processing

```python
def process_file(filename):
     try:
          with open(filename) as f:
               try:
                    for line in f:
                         print(int(line.strip()))
               except ValueError as e:
                    print(f"Data error: {e}")
     except FileNotFoundError:
          print("File not found.")
```

### 6.2. Network Operations with Retry

```python
import requests
def fetch_with_retry(url):
     for attempt in range(3):
          try:
               try:
                    response = requests.get(url)
                    response.raise_for_status()
                    return response.text
               except requests.HTTPError as e:
                    print(f"HTTP error: {e}")
          except requests.RequestException as e:
               print(f"Network error: {e}")
     print("Failed after 3 attempts.")
```

### 6.3. Database Transactions

```python
import sqlite3
def safe_query(db_path, query):
     try:
          conn = sqlite3.connect(db_path)
          try:
               cursor = conn.cursor()
               cursor.execute(query)
               return cursor.fetchall()
          except sqlite3.DatabaseError as e:
               print(f"Query error: {e}")
          finally:
               conn.close()
     except sqlite3.Error as e:
          print(f"Connection error: {e}")
```

---

## 7. Advanced Usage

- Re-raising exceptions from inner blocks to outer blocks for centralized handling.
- Custom exception classes for layered error reporting.
- Multi-level nesting for complex workflows (use sparingly).

### Example: Re-raising

```python
try:
     try:
          raise ValueError("Bad value!")
     except ValueError as e:
          print(f"Inner: {e}")
          raise  # Propagate to outer
except Exception as e:
     print(f"Outer: {e}")
```

---

## 8. Comparison with Flat Exception Handling

- Flat exception handling uses a single try/except block for all errors.
- Nested handling allows for more precise, context-aware error management.
- Use flat handling for simple scripts; use nesting for complex, layered logic.

---

## 9. Summary and Key Takeaways

- Use nested exception handling for fine-grained, context-specific error management.
- Avoid deep nesting; refactor when possible.
- Always document and test your error handling logic.
- Clean up resources at the right level.

---

This comprehensive guide covers every aspect of nested exception handling in Python, with syntax, examples, best practices, and real-world scenarios. For even more depth, add sections on async code, multi-threading, and integration with third-party libraries as needed.
