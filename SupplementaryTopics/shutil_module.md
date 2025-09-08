# Practical Methods of the `shutil` Module in Python

- Introduction to the `shutil` module
- Why use the `shutil` module?
- Importing and exploring the module
- File and directory operations (copy, move, remove)
- Advanced copy operations (copy2, copytree, ignore patterns)
- File and directory archiving (make_archive, unpack_archive)
- Disk usage and space management
- Working with temporary files and directories
- Handling symbolic and hard links
- Error handling and exceptions
- Cross-platform considerations
- Integration with other modules (`os`, `pathlib`, `tempfile`)
- Real-world scenarios and practical examples
- Best practices and anti-patterns
- Advanced usage, edge cases, and integration
  - Efficient large file operations
  - Custom copy/move strategies
  - Security and safe deletion
  - Debugging and performance
  - Troubleshooting common errors
  - Real-world advanced scenarios (batch operations, automation)
  - Handling permissions and metadata
  - Working with file-like objects
  - Parallel and asynchronous operations
- Summary and key takeaways

---

## 2. Introduction to the `shutil` Module

The `shutil` module is a part of Python's standard library and provides a higher-level interface for file operations than the `os` module. It is designed for copying, moving, removing files and directories, archiving, disk usage, and more. `shutil` is essential for scripting, automation, and system administration tasks that require robust file management.

---

## 3. Why Use the `shutil` Module?

- Simplifies file and directory operations
- Provides advanced copy and move capabilities
- Supports archiving and extraction
- Offers disk usage and space management tools
- Integrates well with `os`, `pathlib`, and `tempfile`

---

## 4. Importing and Exploring the Module

```python
import shutil
print(dir(shutil))  # List all functions and classes in shutil
help(shutil)        # Get help on the module
```

---

## 5. File and Directory Operations

### Copying Files

```python
import shutil
shutil.copy('source.txt', 'destination.txt')  # Copies file data and permissions
```

### Copying File Metadata

```python
shutil.copy2('source.txt', 'destination.txt')  # Copies file data and all metadata
```

### Moving Files and Directories

```python
shutil.move('file.txt', 'archive/file.txt')
shutil.move('folder1', 'folder2/folder1')
```

### Removing Files and Directories

```python
import os
os.remove('file.txt')  # Remove a file
shutil.rmtree('folder_to_delete')  # Remove a directory tree
```

---

## 6. Advanced Copy Operations

### Copying Directory Trees

```python
shutil.copytree('src_folder', 'dst_folder')
```

### Ignoring Patterns

```python
def ignore_pycache(dir, files):
  return [f for f in files if f.endswith('.pyc') or f == '__pycache__']
shutil.copytree('src', 'dst', ignore=ignore_pycache)
```

---

## 7. File and Directory Archiving

### Creating Archives

```python
shutil.make_archive('backup', 'zip', 'folder_to_archive')
```

### Extracting Archives

```python
shutil.unpack_archive('backup.zip', 'extracted_folder')
```

---

## 8. Disk Usage and Space Management

```python
total, used, free = shutil.disk_usage('.')
print(f'Total: {total // (2**30)} GiB')
print(f'Used: {used // (2**30)} GiB')
print(f'Free: {free // (2**30)} GiB')
```

---

## 9. Working with Temporary Files and Directories

`shutil` works well with the `tempfile` module for creating and cleaning up temporary files and directories.

```python
import tempfile
import shutil
with tempfile.TemporaryDirectory() as tmpdir:
  shutil.copy('file.txt', tmpdir)
  print('Copied to temp dir:', tmpdir)
```

---

## 10. Handling Symbolic and Hard Links

### Copying Symlinks

```python
shutil.copytree('src', 'dst', symlinks=True)
```

### Detecting and Creating Links

```python
import os
os.symlink('target.txt', 'link.txt')
os.link('target.txt', 'hardlink.txt')
```

---

## 11. Error Handling and Exceptions

`shutil` raises exceptions such as `shutil.Error`, `OSError`, and `FileNotFoundError` for failed operations. Always use try/except blocks for robust scripts.

```python
try:
  shutil.copy('nofile.txt', 'dest.txt')
except FileNotFoundError:
  print('Source file not found!')
```

---

## 12. Cross-Platform Considerations

- `shutil` works on Windows, macOS, and Linux
- Use `os.path` or `pathlib` for path manipulations
- Be aware of file permission differences between platforms

---

## 13. Integration with Other Modules

- Use `os` for low-level file operations
- Use `pathlib` for modern path handling
- Use `tempfile` for temporary files and directories

---

## 14. Real-World Scenarios and Practical Examples

### Example: Batch Copying Files

```python
import shutil, os
for filename in os.listdir('src'):
  if filename.endswith('.txt'):
    shutil.copy(os.path.join('src', filename), 'dst')
```

### Example: Archiving a Project Folder

```python
shutil.make_archive('project_backup', 'gztar', 'my_project')
```

---

## 15. Best Practices and Anti-Patterns

- Always handle exceptions and check return values
- Use `copy2` for preserving metadata
- Prefer `copytree` for directories and use `dirs_exist_ok=True` for Python 3.8+
- Clean up temporary files and directories
- Avoid hardcoding paths; use `os.path.join` or `pathlib`
- Use ignore patterns to skip unnecessary files
- Use context managers for temporary resources
- Log operations for audit and debugging

---

## 16. Advanced Usage, Edge Cases, and Integration

### 16.1. Efficient Large File Operations

#### Copying Large Files in Chunks

