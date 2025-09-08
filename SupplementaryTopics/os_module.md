# Practical Methods of the `os` Module in Python

- Introduction to the `os` module
- Why use the `os` module?
- Importing and exploring the module
- File and directory operations
- Path manipulations (`os.path`)
- Environment variables
- Process management
- Working with permissions and metadata
- Traversing directories (`os.walk`)
- Temporary files and directories
- Advanced file handling (symlinks, hard links)
- Cross-platform considerations
- Integration with other modules (`shutil`, `subprocess`, `pathlib`)
- Real-world scenarios and practical examples
- Best practices and anti-patterns
- Advanced usage, edge cases, and integration
  - Handling large directories efficiently
  - Secure temporary files and atomic operations
  - Avoiding race conditions and file locking
  - Security considerations and safe path handling
  - Cross-module integration examples
  - Debugging, performance, and profiling
  - Troubleshooting common errors
  - Real-world advanced scenarios (monitoring, disk usage, parallelism)
- Summary and key takeaways

---

## 2. Introduction to the `os` Module

The `os` module is a standard library in Python that provides a way to interact with the operating system. It offers functions for file and directory manipulation, process management, environment variables, and more, making it essential for scripting, automation, and system programming.

---

## 3. Why Use the `os` Module?

- Provides a portable way to use operating system-dependent functionality
- Enables file, directory, and process management
- Essential for automation, scripting, and system administration
- Works across Windows, macOS, and Linux

---

## 4. Importing and Exploring the Module

```python
import os
print(dir(os))
```

---

## 5. File and Directory Operations

- `os.listdir(path)`: List files and directories
- `os.mkdir(path)`, `os.makedirs(path)`: Create directories
- `os.remove(path)`, `os.rmdir(path)`, `os.removedirs(path)`: Remove files/directories
- `os.rename(src, dst)`: Rename files or directories
- `os.replace(src, dst)`: Atomic rename/replace

```python
os.mkdir('test_dir')
os.listdir('.')
os.rename('test_dir', 'new_dir')
os.rmdir('new_dir')
```

---

## 6. Path Manipulations (`os.path`)

- `os.path.join()`: Join paths
- `os.path.exists()`: Check if a path exists
- `os.path.abspath()`: Absolute path
- `os.path.basename()`, `os.path.dirname()`: File name and directory
- `os.path.splitext()`: Split file extension

```python
import os
path = os.path.join('folder', 'file.txt')
print(os.path.abspath(path))
```

---

## 7. Environment Variables

- `os.environ`: Mapping of environment variables
- `os.getenv(key, default)`: Get environment variable
- `os.putenv(key, value)`: Set environment variable (not recommended; use `os.environ`)

```python
import os
os.environ['MY_VAR'] = 'value'
print(os.getenv('MY_VAR'))
```

---

## 8. Process Management

- `os.system(command)`: Run a shell command
- `os.startfile(path)`: Open a file (Windows)
- `os.exec*()`: Replace current process
- `os.fork()`, `os.spawn*()`: Create new processes (Unix)
- `os.getpid()`, `os.getppid()`: Get process IDs

```python
import os
os.system('echo Hello, world!')
print(os.getpid())
```

---

## 9. Working with Permissions and Metadata

- `os.chmod(path, mode)`: Change permissions
- `os.stat(path)`: Get file metadata
- `os.access(path, mode)`: Test permissions

```python
import os
os.chmod('file.txt', 0o644)
info = os.stat('file.txt')
print(info.st_size)
```

---

## 10. Traversing Directories (`os.walk`)

- `os.walk(top, topdown=True)`: Generate file names in a directory tree

```python
for root, dirs, files in os.walk('.'):
    print(root, dirs, files)
```

---

## 11. Temporary Files and Directories

- Use `tempfile` module for secure temp files/dirs
- `os.tmpdir` (deprecated; use `tempfile.gettempdir()`)

```python
import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
    print('Created temp dir:', tmpdir)
```

---

## 12. Advanced File Handling (Symlinks, Hard Links)

- `os.symlink(src, dst)`: Create symbolic link
- `os.link(src, dst)`: Create hard link
- `os.readlink(path)`: Read a symbolic link

```python
import os
os.symlink('file.txt', 'link.txt')
print(os.readlink('link.txt'))
```

---

## 13. Cross-Platform Considerations

- Use `os.sep`, `os.pathsep`, `os.linesep` for platform-specific separators
- Use `os.name`, `sys.platform` to detect OS
- Prefer `os.path` and `os` functions over hardcoded paths

---

## 14. Integration with Other Modules

- `shutil`: High-level file operations (copy, move, disk usage)
- `subprocess`: Advanced process management
- `pathlib`: Modern path handling (object-oriented)

---

## 15. Real-World Scenarios and Practical Examples

### 15.1. Batch Renaming Files

```python
import os
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        os.rename(filename, 'old_' + filename)
```

### 15.2. Cleaning Up Temporary Files

```python
import os
for filename in os.listdir('.'):
    if filename.endswith('.tmp'):
        os.remove(filename)
```

### 15.3. Environment-Based Configuration

```python
import os
mode = os.getenv('APP_MODE', 'development')
if mode == 'production':
    print('Running in production mode')
```

---

## 16. Best Practices and Anti-Patterns

- Always use `os.path` for path manipulations
- Avoid using `os.system()` for untrusted input (security risk)
- Use `with` statements for file operations
- Prefer `pathlib` for new code
- Clean up resources (temp files, processes)

---

## 17. Advanced Usage, Edge Cases, and Integration

### 17.1. Handling Large Directories Efficiently

