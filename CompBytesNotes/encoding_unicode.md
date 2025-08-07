# ASCII, Unicode, Encoding, and Decoding in Python

## 1. Introduction

Text processing is fundamental in programming. To handle text, computers use encoding systems that map characters to numbers (bytes). Understanding ASCII, Unicode, encoding, and decoding is essential for robust, internationalized, and bug-free Python code.

---

## 2. ASCII: The Foundation

- **ASCII (American Standard Code for Information Interchange)** is a 7-bit character encoding standard.
- Represents 128 characters: English letters, digits, punctuation, and control characters (e.g., newline, tab).
- Each character maps to a number (0–127).
- Example: 'A' = 65, 'a' = 97, '0' = 48.
- ASCII is a subset of Unicode.

### Example

```python
print(ord('A'))  # 65
print(chr(65))   # 'A'
```

---

## 3. Unicode: Universal Character Set

- **Unicode** is a standard for representing text in most of the world’s writing systems.
- Supports over 1.1 million code points (characters, symbols, emojis, etc.).
- Unicode assigns a unique code point (e.g., U+1F600 for 😀) to every character.
- Unicode is not an encoding; it’s a character set.

### Example

```python
print(ord('😀'))  # 128512
print('\u2602')   # '☂'
```

---

## 4. Encodings: Turning Characters into Bytes

- **Encoding** is the process of converting Unicode code points to bytes for storage or transmission.
- **Decoding** is the reverse: converting bytes back to Unicode characters.
- Common encodings:
  - **ASCII**: 7 bits, only basic English characters.
  - **UTF-8**: Variable-length, 1–4 bytes per character, backward compatible with ASCII, most common on the web.
  - **UTF-16**: 2 or 4 bytes per character.
  - **UTF-32**: 4 bytes per character.
  - **Latin-1**: 1 byte, Western European languages.
- The same Unicode string can be encoded in different ways.

### Example

```python
s = 'café'
utf8_bytes = s.encode('utf-8')
print(utf8_bytes)  # b'caf\xc3\xa9'
print(utf8_bytes.decode('utf-8'))  # 'café'
```

---

## 5. Python Strings, Bytes, and Encoding

- Python 3 strings (`str`) are sequences of Unicode characters.
- **Bytes** (`bytes`) are sequences of raw 8-bit values.
- To convert between them, use `.encode()` (str → bytes) and `.decode()` (bytes → str).
- Always specify the encoding explicitly for reliability.

### Example

```python
text = 'πython 🐍'
encoded = text.encode('utf-8')
print(encoded)  # b'\xcf\x80ython \xf0\x9f\x90\x8d'
decoded = encoded.decode('utf-8')
print(decoded)  # 'πython 🐍'
```

---

## 6. Byte Order Mark (BOM)

- Some encodings (like UTF-16, UTF-32) may include a BOM at the start of a file to indicate byte order.
- UTF-8 BOM is optional and rarely used.
- Python’s `open()` can handle BOM with the `utf-8-sig` encoding.

---

## 7. Common Pitfalls

- **Mismatched encoding/decoding**: Always decode bytes with the same encoding used to encode them.
- **Non-ASCII characters in source files**: Use `# -*- coding: utf-8 -*-` at the top of Python 2 files.
- **UnicodeDecodeError/UnicodeEncodeError**: Raised when encoding/decoding fails.
- **Surrogate pairs**: Some Unicode characters require two code units in UTF-16.

---

## 8. Working with Files

- Always specify encoding when reading/writing text files.
- Default encoding may vary by OS and locale.

### Example

```python
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('naïve café')
with open('example.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```

---

## 9. Detecting and Handling Encodings

- Use libraries like `chardet` or `cchardet` to guess unknown encodings.
- Use `errors` argument in `.encode()`/`.decode()` to handle errors:
  - `'ignore'`, `'replace'`, `'backslashreplace'`, etc.

### Example

```python
b = b'caf\xe9'
print(b.decode('utf-8', errors='replace'))  # 'caf�'
```

---

## 10. Unicode Normalization

- Unicode can represent the same character in multiple ways (e.g., é as U+00E9 or as 'e' + U+0301).
- Use `unicodedata.normalize()` to standardize representations.