```python
import shutil
def copy_large_file(src, dst, buffer_size=16*1024*1024):
  with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
    shutil.copyfileobj(fsrc, fdst, length=buffer_size)
copy_large_file('bigfile.bin', 'bigfile_copy.bin')
```

#### Using sendfile (Unix)

On some platforms, `shutil.copyfile` uses `os.sendfile` for efficiency.

---

### 16.2. Custom Copy/Move Strategies

#### Copying Only New or Changed Files

```python
import os, shutil
def copy_if_newer(src, dst):
  if not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
    shutil.copy2(src, dst)
copy_if_newer('a.txt', 'b.txt')
```

#### Selective Directory Copy with Ignore Patterns

```python
def ignore_patterns(dir, files):
  return [f for f in files if f.endswith('.log') or f.startswith('tmp_')]
shutil.copytree('src', 'dst', ignore=ignore_patterns)
```

---

### 16.3. Security and Safe Deletion

#### Securely Deleting Files (Overwriting Before Remove)

```python
import os
def secure_delete(path, passes=3):
  if os.path.isfile(path):
    length = os.path.getsize(path)
    with open(path, 'ba+', buffering=0) as f:
      for _ in range(passes):
        f.seek(0)
        f.write(os.urandom(length))
    os.remove(path)
secure_delete('sensitive.txt')
```

#### Using Trash Instead of Permanent Delete

Use third-party modules like `send2trash` for safer deletes.

---

### 16.4. Debugging and Performance

- Use logging to track file operations
- Profile large batch operations with `cProfile`
- Use `shutil.disk_usage` to monitor space before/after operations

#### Example: Logging File Moves

```python
import shutil, logging
logging.basicConfig(level=logging.INFO)
def move_with_log(src, dst):
  shutil.move(src, dst)
  logging.info(f"Moved {src} to {dst}")
move_with_log('a.txt', 'archive/a.txt')
```

---

### 16.5. Troubleshooting Common Errors

- `FileNotFoundError`: Check source path
- `PermissionError`: Check file permissions and locks
- `shutil.Error`: Multiple errors in batch operations
- `OSError`: Platform-specific issues

#### Example: Robust Batch Copy with Error Handling

```python
import shutil, os
def batch_copy(src_dir, dst_dir):
  errors = []
  for filename in os.listdir(src_dir):
    try:
      shutil.copy2(os.path.join(src_dir, filename), dst_dir)
    except Exception as e:
      errors.append((filename, str(e)))
  if errors:
    print('Errors:', errors)
batch_copy('src', 'dst')
```

---

### 16.6. Real-World Advanced Scenarios

#### Batch Archiving and Extraction

```python
import shutil, os
def archive_all_txt(src_dir, archive_name):
  with open('filelist.txt', 'w') as f:
    for filename in os.listdir(src_dir):
      if filename.endswith('.txt'):
        f.write(os.path.join(src_dir, filename) + '\n')
  shutil.make_archive(archive_name, 'zip', src_dir)
archive_all_txt('docs', 'docs_backup')
```

#### Automated Cleanup of Old Backups

```python
import os, shutil, time
def cleanup_old_backups(backup_dir, days=30):
  now = time.time()
  for filename in os.listdir(backup_dir):
    path = os.path.join(backup_dir, filename)
    if os.path.isfile(path) and now - os.path.getmtime(path) > days*86400:
      os.remove(path)
cleanup_old_backups('backups')
```

#### Parallel File Copy (ThreadPoolExecutor)

```python
import shutil, os
from concurrent.futures import ThreadPoolExecutor
def copy_file(src_dst):
  shutil.copy2(*src_dst)
src_dir, dst_dir = 'src', 'dst'
os.makedirs(dst_dir, exist_ok=True)
files = [(os.path.join(src_dir, f), os.path.join(dst_dir, f)) for f in os.listdir(src_dir)]
with ThreadPoolExecutor() as executor:
  executor.map(copy_file, files)
```

---

### 16.7. Handling Permissions and Metadata

#### Preserving Permissions and Timestamps

```python
import shutil
shutil.copystat('src.txt', 'dst.txt')
```

#### Copying Extended Attributes (Linux/macOS)

Use `os` and third-party modules for xattr support.

---

### 16.8. Working with File-like Objects

#### Copying from Streams

```python
import shutil, io
src = io.BytesIO(b'example data')
with open('output.bin', 'wb') as f:
  shutil.copyfileobj(src, f)
```

#### Copying to Streams

```python
import shutil, io
with open('input.bin', 'rb') as f:
  dst = io.BytesIO()
  shutil.copyfileobj(f, dst)
  print(dst.getvalue())
```

---

### 16.9. Parallel and Asynchronous Operations

#### Parallel Directory Copy (multiprocessing)

```python
import shutil, os
from multiprocessing import Pool
def copy_file(src_dst):
  shutil.copy2(*src_dst)
src_dir, dst_dir = 'src', 'dst'
os.makedirs(dst_dir, exist_ok=True)
files = [(os.path.join(src_dir, f), os.path.join(dst_dir, f)) for f in os.listdir(src_dir)]
with Pool() as pool:
  pool.map(copy_file, files)
```

#### Async File Operations (aiofiles, third-party)

For true async file I/O, use third-party libraries like `aiofiles`.

---

## 17. Summary and Key Takeaways

- The `shutil` module is essential for advanced file and directory management
- Use its advanced features for robust, efficient, and secure automation
- Integrate with other modules for powerful workflows

---
