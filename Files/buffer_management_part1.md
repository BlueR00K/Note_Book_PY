# 📦 Buffer Management in Python — Part 1 (Foundations, Layers, and Practical Control)

> This note is a deep, implementation-aware guide to buffering in Python. It explains what buffering is, how Python layers I/O, how text vs. binary buffering differ, and how to control flush/sync behavior with real, reproducible patterns.

---

## 0) Quick Map (What you’ll master here)

- The 3-layer I/O stack in Python (`Raw` → `Buffered` → `Text`) and why it exists.
- How `open(..., buffering=...)` actually works (line/full/unbuffered).
- The truth about **line buffering** (TTY vs. file/pipe) and **platform differences**.
- The difference between **flush** (`file.flush()`), **OS page cache**, and **durable fsync** (`os.fsync()`/`os.fdatasync()`).
- Choosing buffer sizes, chunked I/O patterns, and zero-copy-ish techniques (`readinto`, `memoryview`).
- How `encoding`, `errors`, and `newline` interact with buffering in **text mode**.
- Practical recipes: fast copying, streaming logs, atomic writes, and progress-safe writes.

---

## 1) What is buffering (for real)?

When you read or write a file/pipe/socket, the OS is **slow** compared to CPU and RAM. Buffering accumulates data in memory into larger chunks before talking to the kernel. Fewer syscalls ⇒ less overhead ⇒ faster I/O.

**Layers of buffering you must remember:**

1. **User-space buffering (Python’s I/O objects)**  
   - Gathers bytes/chars before calling the kernel.  
   - You control this with `open(..., buffering=...)`, `io.Buffered*` classes, and `TextIOWrapper` behavior.

2. **Kernel buffer cache (OS page cache)**  
   - Even after Python flushes, the OS usually still holds data in RAM before committing to disk.  
   - This is why `flush()` ≠ “data is on disk.”

3. **Hardware caches**  
   - Disk controllers/SSDs may also buffer writes.  
   - True durability requires the kernel to order/cache-flush writes to the device (fsync-like calls).

---

## 2) Python’s I/O stack and classes (the mental model)

Python’s file I/O is layered via the `io` module:

```
Raw I/O (lowest):   io.FileIO                -> does OS-level read/write on a file descriptor
Buffered I/O:       io.BufferedReader/Writer -> adds a byte buffer to reduce syscalls
                    io.BufferedRandom        -> for read+write with one buffer
Text I/O (highest): io.TextIOWrapper         -> decodes/encodes text; newline normalization
```

Typically, `open()` builds this stack for you:

```python
# Text mode
f = open("notes.txt", "w", encoding="utf-8")
# Internally (conceptually): FileIO -> BufferedWriter -> TextIOWrapper

# Binary mode
fb = open("photo.jpg", "rb")
# Internally: FileIO -> BufferedReader
```

You can also build layers manually for full control:

```python
import io, os

fd = os.open("data.bin", os.O_RDONLY)
raw = io.FileIO(fd, closefd=True)
buf = io.BufferedReader(raw, buffer_size=64 * 1024)  # 64 KiB
chunk = buf.read(4096)
```

### Why three layers?

- **FileIO**: minimal, thin wrapper around OS syscalls.  
- **Buffered***: amortizes small reads/writes into bigger ones.  
- **TextIOWrapper**: handles encoding/decoding and newline translation on top of the buffered bytes.

---

## 3) `open()` and the `buffering` parameter (line, full, none)

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

- `buffering=-1` (default): choose a **sensible** default:
  - Text files typically get **line buffering** for **interactive TTY** streams, and **block buffering** otherwise.
  - Binary files get **block buffering** with a default buffer size (often 8 KiB or larger depending on platform/Python).
- `buffering=0`: **unbuffered** (binary only). Every `write()` or `read()` goes to the kernel immediately.
- `buffering=1`: **line buffered** (text mode). Flushes on newline and when buffer fills.
- `buffering>1`: **fully buffered** with the specified size in **bytes** for binary and an internal strategy for text.

> ⚠️ **Line buffering caveat**: True line buffering is only *reliably* applied to **text** streams attached to a **TTY** (terminal). When redirected to a file/pipe, Python may fall back to block buffering.

---

## 4) Text vs. binary buffering (and newline rules)

### 4.1 Binary mode (`'b'`)

- You read/write **bytes** (`bytes` / `bytearray`).
- **No newline translation**.
- Buffer sizes are **byte counts**.

