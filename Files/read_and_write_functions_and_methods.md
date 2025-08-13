# 📂 Read and Write Functions and Methods in Python

---

## 1. Introduction

Reading and writing files are fundamental operations in Python programming.  
Python provides a **file object** with several methods to read from and write to files.

---

## 2. Opening a File

Before reading or writing, you must open the file using `open()`.

Example:

```python
file = open("example.txt", "r")  # Open for reading
# Do operations
file.close()
```

Recommended:

```python
with open("example.txt", "r") as file:
    # Do operations
    pass
# Automatically closed
```

---

## 3. Reading Methods

### 3.1 `read(size=-1)`

- Reads the file content as a string (text mode) or bytes (binary mode).
- `size`: Number of bytes/characters to read; `-1` means read all.

Example:

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### 3.2 `readline(size=-1)`

- Reads one line at a time.
- `size` limits characters read.

Example:

```python
with open("sample.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1, line2)
```

### 3.3 `readlines(hint=-1)`

- Reads all lines into a list.
- Each list element includes the newline character `\n`.
- `hint` optionally limits total characters.

Example:

```python
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

### 3.4 Iterating Over a File Object

```python
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## 4. Writing Methods

### 4.1 `write(string)`

- Writes the string to the file.
- Returns number of characters written.

Example:

```python
with open("output.txt", "w") as f:
    chars_written = f.write("Hello, World!\n")
    print(f"{chars_written} characters written")
```

### 4.2 `writelines(iterable)`

- Writes multiple strings from an iterable to the file.
- Does not add newline automatically.

Example:

```python
lines = ["First line\n", "Second line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

---

## 5. File Positioning

### 5.1 `tell()`

- Returns current file position in bytes.

Example:

```python
with open("output.txt", "w") as f:
    f.write("Hello")
    print(f.tell())
```

### 5.2 `seek(offset, whence=0)`

- Moves the file pointer to a specific position.
- `whence`:  
  - `0` = beginning of file (default)  
  - `1` = current position  
  - `2` = end of file

Example:

```python
with open("sample.txt", "rb") as f:
    f.seek(5)
    print(f.read(10))
```

---

## 6. Working in Binary Mode

```python
with open("binary.dat", "wb") as f:
    f.write(b"\x00\xFF\x10")

with open("binary.dat", "rb") as f:
    data = f.read()
    print(data)
```

---

## 7. Example: File Copy Program

```python
src = "source.txt"
dst = "destination.txt"

with open(src, "r", encoding="utf-8") as fsrc, open(dst, "w", encoding="utf-8") as fdst:
    for line in fsrc:
        fdst.write(line)
```

---

## 8. Handling Large Files

Instead of reading the entire file into memory, read in chunks:

```python
with open("large_file.txt", "r", encoding="utf-8") as f:
    while True:
        chunk = f.read(1024)  # Read 1KB at a time
        if not chunk:
            break
        process(chunk)
```

---

## 9. Error Handling

```python
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Access denied.")
```

---

## 10. Summary

- `read()`, `readline()`, `readlines()` → For reading.
- `write()`, `writelines()` → For writing.
- Always use `with` to ensure closure.
- Use binary mode for non-text files.
- Handle exceptions for robust code.

---

# 📂 Read and Write Functions and Methods in Python — Part 2 (Advanced Details)

---

## 1. Advanced Reading Techniques

### 1.1 Reading Specific Number of Bytes/Characters

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    first_10_chars = f.read(10)
    print(first_10_chars)
```

- Useful when processing fixed-width files or large files.

### 1.2 Reading Line by Line with Performance in Mind

```python
with open("large.txt", "r", encoding="utf-8") as f:
    for line in f:
        process(line)
```

- This avoids loading the whole file into memory.

### 1.3 Using `iter()` with `readline()`

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in iter(f.readline, ''):
        print(line.strip())
```

- Stops iteration when empty string is returned.

### 1.4 Reading into Memory Efficiently

- For binary data, read in blocks to minimize disk access.

```python
BLOCK_SIZE = 4096
with open("bigfile.bin", "rb") as f:
    while chunk := f.read(BLOCK_SIZE):
        process(chunk)