### Example

```python
import unicodedata
s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)  # False
s1_n = unicodedata.normalize('NFC', s1)
s2_n = unicodedata.normalize('NFC', s2)
print(s1_n == s2_n)  # True
```

---

## 11. Real-World Use Cases

- Reading/writing multilingual data
- Web scraping and API data
- Data cleaning and ETL pipelines
- Handling emojis and special symbols
- File format conversions

---

## 12. Advanced Topics

- **Surrogate pairs and astral planes**
- **Combining characters and grapheme clusters**
- **Right-to-left and bidirectional text**
- **Legacy encodings and transcoding**
- **Encoding errors and security**
- **String interning and memory efficiency**

---

## 13. Summary Table

| Concept   | Python Type | Example                | Notes |
|-----------|-------------|------------------------|-------|
| ASCII     | str/bytes   | b'A', 'A'              | 0-127 only |
| Unicode   | str         | 'π', '😀'              | All languages |
| Encoding  | bytes       | b'caf\xc3\xa9'        | Use .encode() |
| Decoding  | str         | 'café'                 | Use .decode() |

---

## 14. Best Practices

- Always specify encoding when reading/writing files.
- Prefer UTF-8 for maximum compatibility.
- Normalize Unicode for comparisons.
- Handle encoding errors gracefully.
- Be aware of platform and library defaults.

---

## Advanced & Real-World Examples

### 1. Detecting File Encoding (with chardet)

Automatically detect the encoding of a file before reading:

```python
import chardet
with open('mystery.txt', 'rb') as f:
    raw = f.read()
result = chardet.detect(raw)
encoding = result['encoding']
print(f"Detected encoding: {encoding}")
text = raw.decode(encoding)
```

### 2. Cleaning Corrupted Text (Handling Decode Errors)

Gracefully handle files with mixed or broken encodings:

```python
with open('broken.txt', 'rb') as f:
    data = f.read()
text = data.decode('utf-8', errors='replace')
print(text)  # Un-decodable bytes become '�'
```

### 3. Emoji Counter in Tweets (Unicode Awareness)

Count the number of emoji characters in a list of tweets:

```python
import re
emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
tweets = ["I love Python 🐍!", "Good morning ☀️", "No emoji here."]
emoji_counts = [len(emoji_pattern.findall(tweet)) for tweet in tweets]
print(emoji_counts)  # Output: [1, 1, 0]
```

### 4. Normalizing User Input for Search

Make user input comparable regardless of accents or case:

```python
import unicodedata
def normalize(text):
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    return text.casefold()
print(normalize('Café'))  # Output: 'cafe'
print(normalize('CAFÉ'))  # Output: 'cafe'
```

### 5. Encoding Data for Web APIs (Base64, UTF-8)

Safely transmit Unicode data in JSON or URLs:

```python
import base64
data = '秘密信息'  # 'Secret message' in Chinese
utf8_bytes = data.encode('utf-8')
b64 = base64.b64encode(utf8_bytes).decode('ascii')
print(b64)  # Output: 5p2o5a+G5paH5Lu2
```

### 6. Fun: ASCII Art Generator

Convert an image to ASCII art (simplified):

```python
from PIL import Image
chars = '@%#*+=-:. '
img = Image.open('cat.png').convert('L').resize((80, 40))
pixels = list(img.getdata())
ascii_str = ''.join(chars[pixel // 25] for pixel in pixels)
for i in range(0, len(ascii_str), 80):
    print(ascii_str[i:i+80])
# Output: ASCII art of the image
```

### 7. Senior: Transcoding Between Encodings

Convert a file from Latin-1 to UTF-8 safely:

```python
with open('legacy.txt', 'r', encoding='latin-1') as src, open('modern.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        dst.write(line)
# Output: 'modern.txt' is now UTF-8 encoded
```

### 8. Advanced: Bidirectional Text Handling

Display right-to-left (RTL) text correctly:

```python
text = 'English עברית'
print(text)  # Output: English עברית (mixed direction)
# For advanced display, use libraries like python-bidi or render in a GUI supporting bidi
```

---