### 4.2 Text mode (`'t'`, default)

- You read/write **str** (Unicode). `TextIOWrapper` encodes/decodes around the byte buffer.
- Newline handling is governed by `newline`:
  - `newline=None` (default): translate platform newlines to `\n` on read; write uses `\n` → platform convention.
  - `newline='\n'` / `'\r\n'` / `'\r'`: choose explicit newline handling.
  - `newline=''`: do **no translation**; you get raw newlines as-is.

**Implication:** text buffering operates on **characters** externally but must coordinate with an internal **byte buffer**. Large writes of text may become multiple byte-buffered writes after encoding.

---

## 5) Flushing vs. syncing (crucial difference)

- `file.flush()` → pushes Python’s **user-space** buffer into the **kernel** (OS page cache).  
  - Data is still not guaranteed to be on disk.
- `os.fsync(file.fileno())` / `os.fdatasync(...)` → ask the OS to flush its cache to **stable storage** (durability).  
  - Slower, but required for correctness in crash-sensitive workflows (e.g., databases, critical logs).

**Durable write recipe (text):**

```python
import os, io, tempfile

data = "important payload\n"

# Write atomically to a temp file, fsync it, then rename
dirpath = "."
with tempfile.NamedTemporaryFile("w", dir=dirpath, delete=False, encoding="utf-8") as tmp:
    tmp.write(data)
    tmp.flush()
    os.fsync(tmp.fileno())  # ensure temp file content reaches storage

final_path = "payload.txt"
os.replace(tmp.name, final_path)  # atomic on POSIX for same filesystem
# Optionally fsync the directory to persist the rename in metadata
dirfd = os.open(dirpath, os.O_DIRECTORY)
try:
    os.fsync(dirfd)
finally:
    os.close(dirfd)
```

> Use this pattern when a partial write or power loss could corrupt files the user depends on.

---

## 6) Choosing buffer sizes (rules of thumb)

- Defaults are good. Only tune if you **measure** a bottleneck.  
- Typical sweet spots: **8 KiB–1 MiB** depending on workload and device.  
- For **HDDs/remote FS**, larger buffers often help.  
- For **SSDs**, diminishing returns after ~128 KiB–1 MiB per I/O.  
- For **pipes/sockets**, tune around typical MTUs (4–64 KiB chunks).

**Benchmark mindset:** Always profile with realistic data; micro-benchmarks lie if they don’t mirror your access pattern.

---

## 7) Chunked I/O patterns you should memorize

### 7.1 Fast binary copy (bounded memory)

```python
CHUNK = 1024 * 1024  # 1 MiB
with open("src.bin", "rb") as r, open("dst.bin", "wb") as w:
    while True:
        buf = r.read(CHUNK)
        if not buf:
            break
        w.write(buf)
```

### 7.2 Zero-copy-ish reuse with `readinto` + `memoryview`

```python
CHUNK = 256 * 1024
buf = bytearray(CHUNK)
with open("src.bin", "rb") as r, open("dst.bin", "wb") as w:
    mv = memoryview(buf)
    while True:
        n = r.readinto(buf)    # fills existing buffer; avoids realloc
        if not n:
            break
        w.write(mv[:n])        # no extra copy
```

### 7.3 Line streaming (text) without `readlines()`

```python
with open("big.txt", "r", encoding="utf-8", newline="") as f:
    for line in f:
        process(line)
```

> Prefer iteration over `readlines()` for large files—constant memory, good locality.

---

## 8) `flush()`, `write()` semantics, and line buffering gotchas

- `write()` buffers in memory; it may not reach the kernel until buffer fills or you `flush()`.
- In **line-buffered** text streams attached to a TTY, a newline **triggers a flush**.  
  - Redirect to a **file/pipe**? You often get **block buffering**; newline won’t flush.
- For progress output that must appear immediately regardless of redirection:

```python
print("step 1...", flush=True)
# or
import sys
sys.stdout.write("step 1...\n"); sys.stdout.flush()
```

- Env & CLI switches:
  - `PYTHONUNBUFFERED=1` or `python -u script.py` → unbuffered `stdin/stdout/stderr` (use sparingly).

---

## 9) Understanding `TextIOWrapper` and encoding buffers

`TextIOWrapper` keeps a **decoder** and **encoder** state. Multibyte encodings (e.g., UTF‑8) can straddle chunk boundaries.

