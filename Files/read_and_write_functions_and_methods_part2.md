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
