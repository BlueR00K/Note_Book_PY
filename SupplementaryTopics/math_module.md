# The `math` Module in Python: Practical Methods and Usages

## 1. Syllabus

- Introduction to the `math` module
- Why use the `math` module?
- Importing and exploring the module
- Common mathematical functions
- Constants in the `math` module
- Advanced mathematical functions
- Working with angles and trigonometry
- Logarithmic and exponential functions
- Special functions (factorial, gcd, etc.)
- Floating-point operations and precision
- Real-world scenarios and practical examples
- Comparison with built-in and NumPy math
- Summary and key takeaways

---

## 2. Introduction to the `math` Module

The `math` module is a standard library in Python that provides access to mathematical functions defined by the C standard. It is designed for floating-point arithmetic and offers a wide range of mathematical operations, constants, and utilities for scientific, engineering, and everyday programming tasks.

---

## 3. Why Use the `math` Module?

- Provides fast, reliable, and accurate mathematical functions
- Offers more advanced operations than Python's built-in operators
- Ensures cross-platform consistency for mathematical calculations
- Essential for scientific computing, engineering, finance, and data analysis

---

## 4. Importing and Exploring the Module

To use the `math` module, import it as follows:

```python
import math
```

You can explore available functions and constants using:

```python
print(dir(math))
```

---

## 5. Common Mathematical Functions

### 5.1. Absolute Value and Rounding

```python
math.fabs(-7.5)      # 7.5 (float absolute value)
math.ceil(2.3)       # 3 (smallest integer >= x)
math.floor(2.7)      # 2 (largest integer <= x)
math.trunc(2.9)      # 2 (truncate towards zero)
```

### 5.2. Power and Roots

```python
math.pow(2, 3)       # 8.0 (2^3)
math.sqrt(16)        # 4.0 (square root)
```

---

## 6. Constants in the `math` Module