- Partial code points may sit in the internal **codec buffer** until enough bytes arrive.
- `errors="replace"` / `"ignore"` change how undecodable data is handled (can silently lose info).

**Explicit control for text:**

```python
with open("log.txt", "w", encoding="utf-8", newline="\n", buffering=1) as f:
    f.write("ready\n")  # likely flushes on TTY; block-buffered when redirected
```

---

## 10) Inspecting file objects (what’s buffered?)

```python
with open("file.txt", "w", encoding="utf-8") as f:
    print(type(f))                  # io.TextIOWrapper
    print(type(f.buffer))           # io.BufferedWriter
    print(type(f.buffer.raw))       # io.FileIO
    print(f.encoding, f.newlines)   # 'utf-8', None/actual newlines seen
```

This reveals the **three-layer stack**. In binary mode, you’ll skip the `TextIOWrapper` layer.

---

## 11) Practical patterns

### 11.1 Real-time-ish logging to file

```python
import time

with open("app.log", "a", buffering=1, encoding="utf-8") as log:  # line-buffered text
    for i in range(3):
        log.write(f"[{time.time():.3f}] tick\n")  # flush likely per line on TTY; block when redirected
        log.flush()  # force immediately regardless of destination
```

### 11.2 Periodic flush to bound data loss

```python
with open("metrics.csv", "a", encoding="utf-8") as out:
    for row in stream_metrics():
        out.write(",".join(map(str, row)) + "\n")
        if need_to_flush_now():
            out.flush()
```

### 11.3 Durable “write-then-rename” (binary)

```python
import os, tempfile

payload = b"critical bytes"
dirpath = "."

with tempfile.NamedTemporaryFile("wb", dir=dirpath, delete=False) as tmp:
    tmp.write(payload)
    tmp.flush()
    os.fsync(tmp.fileno())

os.replace(tmp.name, "safe.bin")
```

### 11.4 Force immediate console progress (even when piped)

```python
import sys, time

for i in range(5):
    sys.stdout.write(f"\rProgress {i}/5")
    sys.stdout.flush()
    time.sleep(0.2)
sys.stdout.write("\n")
```

---

## 12) When **not** to tune buffering

- If you’re CPU‑bound or network‑bound, larger buffers won’t help.
- If your data fits in RAM and the default is already fast, don’t complicate.
- Always **measure** before/after with realistic inputs.

---

## 13) Checklist (Part 1)

- [x] Understand the 3 layers (`FileIO` → `Buffered*` → `TextIOWrapper`).
- [x] Know `buffering=0/1/N` and when it truly takes effect.
- [x] Separate `flush()` from `fsync()` in your mental model.
- [x] Prefer chunked patterns for big data; iteration for text.
- [x] Be explicit about `encoding/newline` for portability.
- [x] Use atomic write when corruption matters.

# 📦 Buffer Management in Python — Part 2 (Advanced Techniques & OS Integration)

---

## Overview

This second part digs into advanced buffer management techniques, OS-level integration, memory-mapped files, compression-stream buffering, spooled temporary files, asynchronous buffering and backpressure, socket/file interoperability, deadlock avoidance, zero-copy transfers, and an actionable performance playbook with benchmarks and tuning recipes.

This document assumes familiarity with Part 1 (I/O stack, buffering modes, flush vs fsync, chunked patterns).

---

## 1. Memory-Mapped Files (`mmap`)

### 1.1 What is `mmap`?

`mmap` maps a file (or portion of it) into memory, letting you access file contents as if they were a bytearray in memory. It can be faster for random access, large files, or when multiple processes share the mapped region.

### 1.2 When to use `mmap`

- Large files where you need random access.
- Sharing memory between processes (POSIX `mmap` with MAP_SHARED).
- Avoiding copy-on-read overhead for certain access patterns.

### 1.3 Basic usage

```python
import mmap, os

with open("large.dat", "r+b") as f:
    size = os.path.getsize(f.name)
    with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as m:
        # treat m like a mutable bytearray
        print(m[0:64])
        m[0:4] = b"\x00\x01\x02\x03"  # write in-place
        m.flush()  # ensure changes reach kernel page cache
```

- `length=0` maps the entire file.
- `m.flush()` flushes modified pages to the kernel; use `os.fsync()` for durable storage.

### 1.4 Caveats and portability

