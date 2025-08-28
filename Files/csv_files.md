# 📘 CSV Files in Python

## 🔹 Introduction

CSV (Comma-Separated Values) files are widely used to store tabular data in plain text format. Each line represents a row, and values are separated by a delimiter (commonly a comma `,`). Python provides built-in and external libraries to efficiently handle CSV files.

---

## 🔹 Key Characteristics of CSV Files

- **Plain text** format (readable in any text editor).
- **Row-based** structure (one line = one record).
- **Delimiter-based** separation (comma by default, but can be semicolon, tab, etc.).
- **Portable** and easy to exchange between applications (Excel, databases, etc.).

---

## 🔹 Working with CSV in Python

Python provides two main approaches:

1. **Using the built-in `csv` module**
2. **Using `pandas` for data analysis**

---

## 1️⃣ Using the Built-in `csv` Module

### ✅ Reading a CSV File

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of values
```

### ✅ Writing to a CSV File

```python
import csv

rows = [["Name", "Age", "City"],
        ["Alice", 25, "New York"],
        ["Bob", 30, "Paris"]]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

### ✅ Using `DictReader` and `DictWriter`

```python
import csv

# Reading CSV into dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])

# Writing dictionaries into CSV
with open("people.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Country"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 25, "Country": "USA"})
    writer.writerow({"Name": "Bob", "Age": 30, "Country": "France"})
```

---

## 2️⃣ Using Pandas

`pandas` makes working with CSVs easier for large datasets.

### ✅ Reading CSV with pandas

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())  # Display first 5 rows
```

### ✅ Writing CSV with pandas

```python
import pandas as pd

# Example DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
}

df = pd.DataFrame(data)
df.to_csv("people.csv", index=False)
```

### ✅ Handling Custom Delimiters

```python
import pandas as pd

# Reading a TSV (tab-separated values)
df = pd.read_csv("data.tsv", sep="\t")
```

---

## 🔹 Practical Examples

### 📌 Example 1: Filtering Rows from a CSV

```python
import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    high_salary = [row for row in reader if int(row["Salary"]) > 50000]

print(high_salary)
```

### 📌 Example 2: Merging Two CSV Files

```python
import pandas as pd

sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")

merged = pd.merge(sales, customers, on="CustomerID")
merged.to_csv("merged.csv", index=False)
```

### 📌 Example 3: Updating a CSV File

```python
import pandas as pd

df = pd.read_csv("students.csv")
df.loc[df["Name"] == "Alice", "Grade"] = "A+"
df.to_csv("students.csv", index=False)
```

---

## 🔹 Common Issues and Solutions

- **Extra blank lines when writing CSV** → use `newline=''` in `open()`.
- **Encoding errors** → specify encoding (e.g., `encoding='utf-8'`).
- **Large files** → use pandas with `chunksize` for processing.

---

## 🔹 Summary

- Use `csv` module for lightweight operations.
- Use `pandas` for heavy data analysis and manipulation.
- Always share **only** the `.pub` keys when dealing with public sharing.
- Be mindful of delimiters and encodings.

---

✅ With this knowledge, you can handle CSV files professionally, from basic reading/writing to advanced analysis and manipulation.