- `math.pi` (π): 3.141592...
- `math.e` (Euler's number): 2.718281...
- `math.tau` (τ): 6.283185...
- `math.inf` (infinity)
- `math.nan` (not a number)

---

## 7. Advanced Mathematical Functions

### 7.1. Exponentials and Logarithms

```python
math.exp(2)          # e^2
math.log(8, 2)       # log base 2 of 8
math.log10(100)      # log base 10
math.log2(32)        # log base 2
```

### 7.2. Trigonometric Functions

```python
math.sin(math.pi/2)  # 1.0
math.cos(0)          # 1.0
math.tan(math.pi/4)  # 1.0
```

### 7.3. Inverse Trigonometric Functions

```python
math.asin(1)         # π/2
math.acos(0)         # π/2
math.atan(1)         # π/4
```

---

## 8. Working with Angles

- `math.degrees(x)`: Convert radians to degrees
- `math.radians(x)`: Convert degrees to radians

```python
math.degrees(math.pi)    # 180.0
math.radians(180)        # 3.141592...
```

---

## 9. Special Functions

- `math.factorial(n)`: Factorial of n
- `math.gcd(a, b)`: Greatest common divisor
- `math.lcm(a, b)`: Least common multiple (Python 3.9+)
- `math.comb(n, k)`: Combinations (Python 3.8+)
- `math.perm(n, k)`: Permutations (Python 3.8+)

```python
math.factorial(5)    # 120
math.gcd(24, 36)     # 12
math.lcm(12, 15)     # 60
math.comb(5, 2)      # 10
math.perm(5, 2)      # 20
```

---

## 10. Floating-Point Operations and Precision

- `math.isclose(a, b, rel_tol=1e-9)`: Test if two floats are close
- `math.copysign(x, y)`: Return x with the sign of y
- `math.modf(x)`: Return fractional and integer parts
- `math.frexp(x)`: Decompose float into mantissa and exponent

```python
math.isclose(0.1 + 0.2, 0.3)  # True
math.copysign(3, -1)          # -3.0
math.modf(2.75)               # (0.75, 2.0)
math.frexp(8.0)               # (0.5, 4)
```

---

## 11. Real-World Scenarios and Practical Examples

### 11.1. Calculating Distance Between Two Points

```python
def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

distance(0, 0, 3, 4)  # 5.0
```

### 11.2. Angle Calculations in Robotics

```python
def angle_between(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a*a for a in v1))
    norm2 = math.sqrt(sum(b*b for b in v2))
    return math.acos(dot / (norm1 * norm2))

angle_between([1, 0], [0, 1])  # π/2
```

### 11.3. Financial Calculations

```python
def compound_interest(principal, rate, time):
    return principal * math.pow(1 + rate, time)

compound_interest(1000, 0.05, 10)  # 1628.89
```

---

## 12. Comparison with Built-in and NumPy Math

- The `math` module is for scalar (single value) math, not arrays.
- For array/matrix operations, use NumPy's `numpy.math` or `numpy` functions.
- Built-in functions like `abs`, `round`, and `pow` are less precise for floats than `math` equivalents.

---

## 13. Summary and Key Takeaways

- The `math` module provides essential mathematical functions and constants.
- Use it for accurate, cross-platform, and efficient math operations.
- For advanced or array-based math, consider NumPy.

---

## 14. Advanced Usage and Edge Cases

### 14.1. Handling Special Values: NaN and Infinity

The `math` module provides `math.nan` and `math.inf` for representing special floating-point values. Use `math.isnan(x)` and `math.isinf(x)` to check for these values.

```python
import math
x = float('nan')
print(math.isnan(x))  # True
y = float('inf')
print(math.isinf(y))  # True
```

### 14.2. Dealing with Floating-Point Precision

Floating-point arithmetic can introduce subtle bugs due to precision limitations. Use `math.isclose()` for comparisons.

```python
print(math.isclose(0.1 + 0.2, 0.3))  # True
print(0.1 + 0.2 == 0.3)              # False (due to floating-point error)
```

### 14.3. Performance Considerations

The `math` module is implemented in C and is very fast for scalar operations. For large-scale or vectorized math, use NumPy.

```python
# Scalar math (fast)
math.sqrt(100)
# Vectorized math (use numpy for performance)
import numpy as np
np.sqrt([1, 4, 9, 16])
```

### 14.4. Using `math` with Other Standard Modules

#### 14.4.1. With `random`

```python
import random
angle = random.uniform(0, 2 * math.pi)
print(math.sin(angle))
```

#### 14.4.2. With `statistics`

```python
import statistics
data = [1, 2, 3, 4, 5]
mean = statistics.mean(data)
stddev = statistics.stdev(data)
z_scores = [(x - mean) / stddev for x in data]
```

#### 14.4.3. With `decimal` and `fractions`

The `math` module only works with floats, not `Decimal` or `Fraction` types. Convert as needed.

```python
from decimal import Decimal
from fractions import Fraction
import math
d = Decimal('2.5')
f = Fraction(1, 3)
print(math.sqrt(float(d)))
print(math.sin(float(f)))
```

---

## 15. Best Practices and Anti-Patterns

### 15.1. Best Practices

- Always import the `math` module explicitly.
- Use `math.isclose()` for float comparisons.
- Prefer `math` functions over built-in functions for mathematical accuracy.
- Use `math` for scalar math, NumPy for arrays.
- Document assumptions about input ranges and types.

### 15.2. Anti-Patterns

- Using `math` functions on non-float types (e.g., `Decimal`, `Fraction`) without conversion.
- Relying on exact equality for floating-point numbers.
- Using `math` for array operations (prefer NumPy).

**Example:**

```python
# BAD: math.sqrt on a Decimal
from decimal import Decimal
# math.sqrt(Decimal('2.5'))  # TypeError
# GOOD:
import math
math.sqrt(float(Decimal('2.5')))
```

---

## 16. Advanced Mathematical Topics

### 16.1. Hyperbolic Functions

```python
math.sinh(1)  # Hyperbolic sine
math.cosh(1)  # Hyperbolic cosine
math.tanh(1)  # Hyperbolic tangent
```

### 16.2. Angle Wrapping and Normalization

Keep angles within a specific range (e.g., 0 to 2π):

```python
def wrap_angle(angle):
    return angle % (2 * math.pi)
```

### 16.3. Working with Complex Numbers

The `math` module does not support complex numbers. Use the `cmath` module for complex math.

```python
import cmath
z = complex(1, 1)
print(cmath.sqrt(z))
```

### 16.4. Special Floating-Point Functions

```python
math.isfinite(1.0)  # True
math.isfinite(float('inf'))  # False
```

### 16.5. Gamma and Error Functions

```python
math.gamma(5)      # Gamma function (factorial generalization)
math.erf(1)        # Error function
math.erfc(1)       # Complementary error function
```

---

## 17. Real-World Patterns and Scenarios

### 17.1. Physics: Projectile Motion

```python
def projectile_range(v, theta):
    # v: initial velocity, theta: launch angle in radians
    g = 9.81
    return (v ** 2) * math.sin(2 * theta) / g

projectile_range(10, math.radians(45))  # ~10.19 meters
```

### 17.2. Engineering: Signal Processing

```python
def sine_wave(amplitude, frequency, t):
    return amplitude * math.sin(2 * math.pi * frequency * t)

sine_wave(1, 50, 0.01)
```

### 17.3. Data Science: Normal Distribution PDF

```python
def normal_pdf(x, mu=0, sigma=1):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

normal_pdf(0)
```

### 17.4. Finance: Loan Payment Calculation

```python
def loan_payment(principal, rate, n_periods):
    # Monthly payment for fixed-rate loan
    if rate == 0:
        return principal / n_periods
    r = rate / 12
    return principal * r * math.pow(1 + r, n_periods) / (math.pow(1 + r, n_periods) - 1)

loan_payment(10000, 0.05, 60)
```

### 17.5. Geometry: Area of a Circle

```python
def area_circle(radius):
    return math.pi * radius ** 2

area_circle(5)
```

---

## 18. Documenting and Testing Math Code

- Always document the expected input types and ranges.
- Use doctests or unit tests to verify mathematical functions.
- Consider edge cases (e.g., zero, negative, infinity, NaN).

**Example docstring:**

```python
def safe_log(x):
    """Return the natural logarithm of x. Raises ValueError if x <= 0.

    >>> safe_log(1)
    0.0
    >>> safe_log(0)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    if x <= 0:
        raise ValueError("math domain error")
    return math.log(x)
```

---

## 19. Summary and Final Thoughts

- The `math` module is a foundation for scientific, engineering, and financial programming in Python.
- Understand its limitations (floats only, no arrays, no complex numbers).
- Integrate with other modules for advanced use cases.
- Always test and document mathematical code for reliability.