- On Windows, file sizes and mapping semantics differ slightly.
- Mapping a file that grows under you can raise errors; resize the mapping or reopen it.
- `mmap` consumes address space — watch for limits on 32-bit systems.

### 1.5 Advanced pattern: memoryview over mmap

```python
mv = memoryview(m)
chunk = mv[1024:1024+4096]  # zero-copy view slice
process(chunk)
```

This avoids additional copies and integrates well with APIs accepting buffer protocol objects.

---

## 2. `readinto()` and Allocation Minimization

### 2.1 Why `readinto()` matters

`readinto()` fills an existing buffer (e.g., `bytearray`) with data from a stream, avoiding new allocations and reducing GC pressure for high-performance loops.

### 2.2 Example: readinto pattern

```python
CHUNK = 64 * 1024
buf = bytearray(CHUNK)
mv = memoryview(buf)
with open("large.bin", "rb") as f, open("dst.bin", "wb") as w:
    while True:
        n = f.readinto(buf)
        if not n:
            break
        w.write(mv[:n])
```

- `readinto()` returns number of bytes read; it may be less than buffer length.
- Great for steady-state high-throughput copying where allocation churn matters.

### 2.3 Interplay with buffered objects

`readinto()` typically delegates to the underlying raw buffer; behavior can vary across Python versions and implementations. Always benchmark if it's performance-critical.

---

## 3. Compression Streams and Their Buffers (`gzip`, `bz2`, `lzma`)

### 3.1 Overview

Compression wrappers compress/decompress in streaming fashion, and they buffer internally. Their buffer sizes and strategies affect latency and throughput.

### 3.2 `gzip` example (streaming copy)

```python
import gzip, shutil

with open("big.txt", "rb") as fin, gzip.open("big.txt.gz", "wb") as fout:
    shutil.copyfileobj(fin, fout, length=1024*64)  # 64 KB chunks
```

- `gzip.GzipFile` has internal buffering; choosing the chunk size with `copyfileobj` or manual `read()` loops matters.
- Compression also consumes CPU; tune chunk size to balance CPU and I/O.

### 3.3 `bz2` and `lzma`

```python
import bz2, lzma

with bz2.open("file.bz2", "wb") as f:
    f.write(b"data...")

with lzma.open("file.xz", "wb") as f:
    f.write(b"data...")
```

- `lzma` often compresses better but slower; important to benchmark for throughput-sensitive paths.
- These libs implement streaming so you don't need whole-file memory for compression operations.

### 3.4 Example: streaming decompression to mmap'd processing

```python
import gzip, io, mmap
# read compressed file in chunks, decompress incrementally, process via buffers
with gzip.open("data.gz", "rb") as gz:
    while chunk := gz.read(64*1024):
        process(chunk)
```

---

## 4. `SpooledTemporaryFile` and In-memory Buffers that Spill to Disk

`tempfile.SpooledTemporaryFile` stores data in memory up to a threshold and spills to disk after that. Useful when most use-cases fit memory and you want disk fallback for large cases.

```python
from tempfile import SpooledTemporaryFile

with SpooledTemporaryFile(max_size=10*1024*1024, mode="w+t", encoding="utf-8") as s:
    s.write("small data")
    s.seek(0)
    print(s.read())
    # If s grows beyond max_size, it will be written to disk automatically
```

- Use `mode="w+b"` for binary data.
- Avoid relying on `name` attribute when the file spills — it may not have one.

---

## 5. Asyncio, Streams, and Backpressure

### 5.1 Async I/O is cooperative

Async I/O doesn’t magically make disk I/O non-blocking; file I/O is blocking unless performed with threads or libraries like `aiofiles`. Async sockets and pipes do provide non-blocking semantics with built-in backpressure mechanisms.

### 5.2 `asyncio.StreamWriter.drain()`

When writing to an `asyncio` stream, call `await writer.drain()` to wait until the buffer is below the low-water mark; this implements backpressure so the producer doesn’t overwhelm the consumer.

```python
import asyncio

async def send_large_data(writer, data_iter):
    for chunk in data_iter:
        writer.write(chunk)
        await writer.drain()  # backpressure control
    writer.close()
    await writer.wait_closed()
```

### 5.3 Files in asyncio

- Files are generally accessed via thread executors: `loop.run_in_executor()` or `aiofiles` (third-party).
- Be cautious: blocking file I/O inside the main event loop will stall other coroutines.

