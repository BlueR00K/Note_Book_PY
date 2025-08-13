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
