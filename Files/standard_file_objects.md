# 📂 Standard File Objects in Python

---

## 1. Introduction

In Python, **Standard File Objects** refer to the three core file-like streams provided automatically by the operating system for every running process:

1. **`sys.stdin`** → Standard Input (default: keyboard)
2. **`sys.stdout`** → Standard Output (default: console/screen)
3. **`sys.stderr`** → Standard Error Output (default: console/screen)

These objects are **file-like** because they implement methods similar to regular file objects, such as `read()`, `write()`, and `flush()`.

They are essential for **input/output operations** and **inter-process communication**.

---

## 2. Importing the Standard File Objects

```python
import sys

print(sys.stdin)   # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
print(sys.stdout)  # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
print(sys.stderr)  # <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
```

These are automatically opened by Python when your program starts.

---

## 3. Standard Input – `sys.stdin`

- **Purpose:** Read input from the user or another process.
- **Default Source:** Keyboard input (interactive) or piped data.
- **Mode:** Read (`'r'`), text mode by default.

Example – Reading from `sys.stdin`:

```python
import sys

print("Enter something:")
user_input = sys.stdin.readline()
print(f"You entered: {user_input}")
```

Reading until EOF (End of File):

```python
import sys

print("Paste text and press Ctrl+D (Unix) or Ctrl+Z (Windows) to stop:")
for line in sys.stdin:
    print(f"Line read: {line.strip()}")
```

---

## 4. Standard Output – `sys.stdout`

- **Purpose:** Write normal program output.
- **Default Destination:** Terminal/console window.
- **Mode:** Write (`'w'`), text mode.

Example – Writing to stdout:

```python
import sys

sys.stdout.write("Hello via sys.stdout!\n")
print("Hello via print()")  # Also writes to sys.stdout internally
```

Redirecting stdout to a file:

```python
import sys

with open("output.txt", "w") as f:
    sys.stdout = f
    print("This will be written to output.txt")
```

Restoring stdout:

```python
sys.stdout = sys.__stdout__
```

---

## 5. Standard Error – `sys.stderr`

- **Purpose:** Write error messages and diagnostics.
- **Default Destination:** Terminal/console (separate from stdout).
- **Mode:** Write (`'w'`), text mode.
- **Not buffered** by default → messages appear immediately.

Example – Writing to stderr:

```python
import sys

sys.stderr.write("This is an error message!\n")
```

Useful for separating normal output and error messages in scripts.

---

## 6. Differences Between `stdout` and `stderr`

| Feature             | stdout                      | stderr                         |
|---------------------|-----------------------------|---------------------------------|
| Purpose             | Normal output               | Errors, diagnostics            |
| Buffering           | Usually line-buffered       | Usually unbuffered              |
| Redirection         | Can be redirected separately| Can be redirected separately   |
| Default Destination | Console                     | Console                         |

---

## 7. Buffering Behavior

- **`sys.stdin`**: Buffered by line (input waits until Enter is pressed).
- **`sys.stdout`**: Line-buffered when writing to terminal, fully buffered when writing to files.
- **`sys.stderr`**: Unbuffered by default (useful for error messages).

Force flushing:

```python
import sys

sys.stdout.write("Processing...")
sys.stdout.flush()
```

---

## 8. Binary Versions of Standard Streams

Text streams (`sys.stdin`, `sys.stdout`, `sys.stderr`) are wrappers around binary streams:

```python
import sys

print(sys.stdin.buffer)   # Binary stdin
print(sys.stdout.buffer)  # Binary stdout
print(sys.stderr.buffer)  # Binary stderr
```

You can use `.buffer` to work with raw bytes instead of strings.

Example:

```python
import sys

data = sys.stdin.buffer.read(5)  # Read 5 raw bytes
sys.stdout.buffer.write(data)    # Write bytes back
```

---

## 9. Redirecting Standard Streams

You can redirect standard streams to:

- Files
- Other processes
- `/dev/null` (discard output on Unix)
- Buffers in memory

Example – Redirect stderr to a file:

```python
import sys

with open("errors.log", "w") as err_file:
    sys.stderr = err_file
    sys.stderr.write("Error logged!\n")
```

Example – Redirect stdout to string buffer:

```python
import sys
import io

buffer = io.StringIO()
sys.stdout = buffer
print("Captured output")
sys.stdout = sys.__stdout__

print("Buffer contents:", buffer.getvalue())
```

---

## 10. Using Standard Streams with `with` Statement

Although `sys.stdin`, `sys.stdout`, and `sys.stderr` are open by default, they can still be replaced temporarily inside a `with` block:

```python
import sys

with open("output.txt", "w") as f:
    old_stdout = sys.stdout
    sys.stdout = f
    print("Hello file!")
    sys.stdout = old_stdout
```

---

## 11. Practical Applications

1. **Command-line tools** – Read input from `stdin` and output to `stdout`.
2. **Logging** – Send normal messages to `stdout` and errors to `stderr`.
3. **Pipelining** – Chain commands with `|` in shell.
4. **Testing** – Capture stdout for verification.
5. **Data streaming** – Read/write binary data using `.buffer`.

---

## 12. Summary

- **`sys.stdin`** – Standard Input (keyboard or piped input)
- **`sys.stdout`** – Standard Output (console or redirected output)
- **`sys.stderr`** – Standard Error Output (separate from stdout, unbuffered)

They behave like file objects and support all standard I/O operations.