### 5.4 Example: use threadpool for file reads in async app

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

def blocking_read(path):
    with open(path, "rb") as f:
        return f.read()

async def main(loop):
    with ThreadPoolExecutor() as pool:
        data = await loop.run_in_executor(pool, blocking_read, "big.bin")
        process(data)

asyncio.run(main(asyncio.get_event_loop()))
```

---

## 6. Sockets, `makefile()`, and File-like Wrappers

### 6.1 `socket.makefile()` returns a buffered file object

`sock.makefile()` wraps a socket with a buffered `file` interface (`TextIOWrapper` if text mode requested). This is convenient, but mixing socket `send()/recv()` with file `read()/write()` can break invariants and lead to subtle bugs if you don't flush or shutdown properly.

### 6.2 Recommendations

- Prefer using raw socket methods for precise control of bytes and non-blocking semantics.
- If you use `makefile()`, avoid mixing `sock.send()`/`sock.recv()` with the file object or be careful to flush/close in the correct order.
- On the server side, call `sock.shutdown(socket.SHUT_WR)` before reading remaining data if protocol requires half-close semantics.

### 6.3 Example: basic server using file-like API

```python
import socket

with socket.socket() as s:
    s.bind(("localhost", 9000))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        f = conn.makefile("rwb", buffering=0)
        request = f.readline()
        f.write(b"HTTP/1.0 200 OK\r\n\r\nHello")
        f.flush()