```

---

## 2. Advanced Writing Techniques

### 2.1 Writing Formatted Data

```python
data = [("Alice", 25), ("Bob", 30)]
with open("people.txt", "w", encoding="utf-8") as f:
    for name, age in data:
        f.write(f"{name}, {age}\n")
```

### 2.2 Writing JSON Data

```python
import json
info = {"name": "Alice", "age": 25}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(info, f, indent=4)
```

### 2.3 Writing CSV Data

```python
import csv
rows = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

### 2.4 Appending Data Safely

- Always open in append mode (`"a"` or `"a+"`) to prevent overwriting.

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Another log entry.\n")
```

---

## 3. File Object Attributes

Once a file is opened, it exposes several attributes:

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.name)       # Filename
    print(f.mode)       # Mode used
    print(f.closed)     # Closed status
    print(f.encoding)   # Encoding used
```

Attributes:

- `name` — Path of file
- `mode` — Access mode
- `closed` — Boolean indicating if file is closed
- `encoding` — Encoding name (text mode only)
- `newlines` — Type of newline characters encountered

---

## 4. File Pointer Control with `seek()` and `tell()`

### 4.1 Using `tell()`

- Returns current position in file.

```python
with open("sample.txt", "r") as f:
    f.read(5)
    print(f.tell())
```

### 4.2 Using `seek()`

- Move pointer to desired position.

```python
with open("sample.txt", "r") as f:
    f.seek(0)  # Move to start
    print(f.read(5))
    f.seek(10)  # Move to byte 10
    print(f.read(5))
```

### 4.3 Seeking from End

```python
with open("sample.txt", "rb") as f:
    f.seek(-10, 2)  # 2 = from end
    print(f.read())
```

---

## 5. Working with Text Encodings

### 5.1 UTF-8

```python
with open("utf8.txt", "w", encoding="utf-8") as f:
    f.write("Hello 🌍")
```

### 5.2 Latin-1

```python
with open("latin1.txt", "w", encoding="latin-1") as f:
    f.write("Olá Mundo")
```

### 5.3 Error Handling in Encoding

```python
text = "Hello 🌍"
with open("ascii.txt", "w", encoding="ascii", errors="replace") as f:
    f.write(text)  # Replaces unsupported chars with '?'
```

---

## 6. Buffering and Performance

### 6.1 Writing with Buffer

```python
with open("buffered.txt", "w", buffering=8192) as f:
    for i in range(100000):
        f.write("Line\n")
```

### 6.2 Flushing the Buffer

```python
with open("flush.txt", "w") as f:
    f.write("Data")
    f.flush()  # Forces write to disk immediately
```

---

## 7. Context Managers in Depth

### 7.1 Nested Context Managers

```python
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())
```

### 7.2 Manual Closing

```python
f = open("file.txt", "r")
try:
    content = f.read()
finally:
    f.close()
```

---

## 8. Best Practices for Read/Write Operations

1. Always use `with` to manage resources.
2. Use binary mode for non-text files.
3. Handle encoding explicitly for text files.
4. Avoid reading large files fully into memory; use chunking.
5. Append instead of overwriting if preserving data is important.
6. Always handle exceptions.

---

## 9. Example Project: Word Frequency Counter

```python
from collections import Counter

with open("sample.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

counter = Counter(words)

with open("word_count.txt", "w", encoding="utf-8") as f:
    for word, count in counter.items():
        f.write(f"{word}: {count}\n")
```

---

## 10. Summary

In this extended part:

- We covered efficient reading/writing techniques.
- Discussed file object attributes.
- Learned advanced pointer control with `seek()` and `tell()`.
- Explored text encodings and buffering.
- Reviewed best practices for robust file handling.

---

## 11. Further Reading

- [Python Official Documentation - File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python - Working with Files in Python](https://realpython.com/python-file-io/)
- [Automate the Boring Stuff with Python - Chapter 8: Files](https://automatetheboringstuff.com/2e/chapter8/)