When working with directories containing thousands or millions of files, `os.scandir()` is much faster than `os.listdir()` because it yields directory entries lazily and provides file metadata without extra system calls.

```python
import os
with os.scandir('.') as it:
    for entry in it:
        if entry.is_file():
            print(f"File: {entry.name} ({entry.stat().st_size} bytes)")
        elif entry.is_dir():
            print(f"Directory: {entry.name}")
```

#### Edge Case: Symbolic Links

```python
for entry in os.scandir('.'):
    if entry.is_symlink():
        print(f"Symlink: {entry.name} -> {os.readlink(entry.path)}")
```

#### Example: Recursive Directory Size Calculation

```python
def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
print("Total size:", get_dir_size('.'), "bytes")
```

---

### 17.2. Secure Temporary Files

Temporary files should be created using the `tempfile` module to avoid race conditions and security issues. Always use context managers to ensure cleanup.

```python
import tempfile
with tempfile.NamedTemporaryFile(delete=True) as tf:
    tf.write(b'secret')
    tf.flush()
    print('Temporary file:', tf.name)
    # File is deleted automatically
```

#### Edge Case: Temporary Directories

```python
with tempfile.TemporaryDirectory() as tmpdir:
    print('Temporary directory:', tmpdir)
    # Use os and shutil to work inside tmpdir
```

#### Example: Atomic File Write

```python
import tempfile, shutil
def atomic_write(filename, data):
    with tempfile.NamedTemporaryFile('w', delete=False) as tf:
        tf.write(data)
    shutil.move(tf.name, filename)
atomic_write('final.txt', 'important data')
```

---

### 17.3. Avoiding Race Conditions

Race conditions can occur when multiple processes or threads access the same file. Use atomic operations and file locks.

- Use `os.replace` for atomic file moves (overwrites destination safely)
- Use file locks for concurrent access (see `fcntl` on Unix, `msvcrt` on Windows, or third-party modules like `portalocker`)

#### Example: File Locking (Unix)

```python
import fcntl
with open('myfile.txt', 'w') as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    f.write('locked write')
    fcntl.flock(f, fcntl.LOCK_UN)
```

---

### 17.4. Security Considerations

- Always validate user input for file paths (avoid path traversal)
- Avoid using `os.system` with untrusted input (use `subprocess` with argument lists)
- Use absolute paths to avoid directory traversal attacks
- Set restrictive permissions on sensitive files (`os.chmod`)

#### Example: Preventing Path Traversal

```python
import os
def safe_join(base, *paths):
    final_path = os.path.abspath(os.path.join(base, *paths))
    if not final_path.startswith(os.path.abspath(base)):
        raise ValueError('Attempted Path Traversal')
    return final_path
```

---

### 17.5. Cross-Module Integration Example

Combining `os`, `shutil`, and `pathlib` for robust workflows:

```python
from pathlib import Path
import shutil
src = Path('file.txt')
dst = Path('backup') / src.name
shutil.copy(src, dst)
```

#### Example: Using `subprocess` for Safe Shell Commands

```python
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

---

### 17.6. Debugging and Performance

- Use `os.scandir` for fast directory listing
- Use logging to track file and process operations
- Minimize disk I/O by batching operations
- Profile code with `cProfile` or `timeit` for bottlenecks

#### Example: Logging File Operations

```python
import logging, os
logging.basicConfig(level=logging.INFO)
for filename in os.listdir('.'):
    logging.info(f'Found file: {filename}')
```

#### Example: Profiling Directory Traversal

```python
import cProfile
def walk():
    for root, dirs, files in os.walk('.'):
        pass
cProfile.run('walk()')
```

---

### 17.7. Troubleshooting Common Errors

- `FileNotFoundError`: Check path and existence
- `PermissionError`: Check file permissions and user rights
- `OSError`: Inspect error code and message
- `NotADirectoryError`, `IsADirectoryError`: Check file/directory types

#### Example: Robust File Deletion

```python
import os
def safe_remove(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print('File not found:', path)
    except PermissionError:
        print('No permission to delete:', path)
safe_remove('maybe_exists.txt')
```

---

### 17.8. Real-World Advanced Scenarios

#### Monitoring a Directory for Changes (Polling)

```python
import os, time
def monitor_dir(path, interval=5):
    prev = set(os.listdir(path))
    while True:
        time.sleep(interval)
        curr = set(os.listdir(path))
        added = curr - prev
        removed = prev - curr
        if added:
            print('Added:', added)
        if removed:
            print('Removed:', removed)
        prev = curr
# monitor_dir('.')  # Uncomment to run
```

#### Disk Usage Summary (Cross-Platform)

```python
import shutil
total, used, free = shutil.disk_usage('.')
print(f'Total: {total // (2**30)} GiB')
print(f'Used: {used // (2**30)} GiB')
print(f'Free: {free // (2**30)} GiB')
```

#### Safe Recursive Delete with Confirmation

```python
import shutil, os
def safe_rmtree(path):
    if os.path.exists(path):
        confirm = input(f'Delete {path}? (y/n): ')
        if confirm.lower() == 'y':
            shutil.rmtree(path)
            print('Deleted:', path)
        else:
            print('Aborted.')
# safe_rmtree('test_dir')
```

#### Using `os` with `concurrent.futures` for Parallel File Operations

```python
import os
from concurrent.futures import ThreadPoolExecutor
def process_file(filename):
    print('Processing', filename)
with ThreadPoolExecutor() as executor:
    executor.map(process_file, os.listdir('.'))
```

---

## 18. Summary and Key Takeaways

- The `os` module is essential for system programming and automation
- Use its methods for portable, robust, and secure code
- Integrate with other modules for advanced workflows

---