```

---

## 7. Subprocess Pipes and Deadlocks

### 7.1 Common deadlock cause

When a child process writes more data than the OS pipe buffer can hold, and the parent is blocked waiting for the child to finish (e.g., waiting on `proc.wait()`), both can deadlock.

### 7.2 Safe patterns

- Use `proc.communicate()` to read both stdout and stderr and send input; it avoids deadlocks by internally managing reads/writes.
- Read pipes in separate threads or via `select`/`poll` in the parent process.
- Set `bufsize=0` (unbuffered) when calling `Popen` sometimes helps but isn't a cure-all.

### 7.3 Example: using `communicate()`

```python
import subprocess
p = subprocess.Popen(["/usr/bin/someheavy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
```

---

## 8. Zero-Copy and OS-Assisted Transfers

### 8.1 `os.sendfile()` (Unix)

`os.sendfile(out_fd, in_fd, offset, count)` performs a kernel-level transfer from a file descriptor to a socket descriptor without copying data into user-space for many kernels — huge win for performance in file-serving scenarios.

```python
import os, socket

with open("large.iso", "rb") as f:
    sock = socket.create_connection(("example.com", 80))
    # send HTTP headers via sock.sendall(...)
    os.sendfile(sock.fileno(), f.fileno(), 0, os.path.getsize("large.iso"))
```

- Not available on all platforms; check availability and fall back to chunked copy.
- Crucial for high-performance servers (web servers, proxies).

### 8.2 `shutil.copyfileobj()` with large buffer

`shutil.copyfileobj(src, dst, length=BUFFER)` is simple and efficient for many cases; tune `length` to match your environment.

---

## 9. File Descriptor Flags for Durability and Behavior

### 9.1 `os.open()` flags

- `os.O_SYNC` / `os.O_DSYNC`: write operations wait for disk commit (blocking), increasing durability at cost of latency.
- `os.O_DIRECT`: bypass kernel page cache (alignment and permission constraints) — may reduce double-buffering but is platform and FS-dependent.
- `os.O_NONBLOCK`: non-blocking mode on some descriptors (sockets/pipes).

Example:

```python
import os
fd = os.open("data.log", os.O_WRONLY | os.O_CREAT | os.O_SYNC, 0o644)
os.write(fd, b"durable entry\n")
os.close(fd)
```

### 9.2 Portability

Not all OSes support all flags; wrap in `hasattr(os, "O_DIRECT")` checks and use fallbacks. Windows has different semantics (e.g., `FILE_FLAG_WRITE_THROUGH`, `FILE_FLAG_NO_BUFFERING` via `msvcrt` or `ctypes`).

---

## 10. Atomic Writes and Crash-Safe Patterns (Beyond fsync)

### 10.1 Write-then-rename (already covered in Part 1)

- Write to temp file, fsync, rename with `os.replace()` to achieve atomic replacement on POSIX.

### 10.2 Write with checksums and journaling

- For critical data files, write a content+checksum and only replace the active file after verifying.

### 10.3 Journaling/log-append approach

- Append-only logs reduce partial-file corruption risk; maintain checkpoints and compaction processes.

---

## 11. Performance Playbook & Benchmarking

### 11.1 Measurement scaffolding

Use real data and realistic concurrency patterns. Measure end-to-end throughput and latency.

Basic benchmark script for copy speeds with varying chunks:

```python
import time, os, shutil

def copy_bench(src, dst, chunk):
    start = time.time()
    with open(src, "rb") as r, open(dst, "wb") as w:
        shutil.copyfileobj(r, w, length=chunk)
    elapsed = time.time() - start
    size = os.path.getsize(src)
    print(f"chunk={chunk}: {size/elapsed/1024/1024:.2f} MB/s")

for chunk in [4*1024, 16*1024, 64*1024, 256*1024, 1024*1024]:
    copy_bench("large.bin", "out.bin", chunk)
```

### 11.2 What to vary & observe

- Chunk size
- Concurrency level (threads/processes)
- Buffering modes (`buffering` param, `readinto()` vs `read()`)
- Compression level and CPU usage
- Use of `sendfile()` or `mmap`

### 11.3 Real-world metrics

- Throughput (MB/s)
- Latency (time-to-first-byte)
- CPU utilization and context switch rates
- System call counts (`strace`) and I/O waits

---

## 12. Practical Examples & Recipes

### 12.1 High-throughput file server (simple idea)

- Accept sockets with `socket.accept()`
- Use `os.sendfile()` to stream static files to clients
- Close/cleanup carefully; avoid copying to user space

### 12.2 Streaming compress-on-the-fly

- Read file in chunks, compress chunk with `zlib`/`gzip`, write to output stream, call `drain()` if asyncio, or `flush()` for blocking sockets.

### 12.3 Efficient log rotation

- Use `rename + reopen` semantics; rotate by moving old file and letting process reopen a fresh file descriptor (or use signaling to trigger reopen).

---

## 13. Troubleshooting & Common Pitfalls

- **Mixed IO**: Mixing `socket.send()` with `makefile()` reads/writes can deadlock or lose bytes. Avoid mixing or flush/close correctly.
- **Unflushed buffers**: Relying only on `flush()` without `fsync()` will still lose data on power failure.
- **Line buffering surprises**: Assuming `print()` flushes on newline when output is redirected; use `flush=True` if necessary.
- **Read-then-write races**: When multiple processes modify files, coordinate with locks (fcntl/flock) or use atomic replacement.

---

## 14. Additional Tools & Libraries

- `aiofiles` — async file operations (third-party).
- `psutil` — inspect system I/O and process stats for bottleneck analysis.
- `pyperf` / `timeit` — microbenchmarks.
- `uvloop` — faster event loop for asyncio-based servers.

---

## 15. Summary & Action Items

- Use mmap for large random-access workloads; use readinto/memoryview to avoid allocations.
- Use `os.sendfile()` where available to leverage zero-copy transfers.
- Tune chunk sizes but always measure with realistic workloads.
- Use `flush()` + `fsync()` for durability; follow write-then-rename patterns for atomic replacements.
- In async apps, respect backpressure via `await writer.drain()`.
- For subprocess and socket cases, avoid mixing buffered and unbuffered APIs without clear flush/shutdown strategy.

---

## 16. Appendix: Benchmark Script (complete)

Save this as `bench_copy.py` and run on representative data:

```python
#!/usr/bin/env python3
import time, os, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument("src")
parser.add_argument("--out", default="out.bin")
parser.add_argument("--sizes", nargs="+", type=int, default=[4096,16384,65536,262144,1048576])
args = parser.parse_args()

def copy_bench(src, dst, chunk):
    start = time.time()
    with open(src, "rb") as r, open(dst, "wb") as w:
        shutil.copyfileobj(r, w, length=chunk)
    elapsed = time.time() - start
    size = os.path.getsize(src)
    print(f"chunk={chunk}: {size/elapsed/1024/1024:.2f} MB/s, time={elapsed:.3f}s")

for chunk in args.sizes:
    copy_bench(args.src, args.out, chunk)
```

---

## 17. References & Further Reading (short list)

- Python `io` module documentation
- `mmap` module docs
- OS-specific guides on `sendfile`, `fsync`, `O_DIRECT` and `O_SYNC`
- `asyncio` stream docs

---
