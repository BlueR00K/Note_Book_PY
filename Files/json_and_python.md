# 🗄 JSON: JavaScript Object Notation and Its Usage in Python

---

## 1. Introduction to JSON

**JSON (JavaScript Object Notation)** is a lightweight data-interchange format that is:

- Easy for humans to read and write.
- Easy for machines to parse and generate.
- Language-independent but uses conventions familiar to programmers of the C family.

Python includes a built-in `json` module to work with JSON data.

---

## 2. JSON Syntax

### 2.1 Data Types Supported

JSON supports the following data types:

| JSON Type | Python Equivalent |
|-----------|------------------|
| Object    | dict              |
| Array     | list              |
| String    | str               |
| Number    | int, float        |
| true      | True              |
| false     | False             |
| null      | None              |

### 2.2 Basic Syntax Rules

- Data is in name/value pairs.
- Data is separated by commas.
- Curly braces `{}` hold objects.
- Square brackets `[]` hold arrays.
- Strings are enclosed in double quotes `"`.

Example:

```json
{
    "name": "Alice",
    "age": 30,
    "is_student": false,
    "skills": ["Python", "Machine Learning"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
```

---

## 3. Working with JSON in Python

### 3.1 Importing the Module

```python
import json
```

### 3.2 Parsing JSON Strings to Python Objects

```python
import json

json_data = '{"name": "Alice", "age": 30, "is_student": false}'
python_obj = json.loads(json_data)
print(python_obj)
# Output: {'name': 'Alice', 'age': 30, 'is_student': False}
```

### 3.3 Reading JSON from a File

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
print(data)
```

---

## 4. Converting Python Objects to JSON

### 4.1 Converting to JSON String

```python
import json

person = {"name": "Bob", "age": 25, "is_student": True}
json_str = json.dumps(person)
print(json_str)
```

### 4.2 Writing JSON to a File

```python
with open("output.json", "w") as file:
    json.dump(person, file)
```

---

## 5. Formatting Options in `dumps` and `dump`

```python
import json

data = {"name": "Charlie", "age": 40, "skills": ["Python", "Django"]}

# Pretty print
print(json.dumps(data, indent=4))

# Sort keys
print(json.dumps(data, indent=4, sort_keys=True))

# Custom separators
print(json.dumps(data, separators=(",", ":")))
```

---

## 6. Handling Non-Serializable Objects

Python objects like sets, complex numbers, and custom classes are not directly serializable.

Example:

```python
import json

def complex_encoder(obj):
    if isinstance(obj, complex):
        return {"real": obj.real, "imag": obj.imag}
    raise TypeError("Type not serializable")

cnum = 3 + 4j
print(json.dumps(cnum, default=complex_encoder))
```

---

## 7. Decoding with Custom Logic

```python
import json

def complex_decoder(dct):
    if "real" in dct and "imag" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

json_str = '{"real": 3, "imag": 4}'
print(json.loads(json_str, object_hook=complex_decoder))
```

---

## 8. JSON and File Pointers

When working with large JSON files, `load()` and `dump()` work with file pointers:

```python
with open("data.json", "r") as file:
    data = json.load(file)
```

---

## 9. Streaming and Large JSON Files

For very large JSON files, consider:

- **Iterative parsing** (`ijson` library).
- **Chunked reading**.
- **JSON Lines** format (`.jsonl`).

Example JSON Lines:

```json
{"name": "Alice"}
{"name": "Bob"}
```

---

## 10. JSON vs Other Formats

| Feature     | JSON   | XML     | CSV     |
|-------------|--------|---------|---------|
| Human Readable | ✅   | ✅     | ✅     |
| Hierarchical  | ✅   | ✅     | ❌     |
| Metadata      | ❌   | ✅     | ❌     |
| Compact       | ✅   | ❌     | ✅     |

---

## 11. Security Considerations

- **Do not** load JSON from untrusted sources without validation.
- JSON itself is safe (text format), but the data may contain harmful instructions if passed to unsafe code.
- Validate schema using libraries like `jsonschema`.

---

## 12. Python JSON Module Functions

| Function     | Description |
|--------------|-------------|
| `json.load()`  | Deserialize JSON from file-like object |
| `json.loads()` | Deserialize JSON from string |
| `json.dump()`  | Serialize Python object to file-like object |
| `json.dumps()` | Serialize Python object to string |

---

## 13. Indentation and Readability

```python
import json
data = {"a": 1, "b": 2}
print(json.dumps(data, indent=2, sort_keys=True))
```

---

## 14. Working with APIs

Most modern web APIs use JSON as the data exchange format.

```python
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()
print(data)
```

---

## 15. Summary

- JSON is a lightweight and widely-used format.
- Python’s `json` module makes it easy to encode and decode data.
- Use `load`/`dump` for files and `loads`/`dumps` for strings.
- Custom serialization is possible via `default` and `object_hook`.
